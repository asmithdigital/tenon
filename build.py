#!/usr/bin/env python3
"""
Build script for the Orbit marketing site.
Generates static HTML files by composing a shared header/footer with
per-page content. Run this whenever page content changes; commit the
generated HTML (GitHub Pages serves plain files, no build step at deploy time).
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV_ITEMS = [
    ("Studio", "studio.html"),
    ("Services", "services.html"),
    ("Work", "work.html"),
    ("Process", "process.html"),
    ("Journal", "journal.html"),
    ("Contact", "contact.html"),
]

ORBIT_MARK_SVG = """<svg class="orbit-mark" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="17" cy="17" r="6.5" fill="#FF4FA3"/>
  <ellipse cx="17" cy="17" rx="16" ry="7" stroke="currentColor" stroke-width="2" transform="rotate(-24 17 17)"/>
  <circle cx="29.5" cy="10.5" r="3" fill="#FFC93C"/>
</svg>"""


def rel(depth):
    return "../" * depth


def head(title, description, depth, extra=""):
    r = rel(depth)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Orbit</title>
<meta name="description" content="{description}">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/main.css">
{extra}
</head>
"""


def header(depth, active):
    r = rel(depth)
    links = []
    for label, href in NAV_ITEMS:
        cur = ' class="current"' if href == active else ""
        links.append(f'<a href="{r}{href}"{cur}>{label}</a>')
    links_html = "\n        ".join(links)
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{r}index.html">
      {ORBIT_MARK_SVG}
      Orbit
    </a>
    <nav class="nav-links" id="nav-links">
        {links_html}
        <a class="nav-cta" href="{r}contact.html">Start a project</a>
    </nav>
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">
      <svg width="24" height="24" viewBox="0 0 22 22"><path d="M2 6h18M2 11h18M2 16h18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
  </div>
</header>
"""


def footer(depth):
    r = rel(depth)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{r}index.html" style="color:var(--paper)">
          {ORBIT_MARK_SVG}
          Orbit
        </a>
        <p style="margin-top:1rem;max-width:28ch;color:rgba(255,251,243,0.7);font-size:0.95rem;">
          A global creative, product &amp; experience delivery agency. Everything we make orbits one thing: your customer.
        </p>
      </div>
      <div>
        <h4>Studio</h4>
        <ul>
          <li><a href="{r}studio.html">About</a></li>
          <li><a href="{r}process.html">Process</a></li>
          <li><a href="{r}journal.html">Journal</a></li>
          <li><a href="{r}contact.html">Careers</a></li>
        </ul>
      </div>
      <div>
        <h4>Work</h4>
        <ul>
          <li><a href="{r}work.html">Case studies</a></li>
          <li><a href="{r}services.html">Services</a></li>
          <li><a href="{r}app/index.html">Client portal</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:hello@orbit.agency">hello@orbit.agency</a></li>
          <li><a href="{r}contact.html">Start a project</a></li>
          <li>Studios in New York, London &amp; Singapore — remote-first everywhere else</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year></span> Orbit Studio, Inc.</span>
      <span>Built on GitHub Pages</span>
    </div>
  </div>
</footer>
<script src="{r}assets/js/main.js"></script>
"""


def page(filename, title, description, depth, active, body, extra_head=""):
    html = head(title, description, depth, extra_head) + "<body>\n" + header(depth, active) + body + "\n" + footer(depth) + "</body>\n</html>\n"
    path = os.path.join(ROOT, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    print("wrote", filename)


if __name__ == "__main__":
    import content
    content.build(page)
