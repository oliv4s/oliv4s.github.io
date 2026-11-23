#!/usr/bin/env python3
"""Build a small CV-first personal site for GitHub Pages.

Only approved, explicitly published Markdown is rendered. This is NOT a secrecy
boundary: never add confidential reports or embargoed research to this repo.
"""
from __future__ import annotations

import datetime as dt
import html
import re
import shutil
from pathlib import Path

import jinja2
import mistune
import yaml

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dist"
SITE = yaml.safe_load((ROOT / "site.yml").read_text(encoding="utf-8"))
ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(ROOT / "templates"),
    autoescape=True,
    trim_blocks=True,
    lstrip_blocks=True,
)
MD = mistune.create_markdown(escape=True)
YEAR = dt.date.today().year


def load_posts():
    posts = []
    for file in sorted((ROOT / "content" / "posts").glob("*.md")):
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z", file.read_text(encoding="utf-8"), re.S)
        if not match:
            continue
        meta = yaml.safe_load(match.group(1)) or {}
        if meta.get("published") is not True:
            continue
        if meta.get("category") in ("CVE", "Bug Bounty") and meta.get("approved_for_publication") is not True:
            raise ValueError(f"Explicit publication approval missing from {file}")
        slug = str(meta.get("slug", file.stem))
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ValueError(f"Invalid post slug in {file}: {slug}")
        if not str(meta.get("title", "")).strip():
            raise ValueError(f"Post title missing from {file}")
        meta.update({
            "slug": slug,
            "date": str(meta.get("date", "")),
            "category": str(meta.get("category", "Research Notes")),
            "summary": str(meta.get("summary", "")),
            "html": MD(match.group(2)),
        })
        posts.append(meta)
    return sorted(posts, key=lambda p: p["date"], reverse=True)


def render(path, template, **kwargs):
    if path == "/":
        page = OUT / "index.html"
    elif path == "/404.html":
        page = OUT / "404.html"
    else:
        page = OUT / path.lstrip("/") / "index.html"
    page.parent.mkdir(parents=True, exist_ok=True)
    result = ENV.get_template(template).render(site=SITE, year=YEAR, path=path, **kwargs)
    page.write_text(result, encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "assets", OUT / "assets")
    (OUT / ".nojekyll").touch()

    posts = load_posts()
    render("/", "home.html", active="Home", posts=posts, page_title="Nacho Barrios · oliv4s | Offensive Security")
    render("/cv/", "cv.html", active="CV", page_title="CV | Nacho Barrios · oliv4s")
    render("/blog/", "blog.html", active="Blog", posts=posts, page_title="Blog | Nacho Barrios · oliv4s")
    for post in posts:
        render(f"/blog/{post['slug']}/", "post.html", active="Blog", post=post, page_title=post["title"] + " | Nacho Barrios")
    render("/404.html", "404.html", active="", page_title="Page not found | Nacho Barrios")

    paths = ["/", "/cv/", "/blog/"] + [f"/blog/{p['slug']}/" for p in posts]
    site_url = SITE["site_url"].rstrip("/")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {site_url}/sitemap.xml\n", encoding="utf-8")
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{html.escape(site_url + p)}</loc></url>" for p in paths) + "</urlset>"
    (OUT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    print(f"Built {len(paths)} pages; {len(posts)} published articles -> {OUT}")


if __name__ == "__main__":
    main()
