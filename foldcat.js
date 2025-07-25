document.addEventListener('DOMContentLoaded', function () {
  const main = document.querySelector('main');
  const foldBtn = document.querySelector('.fold-btn');
  const catReveal = document.querySelector('.cat-reveal');
  const foldHint = document.querySelector('.fold-hint');
  let resetTimeout = null;

  if (foldBtn) {
    foldBtn.addEventListener('mouseenter', function () {
      document.body.classList.add('show-fold-hint');
    });
    foldBtn.addEventListener('mouseleave', function () {
      document.body.classList.remove('show-fold-hint');
    });
    foldBtn.addEventListener('focus', function () {
      document.body.classList.add('show-fold-hint');
    });
    foldBtn.addEventListener('blur', function () {
      document.body.classList.remove('show-fold-hint');
    });
  }

  if (foldBtn && main && catReveal) {
    foldBtn.addEventListener('mouseenter', function () {
      if (!main.classList.contains('folded')) {
        main.classList.add('fold-peek');
      }
    });
    foldBtn.addEventListener('mouseleave', function () {
      main.classList.remove('fold-peek');
    });
    foldBtn.addEventListener('click', function () {
      main.classList.remove('fold-peek');
      main.classList.add('folded');
      if (foldHint) {
        foldHint.style.display = 'none';
      }
      setTimeout(() => {
        catReveal.classList.add('show');
        if (resetTimeout) clearTimeout(resetTimeout);
        resetTimeout = setTimeout(() => {
          main.classList.remove('folded');
          catReveal.classList.remove('show');
        }, 3000);
      }, 700);
    });
  }
});
