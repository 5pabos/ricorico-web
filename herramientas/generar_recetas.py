"""Genera una página web por cada receta de la app, usando SOLO las fotos propias (las marcadas «Foto aportada» en fotos_creditos.json).
Está preparado pero NO se ejecuta por sí solo: sin opciones solo cuenta qué se generaría (prueba en seco).

  python herramientas/generar_recetas.py                      -> prueba en seco: cuántas recetas tienen foto propia
  python herramientas/generar_recetas.py --generar --confirmo-fotos-propias
                                                              -> escribe recetas/*.html, img/recetas/*.jpg y reescribe sitemap.xml
La segunda opción es una confirmación a propósito: las fotos «aportadas» tienen la licencia por confirmar (mira publicacion/GUIA_PUBLICAR.md en el proyecto de la app).
Lee F:/Apk/app/src/main/assets/recetas.json y fotos_creditos.json (cambia --apk si el proyecto está en otro sitio). Solo hace falta Pillow."""
import argparse, html, json, pathlib, re, sys, unicodedata
from PIL import Image

raiz = pathlib.Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument("--apk", default="F:/Apk")
ap.add_argument("--salida", default=str(raiz), help="carpeta de la web (por defecto, esta)")
ap.add_argument("--generar", action="store_true")
ap.add_argument("--confirmo-fotos-propias", action="store_true")
a = ap.parse_args()

assets = pathlib.Path(a.apk) / "app/src/main/assets"
recetas = json.loads((assets / "recetas.json").read_text(encoding="utf8"))
creditos = {c["id"]: c for c in json.loads((assets / "fotos_creditos.json").read_text(encoding="utf8"))}
propias = [r for r in recetas if creditos.get(r["id"], {}).get("titulo") == "Foto aportada" and (assets / "fotos" / f"{r['id']}.jpg").exists()]
print(f"{len(recetas)} recetas; {len(propias)} con foto propia (se generarían); {len(recetas) - len(propias)} sin foto propia (no se generan).")
if not (a.generar and a.confirmo_fotos_propias):
    print("Prueba en seco: no se ha escrito nada. Para generar: --generar --confirmo-fotos-propias")
    sys.exit(0)

salida = pathlib.Path(a.salida)
base = (salida / "sitio.txt").read_text(encoding="utf8").strip().rstrip("/")
(salida / "recetas").mkdir(exist_ok=True)
(salida / "img" / "recetas").mkdir(parents=True, exist_ok=True)

def slug(t):
    t = unicodedata.normalize("NFD", t.lower())
    return re.sub(r"[^a-z0-9]+", "-", "".join(c for c in t if unicodedata.category(c) != "Mn")).strip("-")

def ingrediente(i):
    txt = i.get("t") or i["o"][0]
    return txt[0].upper() + txt[1:] + (" (opcional)" if i.get("x") else "")

CABECERA = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#FFFBE6">
<link rel="icon" href="../img/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="../img/apple-touch-icon.png">
<link rel="canonical" href="{url}">
{extra}<link rel="stylesheet" href="../css/estilo.css">
</head>
<body>
<header class="cabecera"><div class="contenedor"><a class="marca" href="../">RicoRico</a></div></header>
"""
PIE = """<footer class="pie"><div class="contenedor"><nav aria-label="Información legal"><a href="../aviso-legal.html">Aviso legal</a><a href="../privacidad.html">Política de privacidad</a></nav></div></footer>
</body>
</html>
"""
CTA = '<p class="pie-cta">¿Quieres esta receta en tu móvil, con las cantidades de tu cocina? <span class="cta" role="note">Muy pronto en Google Play</span></p>'

enlaces = []
for r in propias:
    nombre, rid = r["nombre"], r["id"]
    archivo = f"{slug(nombre)}-{rid}"
    Image.open(assets / "fotos" / f"{rid}.jpg").convert("RGB").save(salida / "img" / "recetas" / f"{rid}.jpg", quality=78, optimize=True)
    url = f"{base}/recetas/{archivo}.html"
    foto = f"{base}/img/recetas/{rid}.jpg"
    ings = [ingrediente(i) for i in r["ing"]]
    e = html.escape
    desc = f"Receta de {nombre.lower()}: {r['min']} minutos, {len(ings)} ingredientes y los pasos para cocinarla."
    ld = {"@context": "https://schema.org", "@type": "Recipe", "name": nombre, "image": foto, "inLanguage": "es",
          "totalTime": f"PT{r['min']}M", "recipeIngredient": ings,
          "recipeInstructions": [{"@type": "HowToStep", "text": p} for p in r["pasos"]]}
    extra = (f'<meta property="og:type" content="article">\n<meta property="og:title" content="{e(nombre)} · RicoRico">\n<meta property="og:description" content="{e(desc)}">\n'
             f'<meta property="og:url" content="{url}">\n<meta property="og:image" content="{foto}">\n<meta property="og:image:alt" content="{e(nombre)}">\n<meta name="twitter:card" content="summary_large_image">\n'
             f'<script type="application/ld+json">\n{json.dumps(ld, ensure_ascii=False)}\n</script>\n')
    cuerpo = (CABECERA.format(titulo=e(f"{nombre} · RicoRico"), desc=e(desc), url=url, extra=extra)
              + f'<main class="contenedor texto">\n<h1>{e(nombre)}</h1>\n<p>{r["min"]} minutos</p>\n'
              + f'<img src="../img/recetas/{rid}.jpg" alt="{e(nombre)}" style="max-width:100%;height:auto;border-radius:16px" width="640" height="480">\n'
              + "<h2>Ingredientes</h2>\n<ul>\n" + "\n".join(f"<li>{e(i)}</li>" for i in ings) + "\n</ul>\n"
              + "<h2>Preparación</h2>\n<ol>\n" + "\n".join(f"<li>{e(p)}</li>" for p in r["pasos"]) + "\n</ol>\n"
              + CTA + '\n<p><a href="./">Ver todas las recetas</a></p>\n</main>\n' + PIE)
    (salida / "recetas" / f"{archivo}.html").write_text(cuerpo, encoding="utf8")
    enlaces.append((archivo, nombre))

lista = "\n".join(f'<li><a href="{f}.html">{html.escape(n)}</a></li>' for f, n in enlaces)
indice = (CABECERA.format(titulo="Recetas · RicoRico", desc="Recetas de RicoRico con foto, ingredientes y pasos.", url=f"{base}/recetas/", extra="")
          + f'<main class="contenedor texto">\n<h1>Recetas</h1>\n<ul>\n{lista}\n</ul>\n{CTA}\n</main>\n' + PIE)
(salida / "recetas" / "index.html").write_text(indice, encoding="utf8")

urls = [f"{base}/", f"{base}/aviso-legal.html", f"{base}/privacidad.html", f"{base}/recetas/"] + [f"{base}/recetas/{f}.html" for f, _ in enlaces]
(salida / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                    + "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls) + "\n</urlset>\n", encoding="utf8")
print(f"Generadas {len(enlaces)} páginas de recetas en {salida / 'recetas'}")
