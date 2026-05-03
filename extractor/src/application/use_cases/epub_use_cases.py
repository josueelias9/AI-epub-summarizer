"""
Use cases for EPUB extraction, AI summarization, and Marp generation.
Each class has a single responsibility and depends on injected infrastructure.
"""
import logging
import os
from typing import Dict, Any, List, Set

from src.application.ports.service_ports import AIServicePort, EpubExtractorPort, MarpExporterPort, BookRepositoryPort
from src.application.dtos.epub_dtos import (
    ExtractEpubRequest, ExtractEpubResponse,
    SummarizeEpubRequest, SummarizeEpubResponse,
    GenerateMarpRequest, GenerateMarpResponse,
    CheckLLMConnectionResponse,
    ListSectionsRequest, ListSectionsResponse, SectionDTO,
    SetExcludedSectionsRequest, SetExcludedSectionsResponse,
)

logger = logging.getLogger(__name__)


class ExtractEpubUseCase:
    """Extract hierarchical structure from an EPUB and save it. No AI involved."""

    def __init__(self, extractor: EpubExtractorPort, repository: BookRepositoryPort):
        self._extractor = extractor
        self._repository = repository

    def execute(self, request: ExtractEpubRequest) -> ExtractEpubResponse:
        structure = self._extractor.extract_structure(
            request.epub_path, images_output_dir=request.images_output_dir
        )

        existing = self._repository.load_structure(request.book_key)
        if existing:
            self._merge_summaries(existing, structure)

        self._repository.save_structure(request.book_key, structure)

        stats = self._get_statistics(structure)
        return ExtractEpubResponse(
            book_key=request.book_key,
            total_sections=stats["total_sections"],
            total_content_chars=stats["total_content_chars"],
            sections_with_summaries=stats["sections_with_summaries"],
        )

    # TODO: validate that it only works if the content is empty
    def _merge_summaries(self, source: Dict[str, Any], target: Dict[str, Any]) -> None:
        """Copy summaries from an existing structure into the freshly extracted one."""
        for key, info in target.items():
            if key in source and source[key].get("summary"):
                info["summary"] = source[key]["summary"]
            if info.get("subsections") and key in source:
                self._merge_summaries(source[key].get("subsections", {}), info["subsections"])

    def _get_statistics(self, structure: Dict[str, Any]) -> Dict[str, int]:
        stats = {"total_sections": 0, "total_content_chars": 0, "sections_with_summaries": 0}

        def _count(struct: Dict[str, Any]) -> None:
            for info in struct.values():
                stats["total_sections"] += 1
                stats["total_content_chars"] += len(info.get("content", ""))
                if info.get("summary"):
                    stats["sections_with_summaries"] += 1
                if info.get("subsections"):
                    _count(info["subsections"])

        _count(structure)
        return stats


class SummarizeEpubUseCase:
    """Load an existing structure, generate AI summaries, and persist it back."""

    def __init__(self, ai_agent: AIServicePort, repository: BookRepositoryPort):
        self._ai_agent = ai_agent
        self._repository = repository

    def execute(self, request: SummarizeEpubRequest) -> SummarizeEpubResponse:
        logger.info("Starting summary generation for: %s", request.book_key)
        structure = self._repository.load_structure(request.book_key)
        if structure is None:
            raise ValueError(f"No structure found for {request.book_key!r}. Run extract first.")

        excluded_ids = set(self._repository.load_exclusions(request.book_key))
        summarized_count = self._summarize_recursive(structure, excluded_ids)
        logger.info("Summary generation completed")

        self._repository.save_structure(request.book_key, structure)
        return SummarizeEpubResponse(book_key=request.book_key, sections_summarized=summarized_count)

    def _summarize_recursive(self, structure: Dict[str, Any], excluded_ids: Set[str]) -> int:
        count = 0
        for info in structure.values():
            if info.get("id", "") in excluded_ids:
                logger.info("Skipping excluded section id: %s", info.get("id"))
                continue
            logger.info("Summarizing section id: %s", info.get("id"))
            if info.get("content"):
                info["summary"] = self._ai_agent.summarize_content(info["content"])
                count += 1
            else:
                info["summary"] = ""
            if info.get("subsections"):
                count += self._summarize_recursive(info["subsections"], excluded_ids)
        return count


class GenerateMarpUseCase:
    """Generate a Marp markdown presentation from a previously saved structure."""

    def __init__(self, marp_exporter: MarpExporterPort, repository: BookRepositoryPort):
        self._marp_exporter = marp_exporter
        self._repository = repository

    def execute(self, request: GenerateMarpRequest) -> GenerateMarpResponse:
        os.makedirs(os.path.dirname(request.marp_output_path) or ".", exist_ok=True)
        excluded_ids = self._repository.load_exclusions(request.book_key)
        self._marp_exporter.export_from_json(
            json_path=request.book_key,
            output_path=request.marp_output_path,
            title=request.title,
            include_summaries=request.include_summaries,
            include_content=request.include_content,
            max_depth=request.max_depth,
            excluded_ids=excluded_ids,
        )
        return GenerateMarpResponse(marp_output_path=request.marp_output_path)


class CheckLLMConnectionUseCase:
    """Verify that the Ollama LLM service is reachable."""

    def __init__(self, ai_agent: AIServicePort):
        self._ai_agent = ai_agent

    def execute(self) -> CheckLLMConnectionResponse:
        info = self._ai_agent.get_connection_info()
        logger.info("Checking LLM connection to %s (model: %s)", info["host"], info["model"])
        ok = self._ai_agent.test_connection()
        return CheckLLMConnectionResponse(connected=ok, host=info["host"], model=info["model"])


class ListSectionsUseCase:
    """Return a flat list of all sections in a book structure."""

    def __init__(self, repository: BookRepositoryPort):
        self._repository = repository

    def execute(self, request: ListSectionsRequest) -> ListSectionsResponse:
        structure = self._repository.load_structure(request.book_key)
        if structure is None:
            raise ValueError(f"No structure found for {request.book_key!r}. Run extract first.")
        excluded_ids = set(self._repository.load_exclusions(request.book_key))
        sections: List[SectionDTO] = []
        self._collect_recursive(structure, sections, depth=1, excluded_ids=excluded_ids)
        return ListSectionsResponse(book_key=request.book_key, sections=sections)

    def _collect_recursive(
        self,
        structure: Dict[str, Any],
        sections: List[SectionDTO],
        depth: int,
        excluded_ids: Set[str],
    ) -> None:
        for title, info in structure.items():
            sections.append(SectionDTO(
                id=info.get("id", ""),
                title=title,
                depth=depth,
                excluded=info.get("id", "") in excluded_ids,
                has_summary=bool(info.get("summary")),
            ))
            if info.get("subsections"):
                self._collect_recursive(info["subsections"], sections, depth + 1, excluded_ids)


class SetExcludedSectionsUseCase:
    """Persist a set of section IDs that should be excluded from summarization and export."""

    def __init__(self, repository: BookRepositoryPort):
        self._repository = repository

    def execute(self, request: SetExcludedSectionsRequest) -> SetExcludedSectionsResponse:
        excluded_ids = list(request.excluded_ids)

        if request.excluded_titles:
            structure = self._repository.load_structure(request.book_key)
            if structure is None:
                raise ValueError(f"No structure found for {request.book_key!r}. Run extract first.")
            title_set = set(request.excluded_titles)
            ids_from_titles = self._ids_for_titles(structure, title_set)
            excluded_ids = list(set(excluded_ids) | ids_from_titles)

        self._repository.save_exclusions(request.book_key, excluded_ids)
        return SetExcludedSectionsResponse(
            book_key=request.book_key,
            excluded_count=len(excluded_ids),
        )

    def _ids_for_titles(
        self, structure: Dict[str, Any], title_set: Set[str]
    ) -> Set[str]:
        found: Set[str] = set()
        for title, info in structure.items():
            if title in title_set and info.get("id"):
                found.add(info["id"])
            if info.get("subsections"):
                found |= self._ids_for_titles(info["subsections"], title_set)
        return found

