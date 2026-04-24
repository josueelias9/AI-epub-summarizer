"""
Use cases for EPUB extraction, AI summarization, and Marp generation.
Each class has a single responsibility and depends on injected infrastructure.
"""
import logging
from typing import Dict, Any, Optional
import os

from app.application.ports.service_ports import AIServicePort, EpubExtractorPort, MarpExporterPort, StructureRepositoryPort

logger = logging.getLogger(__name__)


class ExtractEpubUseCase:
    """Extract hierarchical structure from an EPUB and save as JSON. No AI involved."""

    def __init__(self, extractor: EpubExtractorPort, repository: StructureRepositoryPort):
        self._extractor = extractor
        self._repository = repository

    def execute(
        self,
        epub_path: str,
        book_key: str,
        images_output_dir: Optional[str] = None,
    ) -> Dict[str, Any]:
        structure = self._extractor.extract_structure(epub_path, images_output_dir=images_output_dir)

        existing = self._repository.load(book_key)
        if existing:
            self._merge_summaries(existing, structure)

        self._repository.save(book_key, structure)
        return structure

    # TODO: validate that it only works if the content is empty
    def _merge_summaries(self, source: Dict[str, Any], target: Dict[str, Any]) -> None:
        """Copy summaries from an existing JSON structure into the freshly extracted one."""
        for key, info in target.items():
            if key in source and source[key].get("summary"):
                info["summary"] = source[key]["summary"]
            if info.get("subsections") and key in source:
                self._merge_summaries(source[key].get("subsections", {}), info["subsections"])

    def get_statistics(self, structure: Dict[str, Any]) -> Dict[str, int]:
        stats = {
            "total_sections": 0,
            "total_content_chars": 0,
            "sections_with_summaries": 0,
        }

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

    def __init__(self, ai_agent: AIServicePort, repository: StructureRepositoryPort):
        self._ai_agent = ai_agent
        self._repository = repository

    def execute(self, book_key: str) -> Dict[str, Any]:
        logger.info("Starting summary generation for: %s", book_key)
        structure = self._repository.load(book_key)
        if structure is None:
            raise ValueError(f"No structure found for {book_key!r}. Run extract first.")

        self._summarize_recursive(structure)
        logger.info("Summary generation completed")

        self._repository.save(book_key, structure)
        return structure
    def _summarize_recursive(self, structure: Dict[str, Any]) -> None:
        for info in structure.values():
            logger.info("Summarizing section id: %s", info.get("id"))
            info["summary"] = (
                self._ai_agent.summarize_content(info["content"])
                if info.get("content")
                else ""
            )
            if info.get("subsections"):
                self._summarize_recursive(info["subsections"])


class GenerateMarpUseCase:
    """Generate a Marp markdown presentation from a previously saved JSON structure."""

    def __init__(self, marp_exporter: MarpExporterPort):
        self._marp_exporter = marp_exporter

    def execute(
        self,
        json_path: str,
        marp_output_path: str,
        title: Optional[str] = None,
        include_summaries: bool = True,
        include_content: bool = False,
        max_depth: int = 3,
    ) -> None:
        os.makedirs(os.path.dirname(marp_output_path) or ".", exist_ok=True)
        self._marp_exporter.export_from_json(
            json_path=json_path,
            output_path=marp_output_path,
            title=title,
            include_summaries=include_summaries,
            include_content=include_content,
            max_depth=max_depth,
        )


class CheckLLMConnectionUseCase:
    """Verify that the Ollama LLM service is reachable."""

    def __init__(self, ai_agent: AIServicePort):
        self._ai_agent = ai_agent

    def execute(self) -> Dict[str, Any]:
        info = self._ai_agent.get_connection_info()
        logger.info("Checking LLM connection to %s (model: %s)", info["host"], info["model"])
        ok = self._ai_agent.test_connection()
        return {
            "connected": ok,
            "host": info["host"],
            "model": info["model"],
        }
