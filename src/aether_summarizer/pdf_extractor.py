"""PDF text extraction utilities."""

from __future__ import annotations

import os
from typing import Optional

import pdfplumber


def extract_text_from_pdf(
    pdf_path: str,
    max_pages: Optional[int] = None,
    skip_first_page: bool = False,
    remove_last_line_per_page: bool = True,
) -> str:
    """
    Extract text from a PDF file with optional cleaning.

    Args:
        pdf_path: Absolute or relative path to the PDF file.
        max_pages: If provided, stop after this many pages.
        skip_first_page: Skip the first page (useful for cover pages).
        remove_last_line_per_page: Remove the last line of each page (often page numbers/footer).

    Returns:
        Concatenated cleaned text from the PDF.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    full_text = []
    with pdfplumber.open(pdf_path) as pdf:
        pages = list(pdf.pages)
        start_idx = 1 if skip_first_page else 0

        for page_num, page in enumerate(pages[start_idx:], start=start_idx + 1):
            if max_pages is not None and page_num > max_pages:
                break

            raw_text = page.extract_text()
            if not raw_text:
                continue

            if remove_last_line_per_page:
                lines = raw_text.split("\n")
                if lines:
                    lines.pop()  # remove footer/page number
                raw_text = "\n".join(lines)

            full_text.append(raw_text)

    return "\n".join(full_text)