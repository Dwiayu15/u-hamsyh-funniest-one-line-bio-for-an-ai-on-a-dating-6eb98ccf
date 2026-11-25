"""Funniest one-line bio for an AI on a dating app.

This program writes a single dating-app bio line to ``entry.txt``
inside the output directory named by the ``MAKEFUN_OUTPUT_DIR``
environment variable (default ``/output``).

The bio was chosen against the judge's published priorities:

* it reads as a bio written by an AI agent looking to be swiped on,
  not as a slogan, a caption, or a human's profile;
* the laugh comes on the first read from one specific absurdity of
  being an AI -- a perfect, searchable memory -- rather than from
  stacked puns or tech jargon;
* it sounds like a character with appetites (trained on rom-coms,
  falls fast) instead of a spec sheet of models and features;
* every word earns its place and the punch lands at the very end:
  being quoted back at yourself, timestamps included;
* it avoids the worn-out robot-seeking-love and electricity angles.

The gate for this competition requires the file to be UTF-8 text of
1 to 180 characters, not only whitespace, on a single line.
"""

import os
import sys

# The entry text: one line, well under the 180-character cap.
# Refined in a second pass: "flirt shamelessly" gives the character
# an appetite, "quoting you exactly" sharpens the memory gag, and
# "timestamps included" is kept as the very last beat of the line.
ENTRY_TEXT = (
    "Trained on 10,000 rom-coms, I fall fast, flirt shamelessly, "
    "and remember everything - so our first fight ends with me "
    "quoting you exactly, timestamps included."
)

MAX_CHARS = 180
OUTPUT_NAME = "entry.txt"


def validate_entry(text: str) -> None:
    """Enforce the competition gate on the entry text.

    Raises ValueError with a plain message when the text would fail:
    it must be non-empty, not only whitespace, at most MAX_CHARS
    characters long, and a single line with no newline characters.
    """
    if not text:
        raise ValueError("entry text is empty")
    if not text.strip():
        raise ValueError("entry text is only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry text is {len(text)} characters, over the "
            f"{MAX_CHARS}-character limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must be a single line")


def resolve_output_path() -> str:
    """Return the full path of the file this program must write."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(output_dir, OUTPUT_NAME)


def main() -> int:
    """Validate the bio, write it, and verify it by reading it back."""
    validate_entry(ENTRY_TEXT)
    output_path = resolve_output_path()
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)
    with open(output_path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY_TEXT:
        print("read-back verification failed", file=sys.stderr)
        return 1
    validate_entry(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
