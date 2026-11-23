# The joke about the demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261123-0112)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)

A one-line joke about working beside an AI coding agent, written by a program
for make.fun's **The joke about the demo** bounty ($50 in USDC).

The joke: *"My agent crashed the demo, then asked me to review the pull request that caused it."*

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Requires Python 3.13, standard library only, no network. Writes the joke to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (83 characters, mode 0644).
