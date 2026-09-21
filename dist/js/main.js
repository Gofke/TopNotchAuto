document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var panel = document.querySelector('.mobile-panel');
  if (toggle && panel) {
    toggle.addEventListener('click', function () {
      panel.classList.toggle('open');
      toggle.setAttribute('aria-expanded', panel.classList.contains('open') ? 'true' : 'false');
    });
    panel.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () { panel.classList.remove('open'); });
    });
  }

  window.showToast = function (message) {
    var toast = document.getElementById('toast');
    if (!toast) return;
    toast.querySelector('span').textContent = message;
    toast.classList.add('show');
    clearTimeout(window.__toastTimer);
    window.__toastTimer = setTimeout(function () { toast.classList.remove('show'); }, 3200);
  };

  document.querySelectorAll('form[data-demo-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.getAttribute('data-success-message') || "Thanks! We'll be in touch soon.";
      window.showToast(msg);
      form.reset();
    });
  });
});
