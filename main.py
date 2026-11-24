"""Make the AI Judge Laugh: Developer Excuses -- write one funny single-line
excuse a developer gives when code breaks in production to /output/entry.txt.

Stdlib only, no network, no randomness: the output is byte-identical on
every run. The line turns the worn "it worked on my machine" excuse inside
out: the code was never fine, production merely ran it faithfully -- exactly
as written at 2 a.m.
"""

import os

# The joke lands because it blames the 2 a.m. author, not production: the code did exactly what it was told.
LINE = (
    "My code didn't break in production \u2014 production just ran it "
    "exactly the way I wrote it at 2 a.m."
)


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.endswith(".") and "\n" not in LINE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back: the file on disk must be exactly the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
