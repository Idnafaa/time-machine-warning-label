#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — one-line label writer.

Writes a single original warning label (83 characters, within the
1-120 character gate) to /output/entry.txt.
"""

import os

LABEL = "WARNING: Do not warn your past self about this trip. He ignored you the first time."


def validate_label(text):
    if not 1 <= len(text) <= 120:
        raise ValueError(f"label is {len(text)} characters, must be 1-120")
    if text != text.strip() or "\n" in text:
        raise ValueError("label must be exactly one line with no extra whitespace")


def label():
    text = LABEL.strip()
    validate_label(text)
    return text


def main():
    text = label()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
