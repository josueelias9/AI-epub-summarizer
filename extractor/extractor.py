from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
from typing import Dict, Any
import html2text
import re


class EPUBExtractor:
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
    
    def extract_structure(self, epub_path: str) -> Dict[str, Any]:
        """
        Extract hierarchical structure from EPUB file
        
        Args:
            epub_path: Path to EPUB file
            
        Returns:
            Dict with book structure (content and subsections)
        """
        print(f"📖 Reading EPUB file: {epub_path}")
        book = epub.read_epub(epub_path)
        structure = {}
        
        # Reset counters for new extraction
        self.section_counters = {}

        for item in book.get_items():
            if item.get_type() == ITEM_DOCUMENT:
                soup = BeautifulSoup(item.get_body_content(), 'lxml')

                # Extract h1-h6 headers
                headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                if not headers:
                    continue

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
                    
                    # Generate unique ID for this section
                    section_id = self._generate_section_id(level)
                    
                    # Create entry for this header
                    entry = {
                        "id": section_id,
                        "content": content_text,
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

        print(f"✓ Extraction complete: {len(structure)} main sections found")
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
            print(f"{prefix}→ [{section_id}] {title} ({subsection_count} subsections, {content_length} chars)")
            
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