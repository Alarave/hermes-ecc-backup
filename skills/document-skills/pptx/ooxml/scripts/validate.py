#!/usr/bin/env python3
"""Dispatcher to sibling docx OOXML validate module."""

import runpy
import sys
from pathlib import Path


def main() -> None:
    shared_script = (
        Path(__file__).resolve().parents[3] / "docx" / "ooxml" / "scripts" / "validate.py"
    )
    sys.path.insert(0, str(shared_script.parent))
    runpy.run_path(str(shared_script), run_name="__main__")


if __name__ == "__main__":
    main()
