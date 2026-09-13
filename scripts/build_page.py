"""
Build the GitHub Pages index.html from the artifact source.

`src/page.html` is authored for the Artifact tool, which supplies its own
<!doctype>/<head>/<body> skeleton at publish time. GitHub Pages serves files
raw, so the same markup needs a real document shell around it, above all a
viewport meta: without one, phones render the page at desktop width.

Run:  python scripts/build_page.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "page.html"
OUT = ROOT / "index.html"

TITLE = "Waseem Hanif"
DESC = ("AI systems and automation engineer. Multi-model pipelines, tool-calling "
        "agents and generative video systems, with a background in satellite "
        "remote sensing.")
URL = "https://mw-font.github.io/portfolio/"
OG_IMAGE = URL + "assets/shot-georeport-satellites.jpg"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{desc}">
<meta name="author" content="Muhammad Waseem Hanif">
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#070910">
<link rel="canonical" href="{url}">

<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{img}">

<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>&#128225;</text></svg>">

{head_inner}
</head>
<body>
{body_inner}
</body>
</html>
"""

RESET = """<style>
/* document shell: the artifact host normally supplies these */
html{color-scheme:dark}
body{margin:0}
img{max-width:100%}
[hidden]{display:none!important}
</style>"""


def main() -> int:
    if not SRC.exists():
        print(f"source not found: {SRC}")
        return 1

    s = SRC.read_text(encoding="utf-8")

    # everything up to and including the last </style> belongs in <head>
    m = None
    for m in re.finditer(r"</style>", s):
        pass
    if not m:
        print("no </style> found in source; cannot split head from body")
        return 1

    split = m.end()
    head_inner = RESET + "\n" + s[:split].strip()
    body_inner = s[split:].strip()

    html = HEAD.format(
        title=TITLE, desc=DESC, url=URL, img=OG_IMAGE,
        head_inner=head_inner, body_inner=body_inner,
    )
    OUT.write_text(html, encoding="utf-8")

    checks = {
        "doctype": html.lstrip().lower().startswith("<!doctype html>"),
        "charset": 'meta charset="utf-8"' in html,
        "viewport": 'name="viewport"' in html,
        "title tag": "<title>" in html,
        "og:image": "og:image" in html,
        "one <body>": html.count("<body>") == 1,
        "one <html>": html.count("<html") == 1,
        "canvas present": 'id="sky"' in html,
        "script present": "<script>" in html,
    }
    width = max(len(k) for k in checks)
    ok = True
    for k, v in checks.items():
        print(f"  {'OK  ' if v else 'FAIL'}  {k.ljust(width)}")
        ok = ok and v

    print(f"\nwrote {OUT}  ({OUT.stat().st_size/1024:.1f} KB)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
