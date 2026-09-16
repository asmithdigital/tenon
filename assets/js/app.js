/* Orbit OS — shared shell behaviour, runs on every /app/*.html page
   except the login screen. */
document.addEventListener("DOMContentLoaded", () => {
  const isLogin = document.body.hasAttribute("data-login-page");

  if (!isLogin) {
    const session = OrbitDB.session();
    if (!session) {
      window.location.href = "index.html";
      return;
    }
    const userEl = document.querySelector("[data-session-user]");
    if (userEl) userEl.textContent = session;

    const logoutBtns = document.querySelectorAll("[data-logout]");
    logoutBtns.forEach(btn => btn.addEventListener("click", () => {
      OrbitDB.logout();
      window.location.href = "index.html";
    }));
  }

  // mobile sidebar toggle
  const menuBtn = document.querySelector("[data-menu-toggle]");
  const sidebar = document.querySelector(".app-sidebar");
  if (menuBtn && sidebar) {
    menuBtn.addEventListener("click", () => sidebar.classList.toggle("open"));
  }

  document.querySelectorAll("[data-year]").forEach(el => {
    el.textContent = new Date().getFullYear();
  });

  // generic drawer open/close wiring (data-drawer-target + data-drawer-close)
  document.querySelectorAll("[data-drawer-close]").forEach(el => {
    el.addEventListener("click", () => closeDrawer(el.closest(".drawer, .drawer-backdrop")));
  });
});

function openDrawer(id) {
  document.getElementById(id + "-backdrop")?.classList.add("open");
  document.getElementById(id)?.classList.add("open");
}
function closeDrawer(el) {
  document.querySelectorAll(".drawer.open, .drawer-backdrop.open").forEach(d => d.classList.remove("open"));
}
