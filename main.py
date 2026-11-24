"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji, U+1F970 SMILING FACE WITH HEARTS, to
entry.txt in the output directory. No trailing newline, nothing else.
"""

import os

ENTRY = "\U0001F970"  # smiling face with hearts


def main() -> int:
    output_dir = (os.environ.get("MAKEFUN_OUTPUT_DIR") or "").strip() or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
