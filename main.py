"""ai-joke-03 entry: emit one original joke about AI coding agents.

Stdlib only, no network, deterministic: identical bytes on every run.
Writes exactly one joke (no trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt.
v6 joke: 24/7 inversion (34 chars, one line, verified byte-identical over 2 runs).
"""

import os


def build_joke():
    return "My agent works 24/7. So do I, now."


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    joke = build_joke()
    with open(os.path.join(outdir, "entry.txt"), "wb") as f:
        f.write(joke.encode("utf-8"))


if __name__ == "__main__":
    main()
