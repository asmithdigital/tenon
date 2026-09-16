# -*- coding: utf-8 -*-
"""Page bodies for the Orbit marketing site."""
from illustrations import blob_field, photo_panel, avatar

CLIENTS = ["ORRIS & CO", "BASELINE FINANCIAL", "HULL MARITIME", "COVEN COFFEE",
           "PARALLAX HEALTH", "MERIDIAN TRANSIT", "SLATE ATHLETIC", "FERROUS TOOLS"]


def ticker(items):
    spans = "".join(f"<span>{i}</span><span class='dot'>&#9679;</span>" for i in items)
    return f'<div class="ticker"><div class="ticker-track">{spans}</div></div>'


# ---------------------------------------------------------------- INDEX ---
def index_body():
    hero_blobs = blob_field([
        dict(cx="-8%", cy="-10%", size="420px", color="#FFE3F1", path_idx=0, opacity=0.9),
        dict(cx="70%", cy="55%", size="360px", color="#E4ECFF", path_idx=1, opacity=0.8),
        dict(cx="40%", cy="-15%", size="260px", color="#FFF3D6", path_idx=2, opacity=0.9),
    ])
    return f"""
<section class="wrap" style="padding-top:2rem;">
  {hero_blobs}
  <div class="joint" style="z-index:1;">
    <div class="a flow">
      <span class="pill-tag pink">Global · full-service · remote-first</span>
      <h1 class="h1">Everything orbits<br>your customer.</h1>
      <p class="lede">Orbit is a global creative, product, and experience
      design agency. Brand, product, platform, and the systems that run the
      business behind them — designed and delivered as one team, one
      timeline, one bright idea at a time.</p>
      <div class="row" style="gap:1rem;flex-wrap:wrap;">
        <a class="btn btn-solid" href="work.html">See the work</a>
        <a class="btn" href="contact.html">Start a project</a>
      </div>
    </div>
    <div class="b">
      {photo_panel("sunset", "orbit")}
    </div>
  </div>
</section>

{ticker(CLIENTS)}

<section class="wrap">
  <div class="split" style="margin-bottom:3rem;">
    <h2 class="h2">What we build</h2>
    <a class="btn" href="services.html">All services</a>
  </div>
  <div class="grid-3">
    <div class="case-card">
      <span class="tag">Brand &amp; identity</span>
      <h3>Naming, systems, and marks built for the whole world</h3>
      <p style="color:var(--ink-soft);font-size:0.98rem;">Verbal and visual identity built to work everywhere your brand shows up — in twelve languages and a thousand tabs.</p>
    </div>
    <div class="case-card">
      <span class="tag">Product &amp; experience design</span>
      <h3>Interfaces people actually enjoy using</h3>
      <p style="color:var(--ink-soft);font-size:0.98rem;">Research, IA, interaction, and the UI kit engineering can ship without guessing what you meant.</p>
    </div>
    <div class="case-card">
      <span class="tag">Web, platform &amp; CRM build</span>
      <h3>Marketing sites, portals, and the ops tools behind them</h3>
      <p style="color:var(--ink-soft);font-size:0.98rem;">Front end, content systems, and the operational tooling that runs the business day to day, globally.</p>
    </div>
  </div>
</section>

<section class="section-tint blue">
  <div class="wrap">
    <div class="grid-3">
      <div class="stat"><span class="num">312</span><span class="label">projects shipped across 34 countries</span></div>
      <div class="stat"><span class="num">96</span><span class="label">clients still working with us today</span></div>
      <div class="stat"><span class="num">4.9</span><span class="label">average client rating, last 3 years</span></div>
    </div>
  </div>
</section>

<section class="wrap">
  <div class="joint">
    <div class="a">
      <p class="quote-block">"Orbit didn't hand us a brand and disappear. They stayed
      long enough to see it survive its first bad quarter — and it did."</p>
      <p class="mono" style="margin-top:1.5rem;color:var(--ink-soft);">Priya Chandrasekaran, CEO, Baseline Financial</p>
    </div>
    <div class="b flow">
      <h2 class="h2">Case study</h2>
      <p class="lede">Baseline Financial's advisor portal cut onboarding time
      from eleven days to ninety minutes across 40 countries. We rebuilt the
      information architecture, not just the paint.</p>
      <a class="btn" href="work/baseline.html">Read the case study</a>
    </div>
  </div>
</section>

<section class="wrap center flow" style="max-width:680px;margin-inline:auto;">
  <h2 class="h2">Tell us what's not fitting together yet.</h2>
  <a class="btn btn-solid" href="contact.html" style="display:inline-flex;margin-top:1rem;">Start a project</a>
</section>
"""


# --------------------------------------------------------------- STUDIO ---
def studio_body():
    return f"""
<section class="wrap">
  <div class="joint">
    <div class="a flow">
      <span class="pill-tag blue">Studio</span>
      <h1 class="h1">A global studio that still feels like one small room.</h1>
      <p class="lede">Orbit started in 2015 with two people who couldn't
      agree on where design ends and engineering begins. Ten years and
      three studios later — New York, London, Singapore, plus a fully
      remote crew everywhere in between — that argument is still our
      operating system: every engagement pairs a design lead with a build
      lead from day one.</p>
    </div>
    <div class="b flow">
      <p>We're a team of 74 across 14 countries: strategists, brand and
      product designers, engineers, writers, and studio producers who keep
      it all on schedule no matter which time zone is asleep.</p>
      <p>We take on roughly forty projects a year — enough to stay busy
      building brands and platforms for organisations going global, not
      so many that a partner stops showing up to every review.</p>
    </div>
  </div>
</section>

<section class="section-tint mint">
  <div class="wrap">
    <h2 class="h2" style="margin-bottom:2.5rem;">How we work</h2>
    <div class="service-row">
      <div class="mono">01 / Fit</div>
      <div><h3 style="font-size:var(--step-1);">We turn down work that isn't a fit</h3>
      <p style="color:var(--ink-soft);">We're built for organisations rebuilding something
      load-bearing — a brand, a core product, an internal operating system — for a global
      audience, not a one-off local landing page.</p></div>
      <div></div>
    </div>
    <div class="service-row">
      <div class="mono">02 / Pairing</div>
      <div><h3 style="font-size:var(--step-1);">Design and engineering sit in the same reviews</h3>
      <p style="color:var(--ink-soft);">No design-then-throw-over-the-wall. Whoever builds it
      is in the room while it's being designed, from week one, in every time zone.</p></div>
      <div></div>
    </div>
    <div class="service-row">
      <div class="mono">03 / Ownership</div>
      <div><h3 style="font-size:var(--step-1);">You leave with the keys, not a dependency</h3>
      <p style="color:var(--ink-soft);">Design systems, source files, and documentation are
      handed over in full. We're glad to keep supporting the work, but nothing is held
      hostage to make that happen.</p></div>
      <div></div>
    </div>
  </div>
</section>

<section class="wrap">
  <h2 class="h2" style="margin-bottom:2.5rem;">Leadership</h2>
  <div class="grid-3">
    <div class="flow">
      {avatar("a")}
      <h3 style="font-size:var(--step-1);">Marisol Ferreira</h3>
      <p class="mono" style="color:var(--ink-soft);">Co-founder, Design — New York</p>
    </div>
    <div class="flow">
      {avatar("b")}
      <h3 style="font-size:var(--step-1);">Dean Okafor</h3>
      <p class="mono" style="color:var(--ink-soft);">Co-founder, Engineering — London</p>
    </div>
    <div class="flow">
      {avatar("c")}
      <h3 style="font-size:var(--step-1);">Harriet Voss</h3>
      <p class="mono" style="color:var(--ink-soft);">Managing Director — Singapore</p>
    </div>
  </div>
</section>

<section class="wrap center flow" style="max-width:680px;margin-inline:auto;">
  <h2 class="h2">Interested in joining?</h2>
  <p class="lede" style="margin-inline:auto;">We hire slowly and in public, from anywhere. Open roles are posted on the journal.</p>
  <a class="btn" href="contact.html" style="display:inline-flex;margin-top:0.5rem;">Get in touch</a>
</section>
"""


# ------------------------------------------------------------- SERVICES ---
def services_body():
    rows = [
        ("Brand &amp; identity", "Positioning, naming, verbal identity, visual identity systems, global rebrands.", "2–8 weeks"),
        ("Product &amp; UX design", "Research, information architecture, interaction design, design systems, usability testing.", "4–16 weeks"),
        ("Web design &amp; build", "Marketing sites, campaign microsites, CMS builds, performance and accessibility audits.", "3–10 weeks"),
        ("Experience design", "Service blueprints, journey mapping, in-product onboarding, physical/digital retail experience.", "4–12 weeks"),
        ("Platform &amp; CRM build", "Client portals, internal tools, CRM and pipeline systems, integrations with email/marketing stacks.", "6–20 weeks"),
        ("Design &amp; front-end retainers", "Ongoing design and build capacity for teams who need a studio, not a freelancer roster.", "Monthly"),
    ]
    rows_html = "".join(f"""
    <div class="service-row">
      <h3 style="font-size:var(--step-1);">{name}</h3>
      <p style="color:var(--ink-soft);">{desc}</p>
      <div class="mono">{dur}</div>
    </div>""" for name, desc, dur in rows)

    return f"""
<section class="wrap">
  <div class="joint">
    <div class="a flow">
      <span class="pill-tag sun">Services</span>
      <h1 class="h1">Services</h1>
      <p class="lede">Engagements are scoped around a problem, not a
      department. Most projects combine two or three of the below into one
      timeline with one global team.</p>
    </div>
    <div class="b">
      {photo_panel("citrus", "bolt")}
    </div>
  </div>
</section>

<section class="wrap">
  {rows_html}
</section>

<section class="section-tint pink">
  <div class="wrap">
    <div class="joint">
      <div class="a flow">
        <h2 class="h2">How pricing works</h2>
        <p class="lede">Fixed-fee for defined deliverables, retainer for
        ongoing capacity. We don't bill hourly — it rewards slowness, and
        we'd rather be measured on outcomes.</p>
      </div>
      <div class="b flow">
        <p class="quote-block" style="font-size:var(--step-1);">"Ask for a
        number in the first call. If we can't give you a range, that's
        useful information about us."</p>
      </div>
    </div>
  </div>
</section>

<section class="wrap center flow" style="max-width:680px;margin-inline:auto;">
  <h2 class="h2">Not sure which service you need?</h2>
  <a class="btn btn-solid" href="contact.html" style="display:inline-flex;margin-top:0.5rem;">Book a discovery call</a>
</section>
"""


# ------------------------------------------------------------------ WORK ---
CASES = [
    dict(slug="baseline", client="Baseline Financial", tag="Product & UX design · Platform build",
         title="Cutting advisor onboarding from eleven days to ninety minutes",
         summary="A ground-up redesign of the advisor portal's information architecture, replacing a document-upload maze with a guided, stateful workflow — live in 40 countries.",
         gradient="sky", icon="chart"),
    dict(slug="parallax", client="Parallax Health", tag="Brand & identity · Experience design",
         title="A clinical brand that patients trust and clinicians respect",
         summary="Full rebrand and patient-experience redesign across 60 clinics on three continents, unifying signage, scheduling, and the patient portal under one identity.",
         gradient="meadow", icon="cross"),
    dict(slug="hull", client="Hull Maritime", tag="Web design & build · CRM build",
         title="Replacing forty spreadsheets with one fleet operations system",
         summary="A custom operations platform for scheduling, maintenance, and client billing across a 140-vessel global charter fleet.",
         gradient="grape", icon="anchor"),
]


def work_body():
    cards = "".join(f"""
    <a class="case-card" href="work/{c['slug']}.html" style="text-decoration:none;">
      {photo_panel(c['gradient'], c['icon'])}
      <span class="tag">{c['tag']}</span>
      <h3>{c['title']}</h3>
      <p style="color:var(--ink-soft);font-size:0.95rem;">{c['summary']}</p>
      <span class="mono" style="margin-top:auto;">{c['client']}</span>
    </a>""" for c in CASES)
    return f"""
<section class="wrap">
  <div class="joint">
    <div class="a flow">
      <span class="pill-tag mint">Work</span>
      <h1 class="h1">Work</h1>
      <p class="lede">A small selection from 312 projects across 34
      countries — ask in the first call if you want references in your
      industry or region.</p>
    </div>
    <div class="b"></div>
  </div>
</section>
<section class="wrap">
  <div class="grid-3">
    {cards}
  </div>
</section>
<section class="wrap center flow" style="max-width:680px;margin-inline:auto;">
  <h2 class="h2">See yours here next.</h2>
  <a class="btn btn-solid" href="contact.html" style="display:inline-flex;margin-top:0.5rem;">Start a project</a>
</section>
"""


def case_body(c, prev_slug, next_slug):
    return f"""
<section class="wrap">
  <div class="flow" style="max-width:70ch;">
    <span class="pill-tag pink">{c['tag']}</span>
    <h1 class="h1" style="font-size:var(--step-4);">{c['title']}</h1>
    <p class="lede" style="max-width:60ch;">{c['summary']}</p>
  </div>
</section>
<section class="wrap">
  {photo_panel(c['gradient'], c['icon'], extra_style="aspect-ratio:16/7;")}
</section>
<section class="wrap">
  <div class="joint">
    <div class="a flow">
      <h2 class="h2">The problem</h2>
      <p>{c['problem']}</p>
    </div>
    <div class="b flow">
      <h2 class="h2">The approach</h2>
      <p>{c['approach']}</p>
    </div>
  </div>
</section>
<section class="section-tint sun">
  <div class="wrap">
    <div class="grid-3">
      {c['stats_html']}
    </div>
  </div>
</section>
<section class="wrap">
  <p class="quote-block">"{c['quote']}"</p>
  <p class="mono" style="margin-top:1.5rem;color:var(--ink-soft);">{c['quote_by']}</p>
</section>
<section class="wrap">
  <div class="split">
    <a class="btn" href="{prev_slug}.html">&larr; Previous case study</a>
    <a class="btn" href="{next_slug}.html">Next case study &rarr;</a>
  </div>
</section>
"""


CASE_DETAIL = {
    "baseline": dict(
        problem="Financial advisors onboarding new clients across 40 countries had to gather signatures across eleven separate PDFs, none of which talked to each other or to the compliance backend. The average onboarding took eleven days and a support call.",
        approach="We mapped every regional compliance dependency into a single decision tree, then rebuilt the portal as one stateful wizard with save-and-resume, real-time validation, and automatic routing to the right compliance path. Engineering was in the room from the first workshop.",
        stats_html="""<div class="stat"><span class="num">90m</span><span class="label">average onboarding time, down from 11 days</span></div>
        <div class="stat"><span class="num">73%</span><span class="label">drop in support tickets related to onboarding</span></div>
        <div class="stat"><span class="num">6</span><span class="label">weeks from kickoff to first release</span></div>""",
        quote="Orbit didn't hand us a brand and disappear. They stayed long enough to see it survive its first bad quarter — and it did.",
        quote_by="Priya Chandrasekaran, CEO, Baseline Financial",
    ),
    "parallax": dict(
        problem="Parallax Health's 60 clinics across three continents had each accumulated their own signage, forms, and booking flow over a decade of independent growth. Patients experienced sixty different companies, not one.",
        approach="We built a single clinical identity system — typography and colour chosen for legibility under clinic lighting, not aesthetics alone — and rolled it out across signage, print, and a shared patient portal, region by region, over eight months.",
        stats_html="""<div class="stat"><span class="num">60</span><span class="label">clinics unified under one identity</span></div>
        <div class="stat"><span class="num">31%</span><span class="label">increase in online booking completion</span></div>
        <div class="stat"><span class="num">8mo</span><span class="label">phased rollout with zero clinic downtime</span></div>""",
        quote="Patients started recognising us across continents for the first time. That was the whole point, and it worked faster than we expected.",
        quote_by="Dr. Innes Whitfield, Clinical Director, Parallax Health",
    ),
    "hull": dict(
        problem="Hull Maritime ran a 140-vessel global charter fleet on forty-plus spreadsheets — scheduling, maintenance logs, and client invoicing lived in separate files that never reconciled cleanly across offices.",
        approach="We designed and built a single operations platform: a scheduling calendar, a maintenance log with automatic service alerts, and billing tied directly to charter records, translated for every regional office. The team trained on it in one afternoon.",
        stats_html="""<div class="stat"><span class="num">40+</span><span class="label">spreadsheets replaced by one system</span></div>
        <div class="stat"><span class="num">140</span><span class="label">vessels scheduled from a single calendar</span></div>
        <div class="stat"><span class="num">4hrs</span><span class="label">saved per week, per fleet manager</span></div>""",
        quote="We didn't think a studio this size could build something this specific to us. They spent two weeks on our docks in three countries before writing a line of code.",
        quote_by="Callum Reyes, Global Operations Director, Hull Maritime",
    ),
}


# --------------------------------------------------------------- PROCESS ---
def process_body():
    steps = [
        ("Discovery", "2 weeks", "Stakeholder interviews, audit of what exists, and a written problem statement both sides sign off on before scope is set."),
        ("Definition", "1–2 weeks", "Information architecture, content strategy, and a fixed-fee proposal for the build phase — no open-ended estimates."),
        ("Design", "3–8 weeks", "Concepting through to high-fidelity, reviewed jointly with the engineering lead so nothing gets designed that can't be built on schedule."),
        ("Build", "3–12 weeks", "Front-end and platform work in parallel with content production, in two-week cycles with a working preview at the end of each."),
        ("Launch", "1 week", "Staged global rollout, monitoring, and a handover package: source files, documentation, and a recorded walkthrough for your team."),
        ("Support", "Ongoing", "Optional retainer for iteration, new features, or design capacity — month to month, no lock-in contract."),
    ]
    rows = "".join(f"""
    <div class="service-row">
      <div class="mono">{i+1:02d}</div>
      <div><h3 style="font-size:var(--step-1);">{name}</h3><p style="color:var(--ink-soft);">{desc}</p></div>
      <div class="mono">{dur}</div>
    </div>""" for i, (name, dur, desc) in enumerate(steps))
    return f"""
<section class="wrap">
  <div class="joint">
    <div class="a flow">
      <span class="pill-tag blue">Process</span>
      <h1 class="h1">Process</h1>
      <p class="lede">This is genuinely a sequence, so we number it. Every
      project runs through all six stages — the only variable is how long
      design and build take for your scope, and how many time zones are involved.</p>
    </div>
    <div class="b"></div>
  </div>
</section>
<section class="wrap">{rows}</section>
<section class="section-tint blue">
  <div class="wrap">
    <div class="joint">
      <div class="a flow">
        <h2 class="h2">What you'll be asked for</h2>
        <p>Access to the people who'll use what we're building — not just the
        people who commissioned it. A single decision-maker who can sign off
        each stage within a week. And existing material: brand guidelines,
        analytics, support tickets, anything that shows how things actually
        work today.</p>
      </div>
      <div class="b flow">
        <h2 class="h2">What you'll get from us</h2>
        <p>A named design lead and build lead for the life of the project, a
        shared project log, working previews at the end of every two-week
        cycle, and full source-file ownership at handover.</p>
      </div>
    </div>
  </div>
</section>
<section class="wrap center flow" style="max-width:680px;margin-inline:auto;">
  <h2 class="h2">Ready for stage one?</h2>
  <a class="btn btn-solid" href="contact.html" style="display:inline-flex;margin-top:0.5rem;">Book a discovery call</a>
</section>
"""


# --------------------------------------------------------------- JOURNAL ---
POSTS = [
    dict(slug="onboarding-is-architecture", date="14 Aug 2026", tag="Product",
         title="Onboarding is an architecture problem, not a UI problem",
         summary="Why most onboarding redesigns fail: they polish the form instead of redrawing the decision tree underneath it.",
         gradient="sky", icon="chart"),
    dict(slug="rebrand-without-relaunch", date="02 Jun 2026", tag="Brand",
         title="How to rebrand sixty locations without a single relaunch day",
         summary="A phased rollout framework for organisations that can't afford downtime, drawn from the Parallax Health rebrand.",
         gradient="meadow", icon="cross"),
    dict(slug="pricing-fixed-fee", date="19 Mar 2026", tag="Studio",
         title="Why we stopped billing by the hour",
         summary="Hourly billing rewards slowness and punishes expertise. Here's what we do instead, and what it costs us.",
         gradient="citrus", icon="bolt"),
]


def journal_body():
    cards = "".join(f"""
    <a class="case-card" href="journal/{p['slug']}.html" style="text-decoration:none;">
      {photo_panel(p['gradient'], p['icon'])}
      <span class="tag mono">{p['tag']} · {p['date']}</span>
      <h3>{p['title']}</h3>
      <p style="color:var(--ink-soft);font-size:0.95rem;">{p['summary']}</p>
    </a>""" for p in POSTS)
    return f"""
<section class="wrap">
  <div class="joint">
    <div class="a flow">
      <span class="pill-tag sun">Journal</span>
      <h1 class="h1">Journal</h1>
      <p class="lede">Notes on the work, written by whoever led it. No
      ghost-written thought leadership — if a partner didn't do the work,
      they don't write the post.</p>
    </div>
    <div class="b"></div>
  </div>
</section>
<section class="wrap"><div class="grid-3">{cards}</div></section>
"""


POST_BODIES = {
    "onboarding-is-architecture": """
<p>Most onboarding redesigns start with the form. Someone screenshots the
current sign-up flow, marks it up in red, and a designer makes it look
calmer. The conversion rate moves a point or two. Nobody touches the
decision tree underneath, so the underlying complexity is still there —
it's just wearing a nicer shirt.</p>
<p>When we started on Baseline Financial's advisor portal, the brief was
"make onboarding less painful" across 40 countries. The actual problem was
that eleven separate compliance paths had been implemented as eleven
separate PDF forms, with no shared logic between them. A UI redesign
couldn't fix that; it needed an information architecture project wearing a
UI redesign's clothes.</p>
<p>We spent the first two weeks not in Figma but in a whiteboard room,
mapping every compliance branch as a decision tree with the compliance team
in the room. Only once that tree existed as a single source of truth did we
start on interface work — and at that point the interface mostly designed
itself, because the hard problem was already solved.</p>
<p>The lesson we keep re-learning: if an onboarding flow feels painful, the
pain is very rarely in the pixels. Look at the tree before you touch the
leaves.</p>
""",
    "rebrand-without-relaunch": """
<p>A rebrand across sixty locations on three continents has an obvious
failure mode: pick a relaunch date, replace everything overnight, and pray
nothing breaks in production while patients are in the waiting room. We
didn't want that risk profile for Parallax Health, so we didn't build
toward a single launch day at all.</p>
<p>Instead we sequenced the rollout by what could change independently.
Digital assets — the portal, email templates, the booking confirmation —
went first, over two weeks, because they could be swapped without anyone
walking into a physical space. Print collateral went next, region by
region, timed to each location's existing reorder cycle so nothing was
thrown away early. Signage went last, because it's the most expensive to
get wrong and the easiest to schedule around a quiet week.</p>
<p>Eight months end to end, with zero days where any clinic was "half
rebranded" in a way patients would notice inside a single visit. Slower
than a big-bang relaunch, but nobody had to explain to a patient why the
sign didn't match the invoice.</p>
""",
    "pricing-fixed-fee": """
<p>We billed hourly for our first two years. It's the easiest model to
explain to a new client and the hardest one to defend once you're good at
your job. Hourly billing has a structural flaw: the better and faster your
team gets, the less you can charge for the same outcome. It rewards
slowness and punishes expertise.</p>
<p>We moved to fixed-fee scoping in 2017. Every engagement starts with a
paid two-week discovery sprint — itself fixed-fee — that produces enough
clarity to quote the full project as a number, not a range. That number
doesn't move unless the scope does, and if the scope changes mid-project we
re-quote the delta before starting it, in writing, same day.</p>
<p>It costs us on the projects that run over — we eat that, not the client.
But it means every planning conversation is about the work, not the clock,
and that trade has been worth it every year since, across every studio.</p>
""",
}


def build(page):
    page("index.html", "Global creative & experience design agency", "Orbit is a global creative, product, and experience design agency.", 0, "", index_body())
    page("studio.html", "Studio", "Who we are and how Orbit works.", 0, "studio.html", studio_body())
    page("services.html", "Services", "Brand, product, web, experience design, and platform build services.", 0, "services.html", services_body())
    page("work.html", "Work", "Selected case studies from the Orbit studio.", 0, "work.html", work_body())
    page("process.html", "Process", "How an Orbit engagement runs from discovery to launch.", 0, "process.html", process_body())
    page("journal.html", "Journal", "Notes on the work, written by the people who did it.", 0, "journal.html", journal_body())

    slugs = [c["slug"] for c in CASES]
    for i, c in enumerate(CASES):
        merged = {**c, **CASE_DETAIL[c["slug"]]}
        prev_s = slugs[(i - 1) % len(slugs)]
        next_s = slugs[(i + 1) % len(slugs)]
        page(f"work/{c['slug']}.html", merged["title"], merged["summary"], 1, "work.html", case_body(merged, prev_s, next_s))

    for p in POSTS:
        body = f"""
<section class="wrap">
  <div class="flow" style="max-width:64ch;">
    <span class="pill-tag pink">{p['tag']} · {p['date']}</span>
    <h1 class="h1" style="font-size:var(--step-4);">{p['title']}</h1>
  </div>
</section>
<section class="wrap">
  {photo_panel(p['gradient'], p['icon'], extra_style="aspect-ratio:16/7;max-width:64ch;")}
</section>
<section class="wrap">
  <div class="flow" style="max-width:64ch;">
    {POST_BODIES[p['slug']]}
  </div>
</section>
"""
        page(f"journal/{p['slug']}.html", p["title"], p["summary"], 1, "journal.html", body)

    contact_body = f"""
<section class="wrap">
  <div class="joint">
    <div class="a flow">
      <span class="pill-tag mint">Contact</span>
      <h1 class="h1">Start a project</h1>
      <p class="lede">Tell us what's not fitting together yet. We reply to
      every enquiry within two business days, and every first call is with
      a partner, not an account manager.</p>
      <div class="flow" style="margin-top:2rem;">
        <p>📩 hello@orbit.agency</p>
        <p>🌍 Studios in New York, London &amp; Singapore — remote-first everywhere else</p>
      </div>
    </div>
    <div class="b">
      <form data-contact-form>
        <div class="field"><label for="name">Name</label><input id="name" name="name" required></div>
        <div class="field"><label for="email">Email</label><input id="email" type="email" name="email" required></div>
        <div class="field"><label for="budget">Approximate budget</label>
          <select id="budget" name="budget">
            <option>Under $20,000</option>
            <option>$20,000 – $75,000</option>
            <option>$75,000 – $200,000</option>
            <option>$200,000+</option>
          </select>
        </div>
        <div class="field"><label for="message">What are you trying to fix?</label><textarea id="message" name="message" required></textarea></div>
        <button class="btn btn-solid" type="submit">Send enquiry</button>
        <p data-form-status class="mono" style="margin-top:1rem;color:var(--ink-soft);"></p>
      </form>
    </div>
  </div>
</section>
"""
    page("contact.html", "Contact", "Start a project with Orbit.", 0, "contact.html", contact_body)
