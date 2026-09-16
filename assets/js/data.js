/* Orbit OS — mock data layer.
   Everything here lives in localStorage so the demo is fully interactive
   with no backend. When you connect a real database, replace the
   OrbitDB.* methods below with API calls — every page consumes only
   this object, so that's the one file to rewire. */

const OrbitDB = (() => {
  const NS = "orbit-os:";

  const SEED = {
    clients: [
      { id: "c1", name: "Baseline Financial", contact: "Priya Chandrasekaran", email: "priya@baselinefinancial.com", stage: "Active", value: 148000, since: "2023-02-11", notes: "Advisor portal redesign + ongoing retainer." },
      { id: "c2", name: "Parallax Health", contact: "Dr. Innes Whitfield", email: "innes@parallaxhealth.org", stage: "Active", value: 96000, since: "2024-05-03", notes: "9-clinic rebrand, phase 2 (patient app) in scoping." },
      { id: "c3", name: "Hull Maritime", contact: "Callum Reyes", email: "callum@hullmaritime.com", stage: "Active", value: 210000, since: "2022-11-20", notes: "Fleet ops platform, quarterly feature retainer." },
      { id: "c4", name: "Coven Coffee", contact: "Ada Solberg", email: "ada@covencoffee.co", stage: "Past", value: 32000, since: "2021-09-01", notes: "Brand + web, project complete." },
      { id: "c5", name: "Meridian Transit", contact: "Foster Aldana", email: "faldana@meridiantransit.gov", stage: "Prospect", value: 0, since: "2026-08-14", notes: "RFP submitted, decision expected October." },
      { id: "c6", name: "Slate Athletic", contact: "Nadia Kessler", email: "nadia@slateathletic.com", stage: "Prospect", value: 0, since: "2026-08-28", notes: "Discovery call booked for next week." },
      { id: "c7", name: "Ferrous Tools", contact: "Marcus Hale", email: "marcus@ferroustools.com", stage: "Active", value: 54000, since: "2025-01-15", notes: "E-commerce rebuild, launching Q4." },
      { id: "c8", name: "Orris & Co", contact: "Beatrix Lund", email: "beatrix@orrisandco.com", stage: "Past", value: 41000, since: "2020-06-01", notes: "Identity system, project complete." },
    ],
    deals: [
      { id: "d1", name: "Meridian Transit — rider app RFP", clientId: "c5", value: 180000, stage: "lead", owner: "Marisol" },
      { id: "d2", name: "Slate Athletic — DTC rebuild", clientId: "c6", value: 65000, stage: "lead", owner: "Dean" },
      { id: "d3", name: "Ferrous Tools — loyalty module", clientId: "c7", value: 22000, stage: "qualified", owner: "Harriet" },
      { id: "d4", name: "Coven Coffee — franchise kit v2", clientId: "c4", value: 18000, stage: "qualified", owner: "Marisol" },
      { id: "d5", name: "Parallax Health — patient app phase 2", clientId: "c2", value: 88000, stage: "proposal", owner: "Dean" },
      { id: "d6", name: "Hull Maritime — crew scheduling module", clientId: "c3", value: 34000, stage: "proposal", owner: "Harriet" },
      { id: "d7", name: "Baseline Financial — compliance dashboard", clientId: "c1", value: 56000, stage: "negotiation", owner: "Marisol" },
      { id: "d8", name: "Orris & Co — 2027 refresh", clientId: "c8", value: 24000, stage: "won", owner: "Dean" },
    ],
    projects: [
      { id: "p1", name: "Advisor Portal v3", clientId: "c1", lead: "Dean Okafor", progress: 82, status: "Active", due: "2026-10-30" },
      { id: "p2", name: "Patient Portal Refresh", clientId: "c2", lead: "Marisol Ferreira", progress: 45, status: "Active", due: "2026-11-20" },
      { id: "p3", name: "Fleet Ops Platform — Phase 3", clientId: "c3", lead: "Dean Okafor", progress: 60, status: "Active", due: "2026-12-05" },
      { id: "p4", name: "Ferrous Tools E-commerce Rebuild", clientId: "c7", lead: "Harriet Voss", progress: 91, status: "Active", due: "2026-10-01" },
      { id: "p5", name: "Coven Coffee Franchise Kit", clientId: "c4", lead: "Marisol Ferreira", progress: 100, status: "Complete", due: "2025-03-01" },
    ],
    invoices: [
      { id: "INV-1042", clientId: "c1", amount: 24000, status: "sent", issued: "2026-09-01", due: "2026-09-30" },
      { id: "INV-1041", clientId: "c3", amount: 42000, status: "active", issued: "2026-08-15", due: "2026-09-14" },
      { id: "INV-1040", clientId: "c7", amount: 18000, status: "overdue", issued: "2026-08-01", due: "2026-08-31" },
      { id: "INV-1039", clientId: "c2", amount: 31000, status: "active", issued: "2026-08-20", due: "2026-09-19" },
      { id: "INV-1038", clientId: "c1", amount: 24000, status: "active", issued: "2026-07-01", due: "2026-07-31" },
      { id: "INV-1037", clientId: "c4", amount: 9000, status: "draft", issued: "2026-09-10", due: "2026-10-10" },
    ],
    campaigns: [
      { id: "cm1", name: "Q3 Journal digest", audience: "All subscribers (1,204)", status: "sent", sent: "2026-09-02", openRate: 48, clickRate: 11 },
      { id: "cm2", name: "Parallax rebrand case study", audience: "Healthcare segment (312)", status: "sent", sent: "2026-08-18", openRate: 61, clickRate: 22 },
      { id: "cm3", name: "New capacity — Q4 availability", audience: "Prospects (89)", status: "scheduled", sent: "2026-09-22", openRate: null, clickRate: null },
      { id: "cm4", name: "Studio hiring announcement", audience: "All subscribers (1,204)", status: "draft", sent: null, openRate: null, clickRate: null },
    ],
    activity: [
      { id: "a1", ts: "2026-09-15T14:20:00", text: "Invoice INV-1042 sent to Baseline Financial" },
      { id: "a2", ts: "2026-09-15T10:05:00", text: "Deal 'Baseline Financial — compliance dashboard' moved to Negotiation" },
      { id: "a3", ts: "2026-09-14T16:40:00", text: "Ferrous Tools E-commerce Rebuild reached 91% complete" },
      { id: "a4", ts: "2026-09-12T09:15:00", text: "Campaign 'Q3 Journal digest' sent to 1,204 subscribers" },
      { id: "a5", ts: "2026-09-10T11:30:00", text: "New prospect added: Slate Athletic" },
    ],
  };

  function read(key) {
    const raw = localStorage.getItem(NS + key);
    return raw ? JSON.parse(raw) : null;
  }
  function write(key, val) {
    localStorage.setItem(NS + key, JSON.stringify(val));
  }
  function ensureSeeded() {
    Object.keys(SEED).forEach((key) => {
      if (read(key) === null) write(key, SEED[key]);
    });
    if (!localStorage.getItem(NS + "session")) {
      localStorage.setItem(NS + "session", "");
    }
  }
  ensureSeeded();

  return {
    get(key) { return read(key) || []; },
    set(key, val) { write(key, val); },
    reset() { Object.keys(SEED).forEach((key) => write(key, SEED[key])); },
    clientById(id) { return this.get("clients").find(c => c.id === id); },
    login(email) { localStorage.setItem(NS + "session", email || "demo@orbit.agency"); },
    logout() { localStorage.setItem(NS + "session", ""); },
    session() { return localStorage.getItem(NS + "session") || ""; },
    fmtMoney(n) { return "$" + Number(n).toLocaleString("en-AU"); },
    fmtDate(s) { return new Date(s).toLocaleDateString("en-AU", { day: "numeric", month: "short", year: "numeric" }); },
    logActivity(text) {
      const list = this.get("activity");
      list.unshift({ id: "a" + Date.now(), ts: new Date().toISOString(), text });
      this.set("activity", list.slice(0, 30));
    },
  };
})();
