"""One Word From Grandma — entry program.

Writes the single word Grandma would text about AI to /output/entry.txt.

The word is BEEPBOOP: Grandma doing her best robot impression in a text.
Warm, a little baffled, instantly readable, and tied to the machine itself —
the sound she thinks the AI makes. One word, nothing else.
"""

from pathlib import Path

WORD = "BEEPBOOP"
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Self-check against the competition gate: UTF-8 text, 1 to 30
    # characters, not only white space, exactly one word.
    text = WORD.strip()
    assert 1 <= len(text) <= 30, "word must be 1-30 characters"
    assert text == WORD and " " not in text, "entry must be exactly one word"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
