// Progressive enhancement: filters cards on skills.html and agents.html.
// Without JavaScript the full lists are shown.
(function () {
  var input = document.getElementById('q');
  if (!input) return;
  var status = document.getElementById('q-status');
  var items = Array.prototype.slice.call(document.querySelectorAll('[data-item]'));
  var groups = Array.prototype.slice.call(document.querySelectorAll('[data-group]'));
  var noun = input.getAttribute('data-filter') === 'agent' ? 'agents' : 'skills';

  function apply() {
    var q = input.value.trim().toLowerCase();
    var shown = 0;
    items.forEach(function (el) {
      var match = !q || el.textContent.toLowerCase().indexOf(q) !== -1;
      el.hidden = !match;
      if (match) shown++;
    });
    groups.forEach(function (g) {
      var any = g.querySelector('[data-item]:not([hidden])');
      g.hidden = !any;
    });
    status.textContent = q ? shown + ' of ' + items.length + ' ' + noun + ' shown' : '';
  }
  input.addEventListener('input', apply);
})();
