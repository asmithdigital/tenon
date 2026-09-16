// Orbit — shared site behaviour
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.querySelectorAll('a').forEach(a => a.addEventListener('click', () => links.classList.remove('open')));
  }

  document.querySelectorAll('[data-year]').forEach(el => {
    el.textContent = new Date().getFullYear();
  });

  // duplicate ticker content once so the CSS keyframe loop is seamless
  document.querySelectorAll('.ticker-track').forEach(track => {
    track.innerHTML += track.innerHTML;
  });

  // basic contact form -> mailto fallback (no backend yet)
  const form = document.querySelector('[data-contact-form]');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const status = form.querySelector('[data-form-status]');
      const name = data.get('name') || '';
      const email = data.get('email') || '';
      const budget = data.get('budget') || '';
      const message = data.get('message') || '';
      const body = encodeURIComponent(
        `From: ${name} <${email}>\nBudget: ${budget}\n\n${message}`
      );
      if (status) {
        status.textContent = 'Thanks — opening your email client to send this. (Wire this form to your CRM/email service once connected.)';
      }
      window.location.href = `mailto:hello@orbit.agency?subject=${encodeURIComponent('New enquiry from ' + name)}&body=${body}`;
    });
  }
});
