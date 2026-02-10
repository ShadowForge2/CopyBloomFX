document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.getElementById('nav-toggle');
  var menu = document.getElementById('nav-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      menu.classList.toggle('open');
    });
  }
});
