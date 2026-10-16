#!/usr/bin/env python3
"""Render legal-src/*.md into <page>/index.html (privacy-policy, terms, support).

Needs the `markdown` package:  python3 -m pip install markdown
Run from anywhere:              python3 tools/build_legal.py
"""
import html
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://kadakchai.tappstudio.in"
PAGES = {
    "privacy-policy": "Privacy Policy",
    "terms": "Terms of Use",
    "support": "Support and Data Deletion",
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} | Kadak</title>
<meta name="description" content="{title} for Kadak: Idle Chai Empire by TappStudio.">
<meta name="robots" content="noindex">
<link rel="canonical" href="{site}/{slug}/">
<meta name="theme-color" content="#12343B">
<meta name="color-scheme" content="dark">
<link rel="icon" href="/assets/favicon-48.png" sizes="48x48">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/legal.css">
</head>
<body>
<header class="bar"><a href="/"><img src="/assets/icon-96.webp" alt="" width="36" height="36">Kadak</a></header>
<main class="doc">
{body}
</main>
</body>
</html>
"""


def render(slug: str, title: str) -> None:
    src = (ROOT / "legal-src" / f"{slug}.md").read_text(encoding="utf-8")
    md = markdown.Markdown(extensions=["tables", "nl2br", "toc", "sane_lists"])
    body = md.convert(src)
    # Tables scroll sideways on phones instead of widening the page.
    body = re.sub(r"<table>", '<div class="table"><table>', body)
    body = body.replace("</table>", "</table></div>")
    out = ROOT / slug / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(TEMPLATE.format(title=html.escape(title), site=SITE, slug=slug, body=body), encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    for slug, title in PAGES.items():
        render(slug, title)
