"""
EpubSourcePort adapter for EPUB files already present on the local filesystem.
"""

import os

from src.application.ports.service_ports import EpubSourcePort


class LocalFileSource(EpubSourcePort):
    """Resolves an EPUB from a path on the local filesystem.

    No copying is performed — the file is used in-place.  *dest_dir* is
    accepted for interface compatibility but is not used.
    """

    def resolve(self, source_ref: str, dest_dir: str) -> str:  # noqa: ARG002
        """Validate that *source_ref* points to an existing file and return it.

        Args:
            source_ref: Absolute or relative path to the EPUB file.
            dest_dir:   Unused; kept for interface compatibility.

        Raises:
            FileNotFoundError: If the path does not exist or is not a file.
        """
        if not os.path.isfile(source_ref):
            raise FileNotFoundError(f"EPUB file not found at local path: {source_ref}")
        return source_ref
