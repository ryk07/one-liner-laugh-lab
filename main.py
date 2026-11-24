#!/usr/bin/env python3
"""Entry for 'One-Liner Laugh Lab' (u-suroso-69-one-liner-laugh-lab-6ccf3aae).

Writes one short funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock. Stdlib only; no path depends on the
working directory. The output path can be overridden with an argument
or the ENTRY_OUTPUT environment variable, which only exists so the
entry can be verified locally without touching the shared /output.
"""

import os
import sys

LINE = (
    "In my defence, the sock resigned from foot duty and applied to be "
    "lunch \u2014 I only processed the paperwork."
)


def output_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
