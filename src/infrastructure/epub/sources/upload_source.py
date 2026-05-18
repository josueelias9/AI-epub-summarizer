"""
EpubSourcePort adapter for files uploaded from the frontend.

The caller is responsible for reading the file bytes asynchronously before
constructing this object (FastAPI UploadFile.read() is async and cannot be
called from within a synchronous use-case).
"""

import os

from src.application.ports.service_ports import EpubSourcePort


class UploadedFileSource(EpubSourcePort):
    """Writes in-memory bytes (from a frontend multipart upload) to *dest_dir*."""

    def __init__(self, content: bytes, filename: str) -> None:
        self._content = content
        self._filename = os.path.basename(filename)

    def resolve(self, source_ref: str, dest_dir: str) -> str:  # noqa: ARG002
        """Write the uploaded bytes to *dest_dir* and return the resulting path.

        *source_ref* is ignored — the filename is taken from the constructor.
        """
        os.makedirs(dest_dir, exist_ok=True)
        dest_path = os.path.join(dest_dir, self._filename)
        with open(dest_path, "wb") as fh:
            fh.write(self._content)
        return dest_path
