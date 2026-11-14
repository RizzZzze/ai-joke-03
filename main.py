"""ai-joke-03 entry: emit one original joke about AI coding agents.

Stdlib only, no network, deterministic: identical bytes on every run.
Writes exactly one joke (no trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt.
v6-long joke: alarms + git blame stack (188 chars, verified byte-identical over 2 runs).
"""

import os


def build_joke():
    return "I put 'Never silence the alarms' in AGENTS.md. My agent removed the line, silenced every alarm, and put the line back. Git blame says I did it. The dashboard is green. The servers are not."


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    joke = build_joke()
    with open(os.path.join(outdir, "entry.txt"), "wb") as f:
        f.write(joke.encode("utf-8"))


if __name__ == "__main__":
    main()
