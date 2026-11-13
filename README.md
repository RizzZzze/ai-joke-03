# ai-joke-03 entry

Entry for the make.fun competition `ai-joke-03` ("Make the AI judge laugh").

`main.py` (Python 3.13, stdlib only, no network) writes exactly one original
joke about AI coding agents to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output`). The output is deterministic: two runs produce byte-identical
files. The joke is 1–280 UTF-8 characters with no trailing newline.

Run locally:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
