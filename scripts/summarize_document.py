#!/usr/bin/env python
"""Entry-point script for running the full summarization pipeline and printing."""

import argparse
import os
from src.aether_summarizer.pdf_extractor import extract_text_from_pdf
from src.aether_summarizer.summarizer import summarize_large_text
from src.aether_summarizer.formatter import print_paginated


def main():
    parser = argparse.ArgumentParser(description="Summarize a PDF document")
    parser.add_argument("pdf_path", help="Path to the input PDF file")
    parser.add_argument("--pages", type=int, help="Limit extraction to first N pages")
    args = parser.parse_args()

    pdf_path = os.path.abspath(args.pdf_path)

    print("Extracting text from PDF...")
    raw_text = extract_text_from_pdf(pdf_path, max_pages=args.pages, remove_last_line_per_page=True)

    print(f"Extracted {len(raw_text):,} characters. Starting summarization...")
    summary = summarize_large_text(raw_text)

    print("\n" + "="*60)
    print("FINAL SUMMARY")
    print("="*60 + "\n")
    print_paginated(summary)


if __name__ == "__main__":
    main()