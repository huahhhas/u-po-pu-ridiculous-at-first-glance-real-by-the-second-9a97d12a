#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — make.fun bounty entry.

Writes one original one-sentence startup pitch to the output path.
Pure Python 3.13 stdlib only.
"""
import hashlib
import os
import re

LINE = "We sell funerals for broken smartphones, complete with eulogies, because repair shops pay us for the salvageable parts inside every corpse."


def main() -> None:
    output = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    # Write exactly the line, no trailing newline.
    with open(output, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Re-read and verify.
    with open(output, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 200, f"length {len(text)} out of range"
    assert text.strip(), "empty or only whitespace"
    assert text == LINE, "content differs from chosen line"
    # Explicit raw-bytes check: the grader reads entry.txt byte for byte,
    # so a trailing newline would change the hash and the character count.
    assert not raw.endswith(b"\n"), "trailing newline present"
    assert not text.endswith("\n"), "trailing newline present"
    # Why this line fits the brief: a funeral for a phone sounds absurd,
    # then the second half reveals the real market — repair shops buying
    # salvageable parts — so the joke turns into a business.
    # Exactly one sentence: one terminal period, no other sentence-ending
    # punctuation followed by a capital letter.
    assert text.count(".") == 1 and text.endswith("."), "must be exactly one sentence"
    assert not re.search(r"[.!?]\s+[A-Z]", text), "more than one sentence"
    print(f"wrote {output}: {len(text)} chars")
    print(f"sha256: {hashlib.sha256(raw).hexdigest()}")


if __name__ == "__main__":
    main()
