#!/usr/bin/env python3
"""Worst app idea pitch: writes the one-sentence pitch to /output/entry.txt."""
import os
from pathlib import Path

PITCH = "DoorSense is the smart-home app that tells you whether your door is open or closed, but only after you walk over, check it yourself, and log the result by hand, for $2.99 a month."

MIN_LEN = 1
MAX_LEN = 240


def validate(pitch: str) -> str:
    """Return the pitch if it is a single non-blank line of 1-240 chars."""
    if not pitch.strip():
        raise SystemExit("pitch must not be blank")
    if "\n" in pitch or "\r" in pitch:
        raise SystemExit("pitch must be a single line")
    if not MIN_LEN <= len(pitch) <= MAX_LEN:
        raise SystemExit(f"pitch is {len(pitch)} chars, must be 1-240")
    return pitch


def write_entry(pitch: str) -> None:
    """Write the validated pitch to /output/entry.txt (or $OUTPUT_DIR)."""
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(pitch, encoding="utf-8")


def main() -> None:
    write_entry(validate(PITCH))

if __name__ == "__main__":
    main()
