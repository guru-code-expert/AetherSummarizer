"""LLM summarization module (legacy OpenAI Completion API)."""

from __future__ import annotations

import openai
from .config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def summarize_chunk(chunk: str, max_tokens: int = 250) -> str:
    """
    Generate a concise summary for a single text chunk using text-davinci-003.

    Args:
        chunk: Text chunk to summarize.
        max_tokens: Maximum tokens in the generated summary.

    Returns:
        Summary text (without leading/trailing whitespace quirks).
    """
    prompt = f"Summarize the following passage in clear, concise prose. Limit the summary to approximately 20 printed pages worth of content:\n\n{chunk}"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=max_tokens,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response.choices[0].text.strip()


def summarize_large_text(text: str, chunk_size: int = 3800) -> str:
    """
    Summarize an arbitrarily long text by chunking + iterative summarization.

    Args:
        text: Full input text.
        chunk_size: Size of each chunk sent to the model.

    Returns:
        Final concatenated summary.
    """
    from .text_processor import chunk_text

    chunks = chunk_text(text, chunk_size=chunk_size)
    summaries = [summarize_chunk(c) for c in chunks]
    return "\n\n".join(summaries)