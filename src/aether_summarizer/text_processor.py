"""Text chunking utilities."""

from __future__ import annotations

from typing import List


def chunk_text(text: str, chunk_size: int = 3800, overlap: int = 200) -> List[str]:
    """
    Split text into overlapping chunks suitable for LLM context windows.

    Args:
        text: Input text.
        chunk_size: Target size per chunk (in characters).
        overlap: Number of characters to overlap between chunks.

    Returns:
        List of text chunks.
    """
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap  # move back by overlap for next chunk

        if end >= len(text):
            break

    return chunks