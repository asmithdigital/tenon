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
    dict(slug="raa-insurance", client="RAA Group · Motor Insurance", tag="Product design · UX research · Design sprint",
         title="Finding the real conversion blocker — and redirecting a product roadmap before six months of build",
         summary="A structured design sprint synthesised five years of research across the motor insurance quote and purchase experience, revealing that member identity matching — not payment options — was preventing completion. The finding redirected the roadmap before a single sprint of development had been committed to the wrong solution.",
         gradient="sunset", icon="route"),
    dict(slug="raa-travel", client="RAA Group · Travel", tag="Product design · Information architecture · Search UX",
         title="Redesigning a travel booking platform for members at every stage of the journey",
         summary="A multi-year UX engagement across the RAA Travel booking platform, from initial redesign through subsequent iterations — covering search and navigation, information architecture, multiple customer personas, and ongoing usability testing across both the customer-facing platform and the travel agent administration interface.",
         gradient="peach", icon="orbit"),
    dict(slug="raa-member-portal", client="RAA Group · Member Portal", tag="Product design · Self-service · Mobile",
         title="Building a self-service member portal that members actually use to resolve issues, not just view information",
         summary="A sustained design engagement across RAA's My Account member portal, progressively adding genuine self-service capability — policy management, renewals, payments, claims, and identity management — with each feature designed to let members resolve their need without calling the contact centre.",
         gradient="citrus", icon="chat"),
    dict(slug="raa-design-system", client="RAA Group · Design System", tag="Design systems · Accessibility · Design Ops",
         title="Building a design system from nothing — including accessibility as a first-class design constraint",
         summary="A multi-year contribution to the RAA design system from its foundation, covering component governance, documentation, adoption across design and engineering, and an embedded accessibility standards partnership with Vision Australia that put WCAG compliance into the system at the component level rather than as a separate audit.",
         gradient="sky", icon="anchor"),
    dict(slug="pali-footwear", client="PALI Footwear", tag="Web design · Ecommerce · Brand",
         title="An ecommerce presence for an independent footwear brand that needed to look like it belonged online",
         summary="Website design and development for an independent footwear retailer, covering product presentation, ecommerce UX, and a visual identity that could compete with larger brands in search and on social.",
         gradient="grape", icon="bolt"),
    dict(slug="bass-coast-podiatry", client="Bass Coast Podiatry", tag="Web design · Health services",
         title="A new website for a regional podiatry practice that needed to convert local search traffic into appointments",
         summary="Website design and build for a regional Victorian podiatry practice, with a focus on local search discoverability, clear service presentation, and an online booking pathway that reduced the number of steps between finding the practice and making an appointment.",
         gradient="citrus", icon="cross"),
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
    "raa-insurance": dict(
        problem="The product team had a strong hypothesis: conversion was dropping because the payment options at checkout were insufficient. A redesign of the payment step was scoped and ready to build. Before committing, the team ran a five-day design sprint to pressure-test the assumption.",
        approach="The sprint synthesised five years of prior research — usability studies, NPS verbatims, analytics drop-off data, and contact centre call logs — into a single structured picture of where members were actually abandoning the journey and why. The real blocker emerged within the first two days: members who already held RAA membership were hitting an identity matching failure that prevented them from completing a quote as a member rather than a new customer. Payment options were not the problem at all. A prototype testing the identity-first flow was built and tested with real members by day four. Results were unambiguous. The roadmap was rewritten before the sprint closed.",
        stats_html="""<div class="stat"><span class="num">0</span><span class="label">development spend committed to the wrong roadmap</span></div>
        <div class="stat"><span class="num">Live</span><span class="label">authenticated quote-to-buy flow shipped for motor insurance</span></div>
        <div class="stat"><span class="num">QoQ</span><span class="label">completion rates improving quarter on quarter since launch</span></div>""",
        quote="Five years of research sitting in separate documents, synthesised in a week. The sprint didn't tell us what to build — it told us what not to build, which turned out to be more valuable.",
        quote_by="Product Manager, RAA Motor Insurance",
    ),
    "raa-travel": dict(
        problem="The RAA Travel platform served customers at very different stages of the travel experience — someone searching for inspiration is in a completely different mindset from someone mid-booking or trying to resolve a post-trip issue. The existing platform design treated all of these customers the same way, with search and navigation built around an older information architecture that did not reflect how members actually thought about travel.",
        approach="Discovery began with in-person member interviews conducted in RAA stores and service centres across South Australia, alongside workshops with travel operations teams, product managers, engineering leads, and external agency partners. Multiple customer personas were developed across inspiration, search, booking, and post-trip contexts. The search experience was redesigned based on keyword analysis and search behaviour data, working within the technical constraints of the booking platform. Information architecture was rebuilt in collaboration with an external IA agency and the internal content team. Usability testing ran in-house across multiple rounds of the redesigned experience. The travel agent administration interface was also redesigned in parallel, with separate discovery and testing for that internal user base.",
        stats_html="""<div class="stat"><span class="num">4</span><span class="label">customer contexts mapped, from inspiration to post-trip</span></div>
        <div class="stat"><span class="num">2</span><span class="label">platforms redesigned: public website and travel booking platform</span></div>
        <div class="stat"><span class="num">In-store</span><span class="label">usability testing conducted across RAA stores in South Australia</span></div>""",
        quote="We needed a design team that could work across our external customers and our internal travel consultants simultaneously, without losing sight of either. That's exactly what happened.",
        quote_by="Travel Operations Lead, RAA Group",
    ),
    "raa-member-portal": dict(
        problem="The existing member portal was informational rather than functional. Members could see their policy but not renew it. They could view their membership but not update it. Every transactional need ended in a phone call. The contact centre was carrying volume that a well-designed self-service experience should have absorbed.",
        approach="Each feature was scoped, discovered, and tested individually rather than delivered as a single large release. User research with members established what they were trying to do and where existing digital journeys were failing them. Each capability was prototyped and tested with members before build, with multiple rounds of usability testing for higher-stakes interactions like payments and claims. The experience was extended to the RAA mobile app in parallel, with separate design work for the different interaction context and re-entry patterns of mobile users. Handoffs from self-service to the contact centre were designed explicitly, so the transition felt like a continuation rather than a failure.",
        stats_html="""<div class="stat"><span class="num">5</span><span class="label">self-service feature areas shipped: policy, renewals, payments, claims, identity</span></div>
        <div class="stat"><span class="num">Mobile</span><span class="label">self-service extended to the RAA app with mobile-specific flows</span></div>
        <div class="stat"><span class="num">Seamless</span><span class="label">handoff designed between self-service and the contact centre</span></div>""",
        quote="The goal was never to stop members from calling us. It was to make sure that when they called, they actually needed to.",
        quote_by="Digital Experience Manager, RAA Group",
    ),
    "raa-design-system": dict(
        problem="The RAA design system needed to be built, not inherited. Components, documentation, governance processes, and the relationship between the design system and engineering implementation were all established from scratch. Accessibility had historically been managed as a compliance review at the end of a project rather than a design constraint built in from the beginning.",
        approach="Component documentation, token architecture, and design system governance processes were established alongside the initial build, with adoption tracked across design and engineering squads. The Vision Australia accessibility partnership was initiated and managed as a standing engagement — regular workshops, WCAG audits built into the design and delivery process, and usability testing with assistive technology users as a standard part of discovery. Accessibility standards were embedded into design system components at the component level, so every team using the system inherited accessible defaults rather than having to apply them case by case.",
        stats_html="""<div class="stat"><span class="num">0→1</span><span class="label">design system built from foundation, with governance across design and engineering</span></div>
        <div class="stat"><span class="num">Ongoing</span><span class="label">accessibility partnership established with Vision Australia</span></div>
        <div class="stat"><span class="num">WCAG</span><span class="label">compliance embedded at the component level, not as a separate audit</span></div>""",
        quote="Accessibility built into a component means every team who uses that component gets accessibility for free. That's a completely different outcome from an audit.",
        quote_by="Senior UX Designer, RAA Group",
    ),
    "pali-footwear": dict(
        problem="PALI Footwear had a wholesale and in-store presence but no ecommerce site that felt credible next to the larger brands shoppers were used to buying from. Product pages were an afterthought bolted onto a generic template, and checkout had no visual connection to the brand at all.",
        approach="Design and development were handled end to end: a product-first template that gave every shoe its own detail page treatment, a simplified checkout, and a visual identity — colour, type, product photography direction — built to hold up on a phone screen and in a Google Shopping listing next to competitors many times the size.",
        stats_html="""<div class="stat"><span class="num">1</span><span class="label">single designer/developer engagement, brand through build</span></div>
        <div class="stat"><span class="num">Mobile-first</span><span class="label">templates built around how footwear actually gets shopped on a phone</span></div>
        <div class="stat"><span class="num">Launched</span><span class="label">full ecommerce rebuild, design through development</span></div>""",
        quote="We needed to look like we belonged online next to brands ten times our size. That's what we got.",
        quote_by="Founder, PALI Footwear",
    ),
    "bass-coast-podiatry": dict(
        problem="Bass Coast Podiatry had no real website — a single static page with a phone number, no service information, and nothing that would surface in a local search. Prospective patients had no way to tell what the practice treated or how to book before calling.",
        approach="The rebuild started with what people actually search for locally — \"podiatrist near me\", specific conditions, opening hours — and structured the site's pages and content around those terms. Service pages were written in plain language, not clinical copy, and a booking pathway was added that took a visitor from search result to a confirmed appointment request in as few steps as possible.",
        stats_html="""<div class="stat"><span class="num">Local SEO</span><span class="label">site structured around real local search terms, not guesswork</span></div>
        <div class="stat"><span class="num">Fewer steps</span><span class="label">booking pathway shortened from phone-only to a direct online request</span></div>
        <div class="stat"><span class="num">Full rebuild</span><span class="label">from a single static page to a full service-based site</span></div>""",
        quote="Patients started mentioning they found us on Google before we'd even finished the launch checklist.",
        quote_by="Practice Owner, Bass Coast Podiatry",
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
