#!/usr/bin/env python3
"""Build script for the /app Orbit OS pages (client portal + internal ops)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(ROOT, "app")

ICONS = {
    "dashboard": '<svg viewBox="0 0 16 16" fill="none"><rect x="1" y="1" width="6" height="6" rx="1.5" stroke="currentColor" stroke-width="1.4"/><rect x="9" y="1" width="6" height="9" rx="1.5" stroke="currentColor" stroke-width="1.4"/><rect x="1" y="9" width="6" height="6" rx="1.5" stroke="currentColor" stroke-width="1.4"/></svg>',
    "pipeline": '<svg viewBox="0 0 16 16" fill="none"><path d="M1 3h14M1 8h10M1 13h6" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>',
    "clients": '<svg viewBox="0 0 16 16" fill="none"><circle cx="8" cy="5" r="3" stroke="currentColor" stroke-width="1.4"/><path d="M2 15c0-3.3 2.7-5 6-5s6 1.7 6 5" stroke="currentColor" stroke-width="1.4"/></svg>',
    "projects": '<svg viewBox="0 0 16 16" fill="none"><rect x="1.5" y="2" width="13" height="12" rx="2" stroke="currentColor" stroke-width="1.4"/><path d="M1.5 6h13" stroke="currentColor" stroke-width="1.4"/></svg>',
    "invoices": '<svg viewBox="0 0 16 16" fill="none"><rect x="2.5" y="1" width="11" height="14" rx="2" stroke="currentColor" stroke-width="1.4"/><path d="M5 5h6M5 8h6M5 11h4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>',
    "campaigns": '<svg viewBox="0 0 16 16" fill="none"><path d="M1 4l7 4 7-4" stroke="currentColor" stroke-width="1.4"/><rect x="1" y="3" width="14" height="10" rx="2" stroke="currentColor" stroke-width="1.4"/></svg>',
    "settings": '<svg viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="2.4" stroke="currentColor" stroke-width="1.4"/><path d="M8 1v2M8 13v2M1 8h2M13 8h2M3 3l1.4 1.4M11.6 11.6L13 13M13 3l-1.4 1.4M4.4 11.6L3 13" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>',
}

NAV = [
    ("dashboard", "Dashboard", "dashboard.html"),
    ("pipeline", "Pipeline", "pipeline.html"),
    ("clients", "Clients", "clients.html"),
    ("projects", "Projects", "projects.html"),
    ("invoices", "Invoices", "invoices.html"),
    ("campaigns", "Campaigns", "campaigns.html"),
    ("settings", "Settings", "settings.html"),
]

ORBIT_MARK_SVG = """<svg class="orbit-mark" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="17" cy="17" r="6.5" fill="#FF4FA3"/>
  <ellipse cx="17" cy="17" rx="16" ry="7" stroke="currentColor" stroke-width="2" transform="rotate(-24 17 17)"/>
  <circle cx="29.5" cy="10.5" r="3" fill="#FFC93C"/>
</svg>"""


def head(title, extra=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Orbit OS</title>
<link rel="icon" href="../assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/main.css">
<link rel="stylesheet" href="../assets/css/app.css">
{extra}
</head>
"""


def sidebar(active):
    items = "".join(
        f'<a href="{href}" class="{"current" if key == active else ""}">{ICONS[key]}{label}</a>'
        for key, label, href in NAV
    )
    return f"""<aside class="app-sidebar">
  <a class="brand" href="dashboard.html">{ORBIT_MARK_SVG} Orbit <span class="mono" style="font-size:0.7rem;opacity:0.6;">OS</span></a>
  <nav class="app-nav">{items}</nav>
  <div class="app-sidebar-foot">
    <div class="mono" data-session-user style="color:var(--paper);margin-bottom:0.5rem;"></div>
    <a href="#" data-logout>Sign out</a> &middot; <a href="../index.html">Marketing site</a>
  </div>
</aside>"""


def shell(active, title, page_title_html, body):
    return f"""<body>
<div class="app-shell">
  {sidebar(active)}
  <div class="app-main">
    <div class="app-mobile-bar">
      <button class="btn-icon" data-menu-toggle aria-label="Menu">
        <svg width="18" height="18" viewBox="0 0 18 18"><path d="M2 5h14M2 9h14M2 13h14" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
      </button>
      <a class="brand" href="dashboard.html" style="font-size:1.1rem;">{ORBIT_MARK_SVG} Orbit</a>
      <span></span>
    </div>
    <div class="app-topbar">
      <h1>{page_title_html}</h1>
      <span class="badge-demo">Demo data &middot; local only</span>
    </div>
    <div class="app-content">
      {body}
    </div>
  </div>
</div>
<script src="../assets/js/data.js"></script>
<script src="../assets/js/app.js"></script>
"""


def page(filename, title, page_title_html, active, body, extra_head="", extra_script=""):
    html = head(title, extra_head) + shell(active, title, page_title_html, body) + extra_script + "\n</body>\n</html>\n"
    path = os.path.join(APP, filename)
    with open(path, "w") as f:
        f.write(html)
    print("wrote app/" + filename)


LOGIN_HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sign in · Orbit OS</title>
<link rel="icon" href="../assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/main.css">
<link rel="stylesheet" href="../assets/css/app.css">
</head>
<body data-login-page>
<div class="login-wrap">
  <div class="login-side">
    <a class="brand" href="../index.html" style="color:var(--paper);font-size:1.6rem;">
      <svg class="orbit-mark" viewBox="0 0 34 34" fill="none"><circle cx="17" cy="17" r="6.5" fill="#FF4FA3"/><ellipse cx="17" cy="17" rx="16" ry="7" stroke="currentColor" stroke-width="2" transform="rotate(-24 17 17)"/><circle cx="29.5" cy="10.5" r="3" fill="#FFC93C"/></svg>
      Orbit
    </a>
    <h1 class="h1" style="font-size:var(--step-4);margin-top:2rem;">Orbit OS</h1>
    <p class="lede" style="color:rgba(255,251,243,0.75);margin-top:1rem;">
      Pipeline, clients, projects, invoicing, and campaigns — the operating
      system behind a global studio. This demo runs entirely in your browser.
    </p>
  </div>
  <div class="login-form-side">
    <div class="flow" style="max-width:380px;">
      <h2 class="h2">Sign in</h2>
      <p class="badge-demo">Demo mode — any email/password works</p>
      <form id="login-form" class="flow" style="margin-top:1rem;">
        <div class="field"><label for="email">Email</label><input id="email" type="email" placeholder="you@orbit.agency" required></div>
        <div class="field"><label for="password">Password</label><input id="password" type="password" placeholder="••••••••" required></div>
        <button class="btn btn-solid" type="submit" style="width:100%;justify-content:center;">Sign in</button>
      </form>
      <p style="font-size:0.9rem;color:var(--ink-soft);">No account system is wired up yet — connect Supabase, Firebase, or your
      own auth API here when you're ready to go beyond the demo.</p>
    </div>
  </div>
</div>
<script src="../assets/js/data.js"></script>
<script>
document.getElementById('login-form').addEventListener('submit', function(e){
  e.preventDefault();
  var email = document.getElementById('email').value || 'demo@orbit.agency';
  OrbitDB.login(email);
  window.location.href = 'dashboard.html';
});
</script>
</body>
</html>
"""


def build():
    os.makedirs(APP, exist_ok=True)
    with open(os.path.join(APP, "index.html"), "w") as f:
        f.write(LOGIN_HTML)
    print("wrote app/index.html")
    import app_content
    app_content.build(page)


if __name__ == "__main__":
    build()
