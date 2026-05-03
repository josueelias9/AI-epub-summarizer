import logging
import os
import re
from typing import Any, Dict, List, Optional, Tuple
from uuid import uuid4

from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
import html2text

from src.application.ports.service_ports import EpubExtractorPort
from src.enterprise.entities import Book, Chapter

logger = logging.getLogger(__name__)


class EPUBExtractor(EpubExtractorPort):
    """Extractor for EPUB files that creates hierarchical structure"""
    
    def __init__(self):
        """Initialize the extractor with ID tracking"""
        self.section_counters = {}  # Track numbering by level
    
    def _generate_section_id(self, level: int) -> str:
        """
        Generate a hierarchical ID for a section based on level numbering
        
        Args:
            level: Header level (1-6)
            
        Returns:
            str: Hierarchical section ID (e.g., "1", "1.1", "2.1.1")
        """
        # Initialize counter for this level if not exists
        if level not in self.section_counters:
            self.section_counters[level] = 0
        
        # Reset counters for deeper levels when we encounter a higher level
        levels_to_reset = [l for l in self.section_counters.keys() if l > level]
        for reset_level in levels_to_reset:
            self.section_counters[reset_level] = 0
        
        # Increment counter for current level
        self.section_counters[level] += 1
        
        # Create hierarchical numbering by collecting all levels up to current
        numbering_parts = []
        for l in range(1, level + 1):
            if l in self.section_counters and self.section_counters[l] > 0:
                numbering_parts.append(str(self.section_counters[l]))
        
        # Join with dots to create hierarchical ID
        section_id = '.'.join(numbering_parts)
        
        return section_id
    
    # ------------------------------------------------------------------
    # Clean Architecture port implementation
    # ------------------------------------------------------------------

    def extract(
        self,
        epub_path: str,
        images_output_dir: Optional[str] = None,
    ) -> Tuple[Book, List[Chapter]]:
        """Parse the EPUB, generate a UUID for the book, and return Book + Chapter list.

        The chapter hierarchy is preserved via ``Chapter.chapter_id`` (parent FK).
        Chapter ordering and depth are encoded together in ``Chapter.number``
        (e.g. "1", "2.3", "1.2.1").
        """
        epub_book = epub.read_epub(epub_path)

        # Read Dublin Core metadata
        title_meta = epub_book.get_metadata("DC", "title")
        book_name = title_meta[0][0] if title_meta else os.path.basename(epub_path)
        author_meta = epub_book.get_metadata("DC", "creator")
        author = author_meta[0][0] if author_meta else None
        language_meta = epub_book.get_metadata("DC", "language")
        language = language_meta[0][0] if language_meta else None

        book_id = str(uuid4())
        book = Book(id=book_id, name=book_name, language=language, author=author)

        structure = self.extract_structure(epub_path, images_output_dir)

        chapters: List[Chapter] = []
        self._flatten_structure(structure, chapters, book_id, parent_id=None, number_prefix="")

        return book, chapters

    def _flatten_structure(
        self,
        structure: Dict[str, Any],
        chapters: List[Chapter],
        book_id: str,
        parent_id: Optional[str],
        number_prefix: str,
    ) -> None:
        """Recursively convert the nested structure dict into flat Chapter entities.

        Each chapter receives a UUID as its id. ``parent_id`` carries the UUID of
        the parent chapter so the hierarchy is preserved via ``chapter_id``.
        ``number`` encodes both position and depth (e.g. "1", "2.3", "1.2.1").
        """
        for idx, (title, info) in enumerate(structure.items(), 1):
            number = f"{number_prefix}.{idx}" if number_prefix else str(idx)
            chapter_uuid = str(uuid4())
            chapters.append(
                Chapter(
                    id=chapter_uuid,
                    book_id=book_id,
                    title=title,
                    content=info.get("content", ""),
                    number=number,
                    include=True,
                    list_of_images=info.get("images", []),
                    chapter_id=parent_id,
                )
            )
            if info.get("subsections"):
                self._flatten_structure(
                    info["subsections"],
                    chapters,
                    book_id,
                    parent_id=chapter_uuid,
                    number_prefix=number,
                )

    def extract_structure(self, epub_path: str, images_output_dir: str = None) -> Dict[str, Any]:
        """
        Extract hierarchical structure from EPUB file
        
        Args:
            epub_path: Path to EPUB file
            images_output_dir: Optional directory where EPUB images will be saved.
                               When provided, each section will include an ``images``
                               list with relative paths (e.g. ``images/fig1.png``).
            
        Returns:
            Dict with book structure (content, images, and subsections)
        """
        logger.info("Reading EPUB file: %s", epub_path)
        book = epub.read_epub(epub_path)
        structure = {}
        
        # Reset counters for new extraction
        self.section_counters = {}

        # --- Extract all EPUB images and build lookup map ---
        image_map: Dict[str, str] = {}  # epub_name -> relative output path
        if images_output_dir:
            os.makedirs(images_output_dir, exist_ok=True)
            images_subdir = os.path.basename(images_output_dir)
            for item in book.get_items():
                media_type = getattr(item, 'media_type', '') or ''
                if media_type.startswith('image/'):
                    img_filename = os.path.basename(item.get_name())
                    if not img_filename:
                        continue
                    img_save_path = os.path.join(images_output_dir, img_filename)
                    with open(img_save_path, 'wb') as f:
                        f.write(item.get_content())
                    rel_path = f"{images_subdir}/{img_filename}"
                    # Map by full epub path and by basename for flexible lookup
                    image_map[item.get_name()] = rel_path
                    image_map[img_filename] = rel_path
            logger.info("Extracted %d images to: %s", len(image_map) // 2, images_output_dir)

        for item in book.get_items():
            if item.get_type() == ITEM_DOCUMENT:
                soup = BeautifulSoup(item.get_body_content(), 'lxml')

                # Extract h1-h6 headers
                headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                if not headers:
                    continue

                # Base directory of this HTML item inside the EPUB (for resolving relative img srcs)
                item_dir = os.path.dirname(item.get_name())

                # Stack to maintain current hierarchy
                hierarchy = {}  # {level: (title, dict_reference)}
                
                for i, header in enumerate(headers):
                    level = int(header.name[1])
                    title = header.get_text(strip=True)
                    
                    # Capture content until finding ANY header
                    content_parts = []
                    current = header.find_next_sibling()
                    
                    while current:
                        # Stop if current element IS a header
                        if current.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                            break
                        
                        # Stop if element CONTAINS a header
                        if current.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                            break
                        
                        content_parts.append(str(current))
                        current = current.find_next_sibling()
                    
                    content_html = ''.join(content_parts)
                    
                    # Parse HTML to clean text
                    content_text = self._parse_html_to_text(content_html)

                    # Extract image references for this section
                    images: List[str] = []
                    if image_map:
                        images = self._extract_image_refs(content_html, image_map, item_dir)
                    
                    # Generate unique ID for this section
                    section_id = self._generate_section_id(level)
                    
                    # Create entry for this header
                    entry = {
                        "id": section_id,
                        "content": content_text,
                        "images": images,
                        "subsections": {}
                    }
                    
                    # Clean hierarchy of equal or greater levels
                    hierarchy = {k: v for k, v in hierarchy.items() if k < level}
                    
                    # Add to structure according to level
                    if level == 1:
                        # h1 is root level
                        structure[title] = entry
                        hierarchy[1] = (title, structure[title])
                    else:
                        # Find parent (immediately superior level)
                        parent_level = level - 1
                        while parent_level > 0:
                            if parent_level in hierarchy:
                                parent_title, parent_dict = hierarchy[parent_level]
                                parent_dict["subsections"][title] = entry
                                hierarchy[level] = (title, parent_dict["subsections"][title])
                                break
                            parent_level -= 1

        logger.info("Extraction complete: %d main sections found", len(structure))
        return structure
    
    def _parse_html_to_text(self, html_content: str) -> str:
        """
        Parse HTML content to Markdown format
        
        Args:
            html_content: HTML string
            
        Returns:
            str: Markdown formatted text preserving structure
        """
        if not html_content or not html_content.strip():
            return ""
        
        # Create html2text converter
        h = html2text.HTML2Text()
        
        # Configure converter for better Markdown output
        h.ignore_links = True  # Keep links
        h.ignore_images = True  # Keep images
        h.ignore_emphasis = False  # Keep bold/italic
        h.body_width = 0  # Don't wrap lines
        h.unicode_snob = True  # Use Unicode characters
        h.skip_internal_links = False  # Keep internal links
        h.inline_links = True  # Put links inline
        h.protect_links = True  # Don't break links
        h.mark_code = True  # Mark code blocks
        
        # Convert HTML to Markdown
        markdown_text = h.handle(html_content)
        
        # Clean up extra whitespace while preserving intentional line breaks
        lines = markdown_text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Strip trailing whitespace but preserve the line
            cleaned_line = line.rstrip()
            cleaned_lines.append(cleaned_line)
        
        # Join lines and remove excessive blank lines (more than 2 consecutive)
        result = '\n'.join(cleaned_lines)
        
        # Replace 3+ consecutive newlines with just 2
        import re
        result = re.sub(r'\n{3,}', '\n\n', result)
        
        return result.strip()
    
    def _extract_image_refs(self, html_content: str, image_map: Dict[str, str], item_dir: str) -> List[str]:
        """
        Find <img> tags in HTML and resolve them to saved output paths.

        Args:
            html_content: Raw HTML for a section
            image_map: Mapping of epub paths / basenames → relative output paths
            item_dir: Directory of the HTML item within the EPUB (for resolving relative srcs)

        Returns:
            Ordered, deduplicated list of relative image output paths
        """
        if not html_content:
            return []
        soup = BeautifulSoup(html_content, 'lxml')
        seen = set()
        refs: List[str] = []
        for img in soup.find_all('img'):
            src = img.get('src', '').strip()
            if not src:
                continue
            basename = os.path.basename(src)
            # Try basename lookup first (fastest)
            if basename in image_map:
                path = image_map[basename]
            else:
                # Try resolving full epub-relative path
                resolved = os.path.normpath(os.path.join(item_dir, src)).replace('\\', '/')
                path = image_map.get(resolved) or image_map.get(basename)
            if path and path not in seen:
                seen.add(path)
                refs.append(path)
        return refs

    def print_structure(self, structure: Dict[str, Any], indent: int = 0) -> None:
        """
        Print book structure in readable format
        
        Args:
            structure: Dictionary with structure
            indent: Indentation level
        """
        for title, info in structure.items():
            prefix = "  " * indent
            subsection_count = len(info.get("subsections", {}))
            content_length = len(info.get("content", ""))
            section_id = info.get("id", "no-id")
            logger.debug("%s-> [%s] %s (%d subsections, %d chars)", prefix, section_id, title, subsection_count, content_length)
            
            if info.get("subsections"):
                self.print_structure(info["subsections"], indent + 1)
  


# Usage example
if __name__ == "__main__":
    extractor = EPUBExtractor()
    
    # Extract structure
    epub_path = "my_book.epub"
    structure = extractor.extract_structure(epub_path)
    
    # Print structure
    print("\n" + "="*80)
    print("BOOK STRUCTURE")
    print("="*80 + "\n")
    extractor.print_structure(structure)
    
    # Example: access specific content
    print("\n" + "="*80)
    print("EXAMPLE OF CONTENT ACCESS")
    print("="*80)
    
    for chapter_title, chapter_data in structure.items():
        print(f"\n📖 Chapter: {chapter_title}")
        content_preview = chapter_data["content"][:200] + "..." if len(chapter_data["content"]) > 200 else chapter_data["content"]
        print(f"Content preview: {content_preview}")
        break  # Only show first chapter as example