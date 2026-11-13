// Efectos de la portada. Todo es opcional: sin JavaScript o con «reducir movimiento» la página se ve igual, con las escenas como tarjetas normales.
(function () {
  var reducir = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // 1) El collage de recetas entra al aparecer en pantalla.
  var coleccion = document.querySelector('.escena3d');
  if (coleccion && !reducir && 'IntersectionObserver' in window) {
    coleccion.classList.add('espera');
    new IntersectionObserver(function (e, o) {
      if (e[0].isIntersecting) { coleccion.classList.remove('espera'); o.disconnect(); }
    }, { threshold: 0.25 }).observe(coleccion);
  }

  // 2) Cámara 3D: el scroll mueve el mundo hacia delante y cada escena se acerca, se ve de cerca y se queda atrás.
  var raiz = document.querySelector('.recorrido');
  if (!raiz || reducir) return;
  var mundo = raiz.querySelector('.mundo'), pista = raiz.querySelector('.pista');
  var escenas = Array.prototype.slice.call(raiz.querySelectorAll('.escena'));
  var PASO = 1100, n = escenas.length, objetivo = 0, actual = 0;
  raiz.classList.add('activo');

  var corriendo = false;
  function despertar() { if (!corriendo) { corriendo = true; requestAnimationFrame(pintar); } }
  function leer() {
    var total = raiz.offsetHeight - innerHeight;
    objetivo = Math.min(1, Math.max(0, -raiz.getBoundingClientRect().top / total));
    despertar();
  }
  function pintar() {
    actual += (objetivo - actual) * 0.12; // suaviza: sin saltos aunque el scroll sea brusco
    if (Math.abs(objetivo - actual) < 0.0002) actual = objetivo;
    var d0 = actual * (n - 1);
    mundo.style.transform = 'translateZ(' + (d0 * PASO).toFixed(1) + 'px)';
    escenas.forEach(function (e, i) {
      var d = i - d0; // >0: aún por llegar; <0: ya la hemos pasado
      var op = d > 0 ? Math.max(0, 1 - d * 0.7) : Math.max(0, 1 + d * 3);
      e.style.opacity = op.toFixed(3);
      e.style.visibility = op < 0.02 ? 'hidden' : 'visible';
    });
    if (pista) pista.style.opacity = actual < 0.03 ? 1 : 0;
    // El bucle solo sigue mientras el suavizado no ha llegado al objetivo.
    if (actual !== objetivo) requestAnimationFrame(pintar); else corriendo = false;
  }
  addEventListener('scroll', leer, { passive: true });
  addEventListener('resize', leer, { passive: true });
  leer(); actual = objetivo; corriendo = true; pintar();

  // La órbita de muslitos se pausa cuando no se ve (ahorra batería y GPU).
  var orbita = document.querySelector('.orbita');
  if (orbita && 'IntersectionObserver' in window) {
    var movil = orbita.querySelectorAll('.anillo, .muslo img');
    new IntersectionObserver(function (e) {
      var estado = e[0].isIntersecting ? 'running' : 'paused';
      for (var k = 0; k < movil.length; k++) movil[k].style.animationPlayState = estado;
    }).observe(orbita);
  }
})();
