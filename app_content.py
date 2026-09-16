# -*- coding: utf-8 -*-
"""Body HTML + inline render scripts for /app pages."""

# --------------------------------------------------------------- DASHBOARD
def dashboard_body():
    return """
<div class="kpi-row">
  <div class="kpi"><span class="num" id="kpi-active">—</span><span class="label">active clients</span><span class="delta up" id="kpi-active-d"></span></div>
  <div class="kpi"><span class="num" id="kpi-pipeline">—</span><span class="label">open pipeline value</span><span class="delta up" id="kpi-pipeline-d"></span></div>
  <div class="kpi"><span class="num" id="kpi-outstanding">—</span><span class="label">outstanding invoices</span><span class="delta down" id="kpi-outstanding-d"></span></div>
  <div class="kpi"><span class="num" id="kpi-mrr">—</span><span class="label">retainer value / mo</span><span class="delta up" id="kpi-mrr-d"></span></div>
</div>

<div class="grid-2" style="align-items:start;">
  <div class="panel">
    <div class="panel-head"><h2>Projects near deadline</h2><a href="projects.html" class="mono" style="font-size:0.8rem;">All projects</a></div>
    <div id="dash-projects"></div>
  </div>
  <div class="panel">
    <div class="panel-head"><h2>Recent activity</h2></div>
    <div id="dash-activity" class="flow"></div>
  </div>
</div>

<div class="panel" style="margin-top:1.5rem;">
  <div class="panel-head"><h2>Invoices due this month</h2><a href="invoices.html" class="mono" style="font-size:0.8rem;">All invoices</a></div>
  <div class="table-wrap"><table class="data-table" id="dash-invoices"></table></div>
</div>
"""


def dashboard_script():
    return """
<script>
(function(){
  const clients = OrbitDB.get('clients');
  const deals = OrbitDB.get('deals');
  const invoices = OrbitDB.get('invoices');
  const projects = OrbitDB.get('projects');
  const activity = OrbitDB.get('activity');

  const activeClients = clients.filter(c => c.stage === 'Active');
  document.getElementById('kpi-active').textContent = activeClients.length;
  document.getElementById('kpi-active-d').textContent = '+2 this quarter';

  const openPipeline = deals.filter(d => d.stage !== 'won').reduce((s,d)=>s+d.value,0);
  document.getElementById('kpi-pipeline').textContent = OrbitDB.fmtMoney(openPipeline);
  document.getElementById('kpi-pipeline-d').textContent = deals.filter(d=>d.stage!=='won').length + ' open deals';

  const outstanding = invoices.filter(i => i.status === 'active' || i.status === 'overdue').reduce((s,i)=>s+i.amount,0);
  document.getElementById('kpi-outstanding').textContent = OrbitDB.fmtMoney(outstanding);
  const overdueCount = invoices.filter(i=>i.status==='overdue').length;
  const od = document.getElementById('kpi-outstanding-d');
  od.textContent = overdueCount + ' overdue';
  if(!overdueCount){ od.className='delta up'; od.textContent='none overdue'; }

  const mrr = activeClients.reduce((s,c)=>s + Math.round(c.value/12), 0);
  document.getElementById('kpi-mrr').textContent = OrbitDB.fmtMoney(mrr);
  document.getElementById('kpi-mrr-d').textContent = 'across ' + activeClients.length + ' retainers';

  const projList = document.getElementById('dash-projects');
  projects.filter(p=>p.status==='Active').sort((a,b)=> new Date(a.due) - new Date(b.due)).slice(0,4).forEach(p=>{
    const client = OrbitDB.clientById(p.clientId);
    const row = document.createElement('div');
    row.style.marginBottom = '1.1rem';
    row.innerHTML = `
      <div class="split" style="margin-bottom:0.4rem;">
        <span style="font-size:0.92rem;">${p.name}</span>
        <span class="mono" style="font-size:0.78rem;color:var(--ink-soft);">due ${OrbitDB.fmtDate(p.due)}</span>
      </div>
      <div class="progress"><span style="width:${p.progress}%"></span></div>
      <div class="mono" style="font-size:0.75rem;color:var(--ink-soft);margin-top:0.3rem;">${client ? client.name : ''} · ${p.progress}%</div>
    `;
    projList.appendChild(row);
  });

  const actList = document.getElementById('dash-activity');
  activity.slice(0,6).forEach(a=>{
    const row = document.createElement('div');
    row.innerHTML = `<div style="font-size:0.9rem;">${a.text}</div><div class="mono" style="font-size:0.75rem;color:var(--ink-soft);">${new Date(a.ts).toLocaleString('en-AU',{day:'numeric',month:'short',hour:'numeric',minute:'2-digit'})}</div>`;
    actList.appendChild(row);
  });

  const invTable = document.getElementById('dash-invoices');
  const dueThisMonth = invoices.filter(i => i.status !== 'draft');
  invTable.innerHTML = `<thead><tr><th>Invoice</th><th>Client</th><th>Amount</th><th>Due</th><th>Status</th></tr></thead>
  <tbody>${dueThisMonth.map(i=>{
    const client = OrbitDB.clientById(i.clientId);
    return `<tr onclick="location.href='invoices.html'">
      <td class="mono">${i.id}</td><td>${client?client.name:''}</td><td>${OrbitDB.fmtMoney(i.amount)}</td>
      <td>${OrbitDB.fmtDate(i.due)}</td><td><span class="pill status-${i.status}">${i.status}</span></td>
    </tr>`;
  }).join('')}</tbody>`;
})();
</script>
"""


# ----------------------------------------------------------------- PIPELINE
def pipeline_body():
    return """
<div class="kanban" id="kanban-board"></div>
<div class="panel" style="margin-top:1.5rem;">
  <div class="panel-head"><h2>Add a deal</h2></div>
  <form id="deal-form" class="grid-3" style="align-items:end;">
    <div class="field" style="margin-bottom:0;"><label>Deal name</label><input name="name" required></div>
    <div class="field" style="margin-bottom:0;"><label>Value (AUD)</label><input name="value" type="number" min="0" required></div>
    <button class="btn btn-solid" type="submit">Add to Lead</button>
  </form>
</div>
"""


def pipeline_script():
    return """
<script>
(function(){
  const STAGES = [['lead','Lead'],['qualified','Qualified'],['proposal','Proposal'],['negotiation','Negotiation'],['won','Won']];
  const board = document.getElementById('kanban-board');

  function render(){
    const deals = OrbitDB.get('deals');
    board.innerHTML = STAGES.map(([key,label])=>{
      const items = deals.filter(d=>d.stage===key);
      const value = items.reduce((s,d)=>s+d.value,0);
      return `<div class="kanban-col" data-stage="${key}">
        <div class="kanban-col-head"><span>${label}</span><span class="count">${items.length} · ${OrbitDB.fmtMoney(value)}</span></div>
        <div class="kanban-cards" data-stage-list="${key}">
          ${items.map(d=>{
            const client = OrbitDB.clientById(d.clientId);
            return `<div class="kanban-card" draggable="true" data-deal-id="${d.id}">
              <span>${d.name}</span>
              <span class="value">${OrbitDB.fmtMoney(d.value)}</span>
              <span class="meta">${client?client.name:''} · ${d.owner}</span>
            </div>`;
          }).join('')}
        </div>
      </div>`;
    }).join('');
    wireDrag();
  }

  function wireDrag(){
    board.querySelectorAll('.kanban-card').forEach(card=>{
      card.addEventListener('dragstart', e=>{
        e.dataTransfer.setData('text/plain', card.dataset.dealId);
      });
    });
    board.querySelectorAll('.kanban-col').forEach(col=>{
      col.addEventListener('dragover', e=>{ e.preventDefault(); col.classList.add('drag-over'); });
      col.addEventListener('dragleave', ()=> col.classList.remove('drag-over'));
      col.addEventListener('drop', e=>{
        e.preventDefault();
        col.classList.remove('drag-over');
        const id = e.dataTransfer.getData('text/plain');
        const deals = OrbitDB.get('deals');
        const deal = deals.find(d=>d.id===id);
        if(deal){
          deal.stage = col.dataset.stage;
          OrbitDB.set('deals', deals);
          OrbitDB.logActivity(`Deal '${deal.name}' moved to ${col.querySelector('.kanban-col-head span').textContent}`);
          render();
        }
      });
    });
  }

  document.getElementById('deal-form').addEventListener('submit', e=>{
    e.preventDefault();
    const fd = new FormData(e.target);
    const deals = OrbitDB.get('deals');
    deals.push({ id:'d'+Date.now(), name: fd.get('name'), clientId:null, value: Number(fd.get('value')), stage:'lead', owner:'You' });
    OrbitDB.set('deals', deals);
    OrbitDB.logActivity(`New deal added: '${fd.get('name')}'`);
    e.target.reset();
    render();
  });

  render();
})();
</script>
"""


# ------------------------------------------------------------------ CLIENTS
def clients_body():
    return """
<div class="row" style="gap:0.6rem;margin-bottom:1.25rem;flex-wrap:wrap;" id="client-filters"></div>
<div class="table-wrap">
  <table class="data-table" id="clients-table"></table>
</div>

<div class="drawer-backdrop" id="client-drawer-backdrop"></div>
<aside class="drawer" id="client-drawer">
  <button class="drawer-close" data-drawer-close aria-label="Close">&times;</button>
  <div id="client-drawer-content"></div>
</aside>
"""


def clients_script():
    return """
<script>
(function(){
  const filters = ['All','Active','Prospect','Past'];
  const filterBar = document.getElementById('client-filters');
  let current = 'All';

  function renderFilters(){
    filterBar.innerHTML = filters.map(f=>`<button class="btn${f===current?' btn-solid':''}" data-filter="${f}" style="padding:0.5rem 1rem;font-size:0.85rem;">${f}</button>`).join('');
    filterBar.querySelectorAll('button').forEach(b=> b.addEventListener('click', ()=>{ current = b.dataset.filter; renderFilters(); renderTable(); }));
  }

  function renderTable(){
    const clients = OrbitDB.get('clients').filter(c => current==='All' || c.stage===current);
    const table = document.getElementById('clients-table');
    table.innerHTML = `<thead><tr><th>Client</th><th>Contact</th><th>Stage</th><th>Lifetime value</th><th>Since</th></tr></thead>
    <tbody>${clients.map(c=>`
      <tr data-client-id="${c.id}">
        <td>${c.name}</td><td>${c.contact}</td>
        <td><span class="pill status-${c.stage==='Active'?'active':c.stage==='Prospect'?'pending':'draft'}">${c.stage}</span></td>
        <td class="mono">${OrbitDB.fmtMoney(c.value)}</td>
        <td>${OrbitDB.fmtDate(c.since)}</td>
      </tr>`).join('')}</tbody>`;
    table.querySelectorAll('tbody tr').forEach(row=> row.addEventListener('click', ()=> openClient(row.dataset.clientId)));
  }

  function openClient(id){
    const c = OrbitDB.clientById(id);
    if(!c) return;
    document.getElementById('client-drawer-content').innerHTML = `
      <span class="pill status-${c.stage==='Active'?'active':c.stage==='Prospect'?'pending':'draft'}">${c.stage}</span>
      <h2 class="h2" style="margin-top:1rem;">${c.name}</h2>
      <p class="mono" style="color:var(--ink-soft);margin-top:0.5rem;">${c.contact} &middot; ${c.email}</p>
      <div class="flow" style="margin-top:1.5rem;">
        <div><div class="mono" style="font-size:0.75rem;color:var(--ink-soft);">Lifetime value</div><div style="font-size:var(--step-1);">${OrbitDB.fmtMoney(c.value)}</div></div>
        <div><div class="mono" style="font-size:0.75rem;color:var(--ink-soft);">Client since</div><div>${OrbitDB.fmtDate(c.since)}</div></div>
        <div><div class="mono" style="font-size:0.75rem;color:var(--ink-soft);">Notes</div><p>${c.notes}</p></div>
      </div>
      <a class="btn" style="margin-top:1rem;" href="mailto:${c.email}">Email ${c.contact.split(' ')[0]}</a>
    `;
    document.getElementById('client-drawer').classList.add('open');
    document.getElementById('client-drawer-backdrop').classList.add('open');
  }

  document.getElementById('client-drawer-backdrop').addEventListener('click', ()=>{
    document.getElementById('client-drawer').classList.remove('open');
    document.getElementById('client-drawer-backdrop').classList.remove('open');
  });

  renderFilters();
  renderTable();
})();
</script>
"""


# ----------------------------------------------------------------- PROJECTS
def projects_body():
    return """
<div class="flow" id="projects-list"></div>
"""


def projects_script():
    return """
<script>
(function(){
  const projects = OrbitDB.get('projects');
  const list = document.getElementById('projects-list');
  list.innerHTML = projects.map(p=>{
    const client = OrbitDB.clientById(p.clientId);
    return `<div class="panel">
      <div class="split" style="margin-bottom:0.75rem;">
        <div>
          <span class="pill status-${p.status==='Active'?'active':'draft'}">${p.status}</span>
          <h3 style="font-size:var(--step-1);margin-top:0.5rem;">${p.name}</h3>
        </div>
        <div style="text-align:right;">
          <div class="mono" style="font-size:0.8rem;color:var(--ink-soft);">due ${OrbitDB.fmtDate(p.due)}</div>
          <div class="mono" style="font-size:0.8rem;">${client?client.name:''}</div>
        </div>
      </div>
      <div class="progress"><span style="width:${p.progress}%"></span></div>
      <div class="split" style="margin-top:0.5rem;">
        <span class="mono" style="font-size:0.78rem;color:var(--ink-soft);">Lead: ${p.lead}</span>
        <span class="mono" style="font-size:0.78rem;color:var(--ink-soft);">${p.progress}% complete</span>
      </div>
    </div>`;
  }).join('');
})();
</script>
"""


# ----------------------------------------------------------------- INVOICES
def invoices_body():
    return """
<div class="split" style="margin-bottom:1.25rem;">
  <div class="row" style="gap:0.6rem;" id="invoice-filters"></div>
  <button class="btn btn-solid" id="new-invoice-btn">New invoice</button>
</div>
<div class="table-wrap"><table class="data-table" id="invoices-table"></table></div>

<div class="drawer-backdrop" id="invoice-drawer-backdrop"></div>
<aside class="drawer" id="invoice-drawer">
  <button class="drawer-close" data-drawer-close aria-label="Close">&times;</button>
  <h2 class="h2">New invoice</h2>
  <form id="invoice-form" class="flow" style="margin-top:1.5rem;">
    <div class="field"><label>Client</label><select name="clientId" id="invoice-client-select" required></select></div>
    <div class="field"><label>Amount (AUD)</label><input name="amount" type="number" min="0" required></div>
    <div class="field"><label>Due date</label><input name="due" type="date" required></div>
    <button class="btn btn-solid" type="submit">Create invoice</button>
  </form>
</aside>
"""


def invoices_script():
    return """
<script>
(function(){
  const filters = ['All','draft','active','sent','overdue'];
  let current = 'All';
  const filterBar = document.getElementById('invoice-filters');

  function renderFilters(){
    filterBar.innerHTML = filters.map(f=>`<button class="btn${f===current?' btn-solid':''}" data-f="${f}" style="padding:0.5rem 1rem;font-size:0.85rem;">${f}</button>`).join('');
    filterBar.querySelectorAll('button').forEach(b=> b.addEventListener('click', ()=>{ current=b.dataset.f; renderFilters(); renderTable(); }));
  }

  function renderTable(){
    const invoices = OrbitDB.get('invoices').filter(i=> current==='All' || i.status===current)
      .sort((a,b)=> new Date(b.issued) - new Date(a.issued));
    const table = document.getElementById('invoices-table');
    table.innerHTML = `<thead><tr><th>Invoice</th><th>Client</th><th>Amount</th><th>Issued</th><th>Due</th><th>Status</th><th></th></tr></thead>
    <tbody>${invoices.map(i=>{
      const client = OrbitDB.clientById(i.clientId);
      return `<tr>
        <td class="mono">${i.id}</td><td>${client?client.name:'—'}</td><td>${OrbitDB.fmtMoney(i.amount)}</td>
        <td>${OrbitDB.fmtDate(i.issued)}</td><td>${OrbitDB.fmtDate(i.due)}</td>
        <td><span class="pill status-${i.status}">${i.status}</span></td>
        <td>${i.status!=='active' && i.status!=='overdue' ? '' : `<button class="btn-icon" data-mark-paid="${i.id}" style="font-size:0.75rem;">Mark paid</button>`}</td>
      </tr>`;
    }).join('')}</tbody>`;
    table.querySelectorAll('[data-mark-paid]').forEach(btn=> btn.addEventListener('click', (e)=>{
      e.stopPropagation();
      const invoices = OrbitDB.get('invoices');
      const inv = invoices.find(i=>i.id===btn.dataset.markPaid);
      inv.status = 'sent';
      OrbitDB.set('invoices', invoices);
      OrbitDB.logActivity(`Invoice ${inv.id} marked paid`);
      renderTable();
    }));
  }

  const clientSelect = document.getElementById('invoice-client-select');
  clientSelect.innerHTML = OrbitDB.get('clients').map(c=>`<option value="${c.id}">${c.name}</option>`).join('');

  document.getElementById('new-invoice-btn').addEventListener('click', ()=>{
    document.getElementById('invoice-drawer').classList.add('open');
    document.getElementById('invoice-drawer-backdrop').classList.add('open');
  });
  document.getElementById('invoice-drawer-backdrop').addEventListener('click', ()=>{
    document.getElementById('invoice-drawer').classList.remove('open');
    document.getElementById('invoice-drawer-backdrop').classList.remove('open');
  });

  document.getElementById('invoice-form').addEventListener('submit', e=>{
    e.preventDefault();
    const fd = new FormData(e.target);
    const invoices = OrbitDB.get('invoices');
    const num = 1043 + invoices.filter(i=>i.id.startsWith('INV-')).length;
    const newInv = { id:'INV-'+num, clientId: fd.get('clientId'), amount:Number(fd.get('amount')), status:'draft', issued: new Date().toISOString().slice(0,10), due: fd.get('due') };
    invoices.unshift(newInv);
    OrbitDB.set('invoices', invoices);
    OrbitDB.logActivity(`Invoice ${newInv.id} created`);
    e.target.reset();
    document.getElementById('invoice-drawer').classList.remove('open');
    document.getElementById('invoice-drawer-backdrop').classList.remove('open');
    renderTable();
  });

  renderFilters();
  renderTable();
})();
</script>
"""


# ---------------------------------------------------------------- CAMPAIGNS
def campaigns_body():
    return """
<div class="split" style="margin-bottom:1.25rem;">
  <p style="max-width:48ch;color:var(--ink-soft);font-size:0.92rem;">Email marketing campaigns. This demo stores drafts locally —
  connect an ESP (Mailchimp, Customer.io, Postmark, etc.) to actually send.</p>
  <button class="btn btn-solid" id="new-campaign-btn">New campaign</button>
</div>
<div class="flow" id="campaigns-list"></div>

<div class="drawer-backdrop" id="campaign-drawer-backdrop"></div>
<aside class="drawer" id="campaign-drawer">
  <button class="drawer-close" data-drawer-close aria-label="Close">&times;</button>
  <h2 class="h2">New campaign</h2>
  <form id="campaign-form" class="flow" style="margin-top:1.5rem;">
    <div class="field"><label>Campaign name</label><input name="name" required></div>
    <div class="field"><label>Audience</label><input name="audience" placeholder="e.g. All subscribers (1,204)" required></div>
    <div class="field"><label>Subject line</label><input name="subject" required></div>
    <div class="field"><label>Body</label><textarea name="body" rows="5"></textarea></div>
    <button class="btn btn-solid" type="submit">Save as draft</button>
  </form>
</aside>
"""


def campaigns_script():
    return """
<script>
(function(){
  const list = document.getElementById('campaigns-list');

  function render(){
    const campaigns = OrbitDB.get('campaigns');
    list.innerHTML = campaigns.map(c=>`
      <div class="panel">
        <div class="split">
          <div>
            <span class="pill status-${c.status==='sent'?'sent':c.status==='scheduled'?'pending':'draft'}">${c.status}</span>
            <h3 style="font-size:var(--step-1);margin-top:0.5rem;">${c.name}</h3>
            <p class="mono" style="font-size:0.8rem;color:var(--ink-soft);margin-top:0.25rem;">${c.audience}</p>
          </div>
          <div class="grid-2" style="gap:1.5rem;text-align:right;">
            <div><div class="mono" style="font-size:0.75rem;color:var(--ink-soft);">Open rate</div><div>${c.openRate!==null?c.openRate+'%':'—'}</div></div>
            <div><div class="mono" style="font-size:0.75rem;color:var(--ink-soft);">Click rate</div><div>${c.clickRate!==null?c.clickRate+'%':'—'}</div></div>
          </div>
        </div>
      </div>`).join('');
  }

  document.getElementById('new-campaign-btn').addEventListener('click', ()=>{
    document.getElementById('campaign-drawer').classList.add('open');
    document.getElementById('campaign-drawer-backdrop').classList.add('open');
  });
  document.getElementById('campaign-drawer-backdrop').addEventListener('click', ()=>{
    document.getElementById('campaign-drawer').classList.remove('open');
    document.getElementById('campaign-drawer-backdrop').classList.remove('open');
  });

  document.getElementById('campaign-form').addEventListener('submit', e=>{
    e.preventDefault();
    const fd = new FormData(e.target);
    const campaigns = OrbitDB.get('campaigns');
    campaigns.unshift({ id:'cm'+Date.now(), name:fd.get('name'), audience:fd.get('audience'), status:'draft', sent:null, openRate:null, clickRate:null });
    OrbitDB.set('campaigns', campaigns);
    OrbitDB.logActivity(`Campaign '${fd.get('name')}' saved as draft`);
    e.target.reset();
    document.getElementById('campaign-drawer').classList.remove('open');
    document.getElementById('campaign-drawer-backdrop').classList.remove('open');
    render();
  });

  render();
})();
</script>
"""


# ----------------------------------------------------------------- SETTINGS
def settings_body():
    return """
<div class="grid-2" style="align-items:start;">
  <div class="panel">
    <div class="panel-head"><h2>Studio profile</h2></div>
    <form id="settings-form" class="flow">
      <div class="field"><label>Studio name</label><input name="studioName" value="Orbit Studio, Inc."></div>
      <div class="field"><label>Primary contact email</label><input name="email" value="hello@orbit.agency"></div>
      <div class="field"><label>Timezone</label>
        <select name="timezone">
          <option>Australia/Adelaide</option><option>Australia/Sydney</option>
          <option>UTC</option><option>America/New_York</option>
        </select>
      </div>
      <button class="btn btn-solid" type="submit">Save changes</button>
      <p class="mono" id="settings-status" style="color:var(--ink-soft);"></p>
    </form>
  </div>
  <div class="panel">
    <div class="panel-head"><h2>Connect real data</h2></div>
    <p style="color:var(--ink-soft);font-size:0.92rem;">This app currently runs entirely on mock data stored in your
    browser's local storage. To go live:</p>
    <ul class="flow" style="margin-top:1rem;">
      <li class="mark">Swap <code>OrbitDB</code> in <code>assets/js/data.js</code> for calls to a real database (Supabase, Firebase, or a custom API).</li>
      <li class="mark">Add real authentication in place of the demo login on <code>app/index.html</code>.</li>
      <li class="mark">Wire the campaigns form to an email provider (Mailchimp, Customer.io, Postmark) to actually send.</li>
      <li class="mark">Wire the contact form on the marketing site to the same backend so leads land straight in Pipeline.</li>
    </ul>
    <hr class="rule" style="margin-block:1.5rem;">
    <button class="btn" id="reset-data-btn">Reset demo data</button>
  </div>
</div>
"""


def settings_script():
    return """
<script>
document.getElementById('settings-form').addEventListener('submit', e=>{
  e.preventDefault();
  document.getElementById('settings-status').textContent = 'Saved locally. Connect a backend to persist this for real.';
});
document.getElementById('reset-data-btn').addEventListener('click', ()=>{
  if(confirm('Reset all demo data back to the original seed?')){
    OrbitDB.reset();
    location.reload();
  }
});
</script>
"""


def build(page):
    page("dashboard.html", "Dashboard", "Dashboard", "dashboard", dashboard_body(), extra_script=dashboard_script())
    page("pipeline.html", "Pipeline", "Pipeline", "pipeline", pipeline_body(), extra_script=pipeline_script())
    page("clients.html", "Clients", "Clients", "clients", clients_body(), extra_script=clients_script())
    page("projects.html", "Projects", "Projects", "projects", projects_body(), extra_script=projects_script())
    page("invoices.html", "Invoices", "Invoices", "invoices", invoices_body(), extra_script=invoices_script())
    page("campaigns.html", "Campaigns", "Campaigns", "campaigns", campaigns_body(), extra_script=campaigns_script())
    page("settings.html", "Settings", "Settings", "settings", settings_body(), extra_script=settings_script())
