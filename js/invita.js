// Lee la invitación de «#i=…» (nunca sale del navegador) y prepara el botón que abre la app. Sin cookies ni estadísticas.
(function () {
  var p = {};
  location.hash.replace(/^#/, "").split("&").forEach(function (kv) {
    var i = kv.indexOf("=");
    if (i > 0) p[kv.slice(0, i)] = kv.slice(i + 1);
  });
  var c = (p.i || "").toLowerCase();
  var q = function (id) { return document.getElementById(id); };
  if (!/^[0-9a-f]{20}$/.test(c)) { q("sin-codigo").hidden = false; return; }
  // Intent de Android: lo resuelve el propio móvil; el código va en la consulta de ese intent local, no en una petición a internet.
  q("abrir").href = "intent://5pabos.github.io/ricorico-web/invita?i=" + c + "#Intent;scheme=https;package=com.ricorico.app;end";
  q("con-codigo").hidden = false;
  if (history.replaceState) history.replaceState(null, "", location.pathname); // quita el código de la barra de direcciones
})();
