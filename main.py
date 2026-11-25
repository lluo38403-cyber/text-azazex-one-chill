"""One Line, One Chill — make.fun entry.

Writes one line to /output/entry.txt: the single scariest sentence I
can write, under 200 characters. No monster, no blood, just the quiet
fact that someone else has been walking around your home in your own
footsteps, and the footprints are still warm.
"""

import os

ENTRY = (
    "I came home to find my own footprints in the dust, leading from "
    "my bedroom to the front door, and they were still warm, like "
    "whoever made them had only just left."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
