"""
EpubProcessingService — orchestrates extraction, AI summarization, and export.
This is the application-layer successor to src/mediator.py.
"""
from typing import Dict, Any, Optional
import json
import os

from infrastructure.epub.epub_extractor import EPUBExtractor
from infrastructure.ai.ollama_agent import AIAgent
from infrastructure.export.marp_exporter import MarpExporter


class EpubProcessingService:
    """Orchestrates the full EPUB → structure → summaries → export workflow."""

    def __init__(
        self,
        ollama_host: str = "http://ollama:11434",
        output_format: str = "text",
    ):
        self._extractor = EPUBExtractor()
        self._ai_agent = AIAgent(ollama_host)
        self._marp_exporter = MarpExporter()
        self._output_format = output_format

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def process_epub(
        self,
        epub_path: str,
        json_output: str,
        generate_summaries: bool = True,
    ) -> Dict[str, Any]:
        """Extract structure from EPUB and optionally add AI summaries."""
        print("=" * 80)
        print("STEP 1: EXTRACTING STRUCTURE")
        print("=" * 80)
        structure = self._extractor.extract_structure(epub_path)

        if generate_summaries:
            print("\n" + "=" * 80)
            print("STEP 2: GENERATING SUMMARIES WITH AI")
            print("=" * 80)
            if not self._ai_agent.test_connection():
                print("⚠️  Could not connect to Ollama. Continuing without summaries.")
            else:
                self._add_summaries_recursive(structure)
                print("\n✓ All summaries generated successfully")

        self._save_to_json(structure, json_output)
        return structure

    def generate_marp_from_json(
        self,
        json_path: str,
        marp_output_path: str,
        title: Optional[str] = None,
        include_summaries: bool = True,
        include_content: bool = False,
        max_depth: int = 3,
    ) -> None:
        """Generate a Marp presentation from a saved JSON structure."""
        out_dir = os.path.dirname(marp_output_path)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)

        self._marp_exporter.export_from_json(
            json_path=json_path,
            output_path=marp_output_path,
            title=title,
            include_summaries=include_summaries,
            include_content=include_content,
            max_depth=max_depth,
        )

    def get_statistics(self, structure: Dict[str, Any]) -> Dict[str, int]:
        """Return basic stats about a processed structure."""
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

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _add_summaries_recursive(
        self, structure: Dict[str, Any], indent: int = 0
    ) -> None:
        for title, info in structure.items():
            prefix = "  " * indent
            print(f"{prefix}📝 Summarizing: {title}")
            info["summary"] = (
                self._ai_agent.summarize_content(info["content"])
                if info.get("content")
                else ""
            )
            if info.get("subsections"):
                self._add_summaries_recursive(info["subsections"], indent + 1)

    def _save_to_json(self, structure: Dict[str, Any], output_path: str) -> None:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(structure, f, ensure_ascii=False, indent=2)
        print(f"✓ Structure saved to: {output_path}")
