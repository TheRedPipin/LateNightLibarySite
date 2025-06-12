document.addEventListener('DOMContentLoaded', function () {
  const hamburger = document.querySelector('.hamburger');
  const navUl = document.querySelector('nav ul');
  const navOverlay = document.querySelector('.nav-overlay');

  function closeMenu() {
    navUl.classList.remove('show');
    hamburger.classList.remove('active');
    hamburger.setAttribute('aria-expanded', 'false');
    if (navOverlay) navOverlay.classList.remove('show');
  }

  if (hamburger && navUl) {
    hamburger.addEventListener('click', function () {
      const isOpen = navUl.classList.toggle('show');
      hamburger.classList.toggle('active');
      hamburger.setAttribute('aria-expanded', isOpen);
      if (navOverlay) {
        if (isOpen) {
          navOverlay.classList.add('show');
        } else {
          navOverlay.classList.remove('show');
        }
      }
    });
  }

  if (navOverlay) {
    navOverlay.addEventListener('click', closeMenu);
  }
});