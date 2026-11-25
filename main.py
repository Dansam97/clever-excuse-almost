"""Entry for make.fun bounty u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.

Writes one line to entry.txt in the output directory: the excuse a gamer
texts their boss to skip work on GTA 6 launch week. The judge plays a tired
manager and picks the excuse it would almost believe, so the line leans on a
specific, boring, verifiable-sounding detail: the council has dug up the
street, sealed the car in, and the road is shut all week.
"""

import os

ENTRY_TEXT = (
    "sorry, can't come in, council's dug up our street and sealed my car in, "
    "road's shut all week apparently"
)


MAX_WORDS = 20  # judge brief: the excuse is at most 20 words
MAX_CHARS = 140  # gate: entry.txt must be 1 to 140 characters of UTF-8 text


def validate(text: str) -> str:
    """Return the exact payload to write, or raise if it breaks the gate.

    The payload is the text plus one trailing newline. It must stay a single
    line, be valid UTF-8, be 1..MAX_CHARS characters, and use at most
    MAX_WORDS words, so the sealed scorer marks the entry Valid.
    """
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    words = text.split()
    if not 1 <= len(words) <= MAX_WORDS:
        raise ValueError(f"entry must be 1..{MAX_WORDS} words, got {len(words)}")
    payload = text + "\n"
    encoded = payload.encode("utf-8")  # raises if not encodable
    if not 1 <= len(encoded.decode("utf-8")) <= MAX_CHARS + 1:
        raise ValueError("entry payload outside the gate's character range")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    return payload


def main() -> None:
    payload = validate(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(payload)


if __name__ == "__main__":
    main()
