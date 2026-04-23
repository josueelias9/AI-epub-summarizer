"""
Use cases for EPUB extraction and Marp generation.
Each class depends on infrastructure abstractions injected at construction time.
"""
from typing import Dict, Any, Optional
import json
import os

from app.infrastructure.epub.epub_extractor import EPUBExtractor
from app.infrastructure.ai.ollama_agent import AIAgent
from app.infrastructure.export.marp_exporter import MarpExporter


class ExtractEpubUseCase:
    """Extract hierarchical structure from an EPUB, optionally summarise with AI, save as JSON."""

    def __init__(
        self,
        extractor: EPUBExtractor,
        ai_agent: AIAgent,
    ):
        self._extractor = extractor
        self._ai_agent = ai_agent

    def execute(
        self,
        epub_path: str,
        json_output: str,
        generate_summaries: bool = False,
    ) -> Dict[str, Any]:
        structure = self._extractor.extract_structure(epub_path)

        if generate_summaries:
            if self._ai_agent.test_connection():
                self._add_summaries_recursive(structure)

        os.makedirs(os.path.dirname(json_output) or ".", exist_ok=True)
        with open(json_output, "w", encoding="utf-8") as f:
            json.dump(structure, f, ensure_ascii=False, indent=2)

        return structure

    def get_statistics(self, structure: Dict[str, Any]) -> Dict[str, int]:
        stats = {
            "total_sections": 0,
            "total_content_chars": 0,
            "total_summary_chars": 0,
            "sections_with_summaries": 0,
        }

        def _count(struct: Dict[str, Any]) -> None:
            for info in struct.values():
                stats["total_sections"] += 1
                stats["total_content_chars"] += len(info.get("content", ""))
                if info.get("summary"):
                    stats["sections_with_summaries"] += 1
                    stats["total_summary_chars"] += len(info["summary"])
                if info.get("subsections"):
                    _count(info["subsections"])

        _count(structure)
        return stats

    def _add_summaries_recursive(self, structure: Dict[str, Any], indent: int = 0) -> None:
        for title, info in structure.items():
            info["summary"] = (
                self._ai_agent.summarize_content(info["content"])
                if info.get("content")
                else ""
            )
            if info.get("subsections"):
                self._add_summaries_recursive(info["subsections"], indent + 1)


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
