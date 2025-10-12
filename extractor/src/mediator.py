from src.extractor import EPUBExtractor
from src.ia_agent import AIAgent
from src.marp_exporter import MarpExporter
from typing import Dict, Any
import json
import os


class Mediator:
    """Mediator that connects EPUB Extractor with AI Agent to generate summaries"""
    
    def __init__(self, ollama_host: str = "http://ollama:11434", output_format: str = "text"):
        """
        Initialize mediator
        
        Args:
            ollama_host: Ollama server host
            output_format: Format for content ('text' or 'markdown')
        """
        self.extractor = EPUBExtractor()
        self.ai_agent = AIAgent(ollama_host)
        self.marp_exporter = MarpExporter()
        self.output_format = output_format
    
    def process_epub(self, epub_path: str, json_output: str, generate_summaries: bool = True) -> Dict[str, Any]:
        """
        Process EPUB file: extract structure and optionally generate summaries
        
        Args:
            epub_path: Path to EPUB file
            generate_summaries: If True, generate AI summaries for all content
            
        Returns:
            Dict with complete book structure including summaries
        """
        # Step 1: Extract structure
        print("="*80)
        print("STEP 1: EXTRACTING STRUCTURE")
        print("="*80)
        structure = self.extractor.extract_structure(epub_path)
        
        # Step 2: Generate summaries if requested
        if generate_summaries:
            print("\n" + "="*80)
            print("STEP 2: GENERATING SUMMARIES WITH AI")
            print("="*80)
            
            # Check AI connection
            if not self.ai_agent.test_connection():
                print("⚠️  Could not connect to Ollama. Continuing without summaries.")
                return structure
            
            # Add summaries recursively
            self._add_summaries_recursive(structure)
            print("\n✓ All summaries generated successfully")
        

        self.save_to_json(structure, json_output)
        
        return structure
    
    def _add_summaries_recursive(self, structure: Dict[str, Any], indent: int = 0) -> None:
        """
        Add AI-generated summaries recursively to entire structure
        
        Args:
            structure: Dictionary with book structure
            indent: Indentation level for logging
        """
        for title, info in structure.items():
            prefix = "  " * indent
            print(f"{prefix}📝 Summarizing: {title}")
            
            # Generate summary for content at this level
            if info.get("content"):
                info["summary"] = self.ai_agent.summarize_content(info["content"])
            else:
                info["summary"] = ""
            
            # Process subsections recursively
            if info.get("subsections"):
                self._add_summaries_recursive(info["subsections"], indent + 1)
    
    def print_structure(self, structure: Dict[str, Any], indent: int = 0, show_summaries: bool = True) -> None:
        """
        Print book structure in readable format
        
        Args:
            structure: Dictionary with structure
            indent: Indentation level
            show_summaries: If True, show summaries
        """
        for title, info in structure.items():
            prefix = "  " * indent
            subsection_count = len(info.get("subsections", {}))
            print(f"{prefix}→ {title} ({subsection_count} subsections)")
            
            if show_summaries and info.get("summary"):
                summary_preview = info["summary"][:150] + "..." if len(info["summary"]) > 150 else info["summary"]
                print(f"{prefix}  💡 {summary_preview}")
            
            if info.get("subsections"):
                self.print_structure(info["subsections"], indent + 1, show_summaries)
    
    def save_to_json(self, structure: Dict[str, Any], output_path: str) -> None:
        """
        Save complete structure with summaries to JSON file
        
        Args:
            structure: Book structure with summaries
            output_path: Output file path
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(structure, f, ensure_ascii=False, indent=2)
        print(f"✓ Structure saved to: {output_path}")
    
    def get_statistics(self, structure: Dict[str, Any]) -> Dict[str, int]:
        """
        Calculate statistics about the processed structure
        
        Args:
            structure: Book structure
            
        Returns:
            Dict with statistics
        """
        stats = {
            "total_sections": 0,
            "total_content_chars": 0,
            "total_summary_chars": 0,
            "sections_with_summaries": 0
        }
        
        def count_recursive(struct: Dict[str, Any]):
            for title, info in struct.items():
                stats["total_sections"] += 1
                stats["total_content_chars"] += len(info.get("content", ""))
                
                if info.get("summary"):
                    stats["sections_with_summaries"] += 1
                    stats["total_summary_chars"] += len(info["summary"])
                
                if info.get("subsections"):
                    count_recursive(info["subsections"])
        
        count_recursive(structure)
        return stats

    def generate_marp_from_json(
        self,
        json_path: str,
        marp_output_path: str,
        title: str | None = None,
        include_summaries: bool = True,
        include_content: bool = False,
        max_depth: int = 3,
    ) -> None:
        """
        Generate a Marp presentation directly from a saved JSON structure.

        Args:
            json_path: Path to the JSON structure file (e.g., output/book_with_summaries.json)
            marp_output_path: Path to the Marp markdown output (e.g., output/book_presentation.md)
            title: Optional presentation title; defaults to the first top-level section
            include_summaries: Include summary slides
            include_content: Include full content slides
            max_depth: Maximum depth to include
        """
        # Ensure output directory exists
        out_dir = os.path.dirname(marp_output_path)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)

        self.marp_exporter.export_from_json(
            json_path=json_path,
            output_path=marp_output_path,
            title=title,
            include_summaries=include_summaries,
            include_content=include_content,
            max_depth=max_depth,
        )


# Usage example
if __name__ == "__main__":
    # Example 1: Full workflow with Marp export
    # print("="*80)
    # print("FULL WORKFLOW: EPUB → SUMMARIES → MARP PRESENTATION")
    # print("="*80)
    
    # # Create mediator with Markdown format (recommended for Marp)
    mediator = Mediator(ollama_host="http://ollama:11434", output_format="markdown")
    
    # # Process EPUB with summaries
    json_output = os.path.join("output", "book_with_summaries.json")
    epub_path = "my_book.epub"
    mediator.process_epub(epub_path,json_output, generate_summaries=True)
    
    # # Display structure with summaries
    # print("\n" + "="*80)
    # print("BOOK STRUCTURE WITH SUMMARIES")
    # print("="*80 + "\n")
    # mediator.print_structure(structure, show_summaries=True)
    
    # # Show statistics
    # print("\n" + "="*80)
    # print("STATISTICS")
    # print("="*80)
    # stats = mediator.get_statistics(structure)
    # for key, value in stats.items():
    #     print(f"{key}: {value}")
     
    # Export to Marp presentation
    print("\n" + "="*80)
    print("EXPORTING TO MARP PRESENTATION")
    print("="*80)
    
    # Export full presentation
    marp_output = os.path.join("output", "book_presentation.md")
    mediator.generate_marp_from_json(
        json_path=json_output,
        marp_output_path=marp_output,
        title="Book Summary Presentation",
        include_summaries=True,
        include_content=False,
        max_depth=4,
    )
    