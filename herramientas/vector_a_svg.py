"""Convierte los iconos del muslito de la app (vectores de Android) a SVG para la web, SIN redibujarlos: mismos trazados y colores.

  python herramientas/vector_a_svg.py           → escribe img/muslo-<estado>.svg (7 estados)

Fuente: el proyecto de la app (F:/Apk, cambia --apk si está en otro sitio):
  hueso, crudo, fuego, oro, quemado, mordido → app/src/main/res/drawable/ic_estado_fg_<estado>.xml
  hecho (el logo de siempre)                  → app/src/main/res/drawable/ic_launcher_foreground.xml
Solo se usa la capa de primer plano (sin el fondo crema), para que floten sobre la página como emojis.
Un <group> de Android (escala, giro y traslación) pasa a un transform de SVG con el mismo orden: escala, giro alrededor del pivote y traslación.
"""
import argparse, pathlib, xml.etree.ElementTree as ET

NS = "{http://schemas.android.com/apk/res/android}"
ESTADOS = ["hueso", "crudo", "hecho", "fuego", "oro", "quemado", "mordido"]
raiz = pathlib.Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser()
ap.add_argument("--apk", default="F:/Apk")
a = ap.parse_args()
drawable = pathlib.Path(a.apk) / "app/src/main/res/drawable"

def num(v):
    v = float(v)
    return str(int(v)) if v == int(v) else ("%g" % v)

def trazado(p):
    s = ['d="%s"' % p.get(NS + "pathData")]
    s.append('fill="%s"' % p.get(NS + "fillColor") if p.get(NS + "fillColor") else 'fill="none"')
    if p.get(NS + "fillAlpha"): s.append('fill-opacity="%s"' % p.get(NS + "fillAlpha"))
    if p.get(NS + "strokeColor"):
        s.append('stroke="%s"' % p.get(NS + "strokeColor"))
        s.append('stroke-width="%s"' % num(p.get(NS + "strokeWidth", 1)))
        if p.get(NS + "strokeLineJoin"): s.append('stroke-linejoin="%s"' % p.get(NS + "strokeLineJoin"))
        if p.get(NS + "strokeLineCap"): s.append('stroke-linecap="%s"' % p.get(NS + "strokeLineCap"))
    return "<path " + " ".join(s) + "/>"

def nodo(el, sangria="  "):
    salida = []
    for h in el:
        if h.tag == "group":
            px, py = float(h.get(NS + "pivotX", 0)), float(h.get(NS + "pivotY", 0))
            rot, sx, sy = h.get(NS + "rotation", "0"), h.get(NS + "scaleX", "1"), h.get(NS + "scaleY", "1")
            tx, ty = float(h.get(NS + "translateX", 0)), float(h.get(NS + "translateY", 0))
            t = "translate(%s %s) translate(%s %s) rotate(%s) scale(%s %s) translate(%s %s)" % (num(tx), num(ty), num(px), num(py), rot, sx, sy, num(-px), num(-py))
            salida.append('%s<g transform="%s">' % (sangria, t))
            salida += nodo(h, sangria + "  ")
            salida.append("%s</g>" % sangria)
        elif h.tag == "path":
            salida.append(sangria + trazado(h))
    return salida

(raiz / "img").mkdir(exist_ok=True)
for e in ESTADOS:
    f = drawable / ("ic_launcher_foreground.xml" if e == "hecho" else "ic_estado_fg_%s.xml" % e)
    cuerpo = nodo(ET.parse(f).getroot())
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108" width="108" height="108">\n' + "\n".join(cuerpo) + "\n</svg>\n"
    (raiz / "img" / ("muslo-%s.svg" % e)).write_text(svg, encoding="utf8", newline="\n")
    print("img/muslo-%s.svg" % e)
