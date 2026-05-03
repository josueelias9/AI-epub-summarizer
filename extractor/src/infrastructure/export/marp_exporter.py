import logging
import os
import json
from typing import Any, Dict, List, Optional

from src.application.ports.service_ports import MarpExporterPort
from src.enterprise.entities import Book, Chapter

logger = logging.getLogger(__name__)


class MarpExporter(MarpExporterPort):
    """Exporter that converts book structure to Marp presentation format"""
    
    def __init__(self):
        """Initialize Marp exporter with static configuration"""
        pass

    # ------------------------------------------------------------------
    # Clean Architecture port implementation
    # ------------------------------------------------------------------

    def export(
        self,
        book: Book,
        chapters: List[Chapter],
        output_path: str,
        include_summaries: bool = True,
        include_content: bool = False,
        max_depth: int = 3,
    ) -> None:
        """Render a Marp presentation from Book and Chapter entities.

        The chapter hierarchy is reconstructed from ``Chapter.chapter_id``
        before rendering.
        """
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

        # Build parent → children lookup (preserving order)
        children_map: Dict[Optional[str], List[Chapter]] = {}
        for ch in sorted(chapters, key=lambda c: [int(x) for x in c.number.split(".")]):
            children_map.setdefault(ch.chapter_id, []).append(ch)

        title = book.name
        slides: list = [self._generate_title_slide(title)]

        self._render_chapters(
            children_map.get(None, []),
            slides,
            children_map,
            level=1,
            max_depth=max_depth,
            include_summaries=include_summaries,
            include_content=include_content,
        )

        final_content = self._generate_front_matter() + "\n" + "".join(slides)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_content)

        logger.info("Marp presentation exported to: %s (%d slides)", output_path, len(slides))

    def _render_chapters(
        self,
        chapters: List[Chapter],
        slides: list,
        children_map: Dict[Optional[str], List[Chapter]],
        level: int,
        max_depth: int,
        include_summaries: bool,
        include_content: bool,
    ) -> None:
        if level > max_depth:
            return
        for ch in chapters:
            slides.append(self._generate_section_slide(ch.title, level, ""))
            if include_summaries and ch.summary:
                slides.append(self._generate_summary_slide(ch.summary))
            for img_path in ch.list_of_images:
                slides.append(self._generate_image_slide(img_path))
            if ch.content:
                tables = self._extract_tables_from_content(ch.content)
                for idx, table in enumerate(tables, 1):
                    slides.append(self._generate_table_slide(table, idx, ch.title))
            children = children_map.get(ch.id, [])
            if children:
                self._render_chapters(
                    children, slides, children_map,
                    level + 1, max_depth, include_summaries, include_content,
                )


    def export_from_json(
        self,
        json_path: str,
        output_path: str,
        title: Optional[str] = None,
        include_summaries: bool = True,
        include_content: bool = False,
        max_depth: int = 3,
        excluded_ids: Optional[List[str]] = None,
    ) -> None:
        """
        Load a saved book structure (book_with_summaries.json) and export to Marp.

        This method ensures strict slide separation without extra blank lines:
        each slide is separated by a single line containing '---'.

        Args:
            json_path: Path to JSON file containing the book structure with summaries
            output_path: Path to save the Marp markdown file
            title: Presentation title (defaults to first top-level section or a generic title)
            include_summaries: Include summary slides
            include_content: Include full content slides (can be very long)
            max_depth: Maximum heading depth to include
        """
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"JSON structure not found: {json_path}")

        # Ensure output directory exists
        out_dir = os.path.dirname(output_path)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)

        # Load structure from JSON
        with open(json_path, 'r', encoding='utf-8') as f:
            structure: Dict[str, Any] = json.load(f)

        # Derive title if not provided
        if not title:
            title = next(iter(structure.keys()), "Book Summary Presentation")

        # Build slides (without writing yet)
        slides: list[str] = []

        # Title slide
        slides.append(self._generate_title_slide(title))

        # Generate slides from structure
        self._process_structure_recursive(
            structure,
            slides,
            level=1,
            include_summaries=include_summaries,
            include_content=include_content,
            max_depth=max_depth,
            excluded_ids=set(excluded_ids or []),
        )

        # Prepare front matter
        front_matter = self._generate_front_matter()

        # Compose final content: front matter block + strict slide separation
        final_content = front_matter + '\n' + ''.join(slides)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

        logger.info("Marp presentation exported to: %s (%d slides)", output_path, len(slides))
        logger.debug("Source JSON: %s", json_path)
    
    def _generate_front_matter(self) -> str:
        """Generate Marp front matter configuration"""
        return """---
marp: true
theme: default
paginate: true
footer: 'Eng. Josué Huamán'
style: |
  section {
    background-image: url('https://upload.wikimedia.org/wikipedia/commons/5/51/Google_Cloud_logo.svg');
    background-size: 250px;
    background-position: 95% 5%;
    background-repeat: no-repeat;
    opacity: 1;
  }
  section img {
    max-height: 65vh;
    max-width: 85%;
    object-fit: contain;
    display: block;
    margin: 0 auto;
  }

---

<style>
section.centered {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-size: 16px;
}
</style>

---

![bg](https://upload.wikimedia.org/wikipedia/commons/5/51/Google_Cloud_logo.svg)

---"""
    
    def _generate_title_slide(self, title: str) -> str:
        """Generate title slide"""
        return f"""<!-- _class: lead -->
<!-- _paginate: false -->

# {title}

### AI-Generated Book Summary

---"""
    


    
    def _process_structure_recursive(
        self,
        structure: Dict[str, Any],
        slides: list,
        level: int,
        include_summaries: bool,
        include_content: bool,
        max_depth: int,
        excluded_ids: set,
        parent_number: str = ""
    ) -> None:
        """
        Recursively process structure and generate slides
        
        Args:
            structure: Structure dictionary
            slides: List to append slides to
            level: Current heading level
            include_summaries: Include summary slides
            include_content: Include content slides
            max_depth: Maximum depth to process
            parent_number: Parent section numbering (e.g., "1.2")
        """
        if level > max_depth:
            return
        
        for idx, (title, info) in enumerate(structure.items(), 1):

            # Skip sections excluded by the user
            if info.get("id", "") in excluded_ids:
                continue
            
            # Generate section number
            section_number = f"{parent_number}{idx}." if parent_number else f"{idx}."
            
            # Generate section title slide
            slides.append(self._generate_section_slide(title, level, section_number))
            
            # Add summary slide if available
            if include_summaries and info.get("summary"):
                slides.append(self._generate_summary_slide(info["summary"]))

            # Add one full-background slide per image found in this section
            for img_path in info.get("images") or []:
                slides.append(self._generate_image_slide(img_path))


            tables = self._extract_tables_from_content(info["content"])
            for table_idx, table in enumerate(tables, 1):
                slides.append(self._generate_table_slide(table, table_idx, title))
            
            
            # Process subsections recursively
            if info.get("subsections"):
                self._process_structure_recursive(
                    info["subsections"],
                    slides,
                    level + 1,
                    include_summaries,
                    include_content,
                    max_depth,
                    excluded_ids,
                    section_number
                )
                
    
    def _generate_section_slide(self, title: str, level: int, section_number: str) -> str:
        """Generate a section title slide"""
        # Use different styles based on level
        if level == 1:
            return f"""# {section_number} {title}

---

"""
        elif level == 2:
            return f"""## {section_number} {title}

"""
        elif level ==3:
            return f"""### {section_number} {title}

"""
        else:
            return f"""#### {section_number} {title}

"""
    
    def _generate_summary_slide(self, summary: str) -> str:
        """Generate a summary slide"""
        # Split summary into chunks if too long
        max_chars = 700
        
        if len(summary) <= max_chars:
            return f"""{summary}

---

"""
        else:
            # Split into multiple slides by lines to preserve formatting
            lines = summary.split('\n')
            chunks = []
            current_chunk_lines = []
            current_length = 0
            
            for line in lines:
                line_length = len(line) + 1  # +1 for the newline character
                
                # If adding this line would exceed max_chars, start a new chunk
                if current_length + line_length > max_chars and current_chunk_lines:
                    chunks.append('\n'.join(current_chunk_lines))
                    current_chunk_lines = [line]
                    current_length = line_length
                else:
                    current_chunk_lines.append(line)
                    current_length += line_length
            
            # Add remaining lines as the last chunk
            if current_chunk_lines:
                chunks.append('\n'.join(current_chunk_lines))
            
            # Generate slides from chunks
            slides = []
            for i, chunk in enumerate(chunks, 1):
                slides.append(f"""{chunk}

---
""")
            
            return '\n'.join(slides)
    
    def _generate_image_slide(self, image_path: str) -> str:
        """Generate a dedicated slide for an image"""
        return f"""
![center w:85%]({image_path})

---

"""

    def _extract_tables_from_content(self, content: str) -> list:
        """
        Extract Markdown tables from content
        
        Args:
            content: Content string in Markdown format
            
        Returns:
            List of table strings
        """
        if not content:
            return []
        
        import re
        
        # Improved pattern to match Markdown tables
        # Matches: header line with |, separator line with dashes, then data lines
        table_pattern = r'([^\n]*\|[^\n]*\n[-|\s]+\n(?:[^\n]*\|[^\n]*\n?)+)'
        
        tables = []
        matches = re.finditer(table_pattern, content, re.MULTILINE)
        
        for match in matches:
            table_text = match.group(1).strip()
            lines = table_text.split('\n')
            
            # Validate it's a proper table (has at least 3 lines: header, separator, data)
            if len(lines) >= 3:
                # Check if second line looks like a separator (contains - and |)
                second_line = lines[1].strip()
                if '-' in second_line and ('|' in second_line or '---' in second_line):
                    tables.append(table_text)
        
        return tables
    
    def _generate_table_slide(self, table: str, table_number: int, section_title: str) -> str:
        """
        Generate a slide for a table
        
        Args:
            table: Markdown table string
            table_number: Table number within the section
            section_title: Title of the section containing the table
            
        Returns:
            Formatted slide string
        """
        return f"""*{section_title}*
{table}

<!-- _class: centered -->

---

"""

