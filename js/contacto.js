// Monta el enlace de correo al cargar la página: así la dirección no aparece escrita de una pieza en el HTML (los robots simples no la recogen).
// Sin JavaScript se ve «appricorico (arroba) gmail.com», legible para una persona.
// shortcut: no frena a un robot que ejecute JavaScript; para eso habría que usar un formulario, que se descartó para no tener servidor.
document.querySelectorAll('a.correo').forEach(function (a) {
  var dir = a.dataset.u + '@' + a.dataset.d;
  a.href = 'mailto:' + dir;
  if (!a.dataset.texto) a.textContent = dir;
});
