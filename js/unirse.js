// Lee el código de «#c=…&h=…» (nunca sale del navegador) y prepara el botón que abre la app. Sin cookies ni estadísticas.
(function () {
  var p = {};
  location.hash.replace(/^#/, "").split("&").forEach(function (kv) {
    var i = kv.indexOf("=");
    if (i > 0) p[kv.slice(0, i)] = kv.slice(i + 1);
  });
  var c = (p.c || "").toUpperCase();
  var h = /^[0-9]{1,15}$/.test(p.h || "") ? p.h : "";
  var ok = /^[A-Z0-9]{4}(-?[A-Z0-9]{4}){2}$/.test(c);
  var q = function (id) { return document.getElementById(id); };
  if (!ok) { q("sin-codigo").hidden = false; return; }
  q("codigo").textContent = c;
  // Intent de Android: lo resuelve el propio móvil; el código va en la consulta de ese intent local, no en una petición a internet.
  q("abrir").href = "intent://5pabos.github.io/ricorico-web/unirse?c=" + encodeURIComponent(c) + (h ? "&h=" + h : "") +
    "#Intent;scheme=https;package=com.ricorico.app;end";
  q("con-codigo").hidden = false;
  q("con-codigo2").hidden = false;
  if (history.replaceState) history.replaceState(null, "", location.pathname); // quita el código de la barra de direcciones
})();
