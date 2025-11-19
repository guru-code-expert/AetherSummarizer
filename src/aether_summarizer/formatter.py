"""Utility to print long text in paginated format."""

from __future__ import annotations


def print_paginated(
    text: str,
    words_per_page: int = 1600,
    words_per_line: int = 11,
) -> None:
    """
    Print text with page headers and line wrapping to simulate book pages.

    Args:
        text: Text to print.
        words_per_page: Approximate words per printed page.
        words_per_line: Words before line break.
    """
    words = text.split()
    page = 1
    word_count_on_page = 0
    line_word_count = 0

    for word in words:
        if word_count_on_page == 0:
            print("\n" + "=" * 40)
            print(f"Page {page}".center(40))
            print("=" * 40 + "\n")

        print(word, end=" ")
        line_word_count += 1
        word_count_on_page += 1

        if line_word_count == words_per_line:
            print()
            line_word_count = 0

        if word_count_on_page >= words_per_page:
            print("\n")
            page += 1
            word_count_on_page = 0
            line_word_count = 0

    if word_count_on_page > 0:
        print("\n")