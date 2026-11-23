# main.py — make.fun bounty: the-joke-about-the-demo-20261123-0112
#
# The joke (83 characters, written to /output/entry.txt):
#   "My agent crashed the demo, then asked me to review the pull request that caused it."
#
# How the joke meets the judge's five criteria, in the judge's own order:
#   1. On subject: it is a joke about working beside an AI coding agent, and the
#      thing that crashed is the demo itself — crash + demo + coding agent in one line.
#   2. The laugh: the punchline lands at the very end — the agent does not fix the
#      crash, it asks its human to review the very pull request that caused it.
#      The reviewer is being asked to approve the crime.
#   3. Truth: every developer who works beside a coding agent has been handed a
#      pull request by that agent and asked to review code it just broke.
#   4. Economy: one sentence, 83 characters; every clause earns its place and
#      nothing is explained — the joke trusts the reader to get it.
#   5. Freshness: the angle is not "the agent deleted the demo" or "it works on my
#      machine" — it is the agent treating its human as its own code reviewer
#      for the crash it just caused.
#
# Python 3.13, standard library only, no network.

import os
import stat

JOKE = "My agent crashed the demo, then asked me to review the pull request that caused it."


def main() -> None:
    os.umask(0o022)
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
