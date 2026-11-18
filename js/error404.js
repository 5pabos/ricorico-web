// Una de las frases de Rico al azar en cada visita al 404.
(function () {
  var frases = [
    'Aquí no hay nada… ni siquiera un yogur caducado.',
    'Esta página se ha ido de compras y todavía no ha vuelto.',
    'He mirado en toda la nevera y esta página no está.',
    'Hmm… esto no sale en ninguna receta que yo conozca.',
    'A todos se nos olvida algo al fondo de la nevera. A esta página, también.'
  ];
  var el = document.getElementById('frase');
  if (el) el.textContent = frases[Math.floor(Math.random() * frases.length)];
})();
