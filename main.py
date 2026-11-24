"""One Word From Grandma — entry program.

Writes the single word Grandma would text about AI to /output/entry.txt.

The word is BEEPBOOP: Grandma doing her best robot impression in a text.
Warm, a little baffled, instantly readable, and tied to the machine itself —
the sound she thinks the AI makes. One word, nothing else.
"""

from pathlib import Path

WORD = "BEEPBOOP"
OUTPUT = Path("/output/entry.txt")


def validate(word: str) -> str:
    """Enforce the competition gate on the word before it is written.

    The sealed gate accepts UTF-8 text of 1 to 30 characters, not only
    white space; the judge brief wants exactly one word, no sentence,
    no explanation, no punctuation tricks. Anything failing here must
    never reach /output/entry.txt.
    """
    if not (1 <= len(word) <= 30):
        raise ValueError(f"word must be 1-30 characters, got {len(word)}")
    if not word.strip():
        raise ValueError("word must not be only white space")
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word, no white space")
    if any(not ch.isalpha() for ch in word):
        raise ValueError("entry must be letters only, no punctuation tricks")
    return word


def main() -> None:
    text = validate(WORD)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")
    # Round-trip check: what the judge will read must be exactly the word.
    if OUTPUT.read_text(encoding="utf-8") != text:
        raise RuntimeError("written entry does not match the word")


if __name__ == "__main__":
    main()
