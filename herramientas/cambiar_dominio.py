"""Cambia la dirección base de la web en todos los archivos (og:url, canonical, datos estructurados, sitemap, robots, 404).
Hoy:        python herramientas/cambiar_dominio.py https://5pabos.github.io/ricorico-web   (no hace falta)
Con dominio: python herramientas/cambiar_dominio.py https://ricorico.es
La dirección actual está en sitio.txt. Si el nuevo es un dominio propio (sin ruta), también crea el archivo CNAME que GitHub Pages necesita."""
import pathlib, sys

raiz = pathlib.Path(__file__).resolve().parents[1]
actual = (raiz / "sitio.txt").read_text(encoding="utf8").strip().rstrip("/")
nueva = sys.argv[1].strip().rstrip("/") if len(sys.argv) > 1 else sys.exit("Uso: python herramientas/cambiar_dominio.py https://tudominio.es")
if not nueva.startswith("https://"):
    sys.exit("La dirección tiene que empezar por https://")
cambiados = 0
for f in list(raiz.glob("*.html")) + list(raiz.glob("recetas/*.html")) + [raiz / "sitemap.xml", raiz / "robots.txt"]:
    t = f.read_text(encoding="utf8")
    if actual in t:
        f.write_text(t.replace(actual, nueva), encoding="utf8")
        cambiados += 1
(raiz / "sitio.txt").write_text(nueva + "\n", encoding="utf8")
host = nueva.removeprefix("https://")
if "/" not in host:
    (raiz / "CNAME").write_text(host + "\n", encoding="utf8")
print(f"{cambiados} archivos cambiados: {actual} -> {nueva}")
