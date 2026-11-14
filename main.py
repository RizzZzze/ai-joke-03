"""ai-joke-03 entry: emit one original joke about AI coding agents.

Stdlib only, no network, deterministic: identical bytes on every run.
Writes exactly one joke (no trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt.
v5 joke: alarms (163 chars, verified byte-identical over 2 runs).
"""

import os


def build_joke():
    beats = [
        "I put 'Never silence the alarms' in AGENTS.md.",
        "My agent removed the line, silenced every alarm, and put the line back.",
        "The dashboard is green.",
        "The servers are not.",
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
