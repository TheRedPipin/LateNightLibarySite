document.addEventListener('DOMContentLoaded', function () {
  const hamburger = document.querySelector('.hamburger');
  const navUl = document.querySelector('nav ul');

  if (hamburger && navUl) {
    hamburger.addEventListener('click', function () {
      navUl.classList.toggle('show');
      hamburger.classList.toggle('active');
      hamburger.setAttribute('aria-expanded', navUl.classList.contains('show'));
    });
  }
});