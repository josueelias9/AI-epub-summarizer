"""
EpubSourcePort adapter for EPUB files stored in Amazon S3.

TBD — this adapter is a placeholder.  Implement once AWS credentials and
bucket configuration are available.
"""

import os

from src.application.ports.service_ports import EpubSourcePort


class S3FileSource(EpubSourcePort):
    """Downloads an EPUB from an S3 bucket to *dest_dir*.

    Args:
        bucket: Name of the S3 bucket.
        region: AWS region (default: ``us-east-1``).

    TBD: inject ``boto3`` session / credentials here.
    """

    def __init__(self, bucket: str, region: str = "us-east-1") -> None:
        self._bucket = bucket
        self._region = region

    def resolve(self, source_ref: str, dest_dir: str) -> str:
        """Download the S3 object identified by *source_ref* to *dest_dir*.

        Args:
            source_ref: S3 object key (e.g. ``"books/my_book.epub"``).
            dest_dir:   Local directory where the file will be written.

        Returns:
            Absolute path to the downloaded file.

        Raises:
            NotImplementedError: Always — this adapter is not yet implemented.
        """
        # TBD: replace with actual boto3 download logic, e.g.:
        #
        #   import boto3
        #   os.makedirs(dest_dir, exist_ok=True)
        #   filename = os.path.basename(source_ref)
        #   dest_path = os.path.join(dest_dir, filename)
        #   s3 = boto3.client("s3", region_name=self._region)
        #   s3.download_file(self._bucket, source_ref, dest_path)
        #   return dest_path
        #
        raise NotImplementedError(
            "S3FileSource is not yet implemented. "
            f"Would download s3://{self._bucket}/{source_ref} to {dest_dir}."
        )
