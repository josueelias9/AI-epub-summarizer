"""
Use cases for EPUB extraction, AI summarization, and Marp generation.
Each class has a single responsibility and depends on injected infrastructure.
"""
import logging
from typing import Dict, Any, Optional
import json
import os

from app.infrastructure.epub.epub_extractor import EPUBExtractor
from app.infrastructure.ai.ollama_agent import AIAgent
from app.infrastructure.export.marp_exporter import MarpExporter

logger = logging.getLogger(__name__)


class ExtractEpubUseCase:
    """Extract hierarchical structure from an EPUB and save as JSON. No AI involved."""

    def __init__(self, extractor: EPUBExtractor):
        self._extractor = extractor

    def execute(self, epub_path: str, json_output: str) -> Dict[str, Any]:
        output_dir = os.path.dirname(os.path.abspath(json_output))
        images_output_dir = os.path.join(output_dir, "images")
        structure = self._extractor.extract_structure(epub_path, images_output_dir=images_output_dir)

        # Preserve existing summaries so a re-extract does not wipe AI work
        if os.path.exists(json_output):
            with open(json_output, "r", encoding="utf-8") as f:
                existing = json.load(f)
            self._merge_summaries(existing, structure)

        os.makedirs(os.path.dirname(json_output) or ".", exist_ok=True)
        with open(json_output, "w", encoding="utf-8") as f:
            json.dump(structure, f, ensure_ascii=False, indent=2)
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
    """Load an existing JSON structure, generate AI summaries, and overwrite the file."""

    def __init__(self, ai_agent: AIAgent):
        self._ai_agent = ai_agent

    def execute(self, json_path: str) -> Dict[str, Any]:
        logger.info("Starting summary generation from: %s", json_path)
        with open(json_path, "r", encoding="utf-8") as f:
            structure = json.load(f)

        self._summarize_recursive(structure)
        logger.info("Summary generation completed")

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(structure, f, ensure_ascii=False, indent=2)

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

    def __init__(self, marp_exporter: MarpExporter):
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

    def __init__(self, ai_agent: AIAgent):
        self._ai_agent = ai_agent

    def execute(self) -> Dict[str, Any]:
        logger.info("Checking LLM connection to %s (model: %s)", self._ai_agent.ollama_host, self._ai_agent.model)
        ok = self._ai_agent.test_connection()
        return {
            "connected": ok,
            "host": self._ai_agent.ollama_host,
            "model": self._ai_agent.model,
        }
