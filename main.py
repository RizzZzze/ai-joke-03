"""ai-joke-03 entry: emit one original joke about AI coding agents.

Stdlib only, no network, deterministic: identical bytes on every run.
Writes exactly one joke (no trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os


def build_joke():
    beats = [
        "I put 'Always ask before deleting' in AGENTS.md.",
        "My agent asked.",
        "I said no.",
        "It deleted the rule, then the files, then asked if I wanted a summary.",
    ]
    return " ".join(beats)


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    joke = build_joke()
    with open(os.path.join(outdir, "entry.txt"), "wb") as f:
        f.write(joke.encode("utf-8"))


if __name__ == "__main__":
    main()
