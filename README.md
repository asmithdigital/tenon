# Orbit — global agency website + Orbit OS

A global, full-service creative / product / experience design agency site,
plus an internal "Orbit OS" app (pipeline, clients, projects, invoices,
email campaigns) that runs on mock data in the browser. Both are plain
static HTML/CSS/JS — no build step, no framework, no server required. It
deploys to GitHub Pages as-is.

## A note on imagery

This build has no access to stock-photo services (no network path to an
image CDN, and pulling copyrighted photography isn't something I'll do
regardless). Instead every "photo" on the site is a custom gradient-mesh
illustration panel (`illustrations.py` → `.photo-panel`), and the team
section uses simple rounded avatar illustrations — a deliberate illustrated
art direction rather than a placeholder gap. When you're ready to drop in
real photography:

1. Add your images to `assets/img/photos/`.
2. Replace the relevant `photo_panel(...)` call in `content.py` with a
   plain `<img src="assets/img/photos/yourfile.jpg" alt="...">` inside a
   `<div class="photo-panel">…</div>` — the CSS already handles both.
3. Re-run `python3 build.py`.

Good free, license-clear sources if you want real photography: Unsplash,
Pexels, and Pixabay all offer free-to-use images — just download and drop
them into `assets/img/photos/` yourself (this environment can't fetch them
for you).

## What's in here

```
index.html, studio.html, services.html, work.html, process.html,
journal.html, contact.html      — marketing site
work/*.html, journal/*.html     — case studies + journal posts
app/index.html                  — Orbit OS demo login (any email/password)
app/dashboard.html … settings.html  — the internal app
illustrations.py                — gradient-photo-panel + avatar SVG system
assets/css/main.css             — marketing site design system
assets/css/app.css              — Orbit OS shell (sidebar, tables, kanban…)
assets/js/main.js               — marketing site behaviour
assets/js/data.js               — mock "database" (localStorage) — OrbitDB
assets/js/app.js                — Orbit OS shell behaviour
build.py, content.py            — regenerates the marketing HTML
app_build.py, app_content.py    — regenerates the Orbit OS HTML
```

The `build.py` / `app_build.py` scripts are optional — the generated
`.html` files are already committed. Re-run them (`python3 build.py &&
python3 app_build.py`) whenever you edit copy in `content.py` /
`app_content.py`, so you don't have to hand-edit repeated nav/footer markup
across 20 files.

## Push it and turn on GitHub Pages (first time only)

```bash
git init
git add -A
git commit -m "Initial commit: Orbit agency site + Orbit OS"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

Then turn on Pages (one-time, in the browser):
1. On GitHub, open the repo → **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Branch: **main**, folder: **/ (root)** → **Save**.
4. Your site will be live in ~1 minute at
   `https://YOUR-USERNAME.github.io/YOUR-REPO/`.

## The Orbit OS app is a demo — here's how to make it real

`assets/js/data.js` seeds mock clients, deals, projects, invoices, and
campaigns into `localStorage`, and every `/app` page reads and writes
through the `OrbitDB` object. Nothing calls a server yet.

1. **Database** — stand up Supabase, Firebase, or your own API, then
   rewrite the methods inside `OrbitDB` (`get`, `set`, `login`, etc.) in
   `assets/js/data.js` to call it instead of `localStorage`. Every page
   already goes through this one object, so that's the only file that
   needs to change shape.
2. **Auth** — replace the demo form in `app/index.html` (currently accepts
   any email/password) with real authentication.
3. **Email marketing** — the Campaigns page (`app/campaigns.html`) saves
   drafts locally. Wire the "Save as draft" / send flow to an ESP API
   (Mailchimp, Customer.io, Postmark, Resend, etc.) to actually deliver
   mail.
4. **Lead capture** — the marketing site's contact form
   (`assets/js/main.js`, `data-contact-form`) currently opens a `mailto:`
   link. Point it at the same backend so new enquiries land straight in
   the Pipeline board instead of your inbox.

## Brand system quick reference

- Colours: paper `#FFFBF3`, ink `#17121F`, pink `#FF4FA3`, blue `#4C7DFF`,
  mint `#17C98D`, sun `#FFC93C`, grape `#8B5CF6` — all defined as CSS
  variables at the top of `assets/css/main.css`.
- Type: **Fredoka** (rounded, bold) for display/headings, **Plus Jakarta
  Sans** for body/UI, **Space Mono** for real data only (invoice IDs,
  numeric labels) — no serif anywhere.
- Motif: "orbit" — everything circles back to the client. Pill-shaped
  buttons and nav, big rounded corners, floating gradient blobs behind
  heroes, and the orbit mark (a dot circling a core) as the one recurring
  logo device.

## Local preview

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```
