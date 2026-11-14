"""Genera las poses de Rico en SVG con las mismas piezas que saludando.svg (cuerpo, gorro, pierna, cara), para que todas encajen.
  python mascota/generar_poses.py        → escribe cocinando, pensando, celebrando, lista y nevera-vacia en esta carpeta.
«saludando.svg» está dibujado a mano y NO se regenera aquí. Colores: los del icono de la app."""
import pathlib

NAVY, CARNE, CREMA, BRILLO, ROSA = "#23395B", "#E0913F", "#FFF8E7", "#F6C27A", "#F4A6A6"
AQUI = pathlib.Path(__file__).resolve().parent

def sombra(rx=17, op=.12):
    return f'<ellipse cx="50" cy="117" rx="{rx}" ry="2.6" fill="{NAVY}" opacity="{op}"/>'

def pierna():
    return ('<rect x="46.2" y="88" width="7.6" height="17" rx="3.4" fill="#FFF8E7"/><circle cx="45.6" cy="109" r="5.6" fill="#FFF8E7"/>'
            '<circle cx="54.4" cy="109" r="5.6" fill="#FFF8E7"/><path d="M47.4,104.5 L52.6,104.5" fill="none" stroke="#FFF8E7" stroke-width="3.6"/>')

def brazo(d, x, y):
    return f'<path d="{d}" fill="none"/><circle cx="{x}" cy="{y}" r="4.3" fill="{CARNE}"/>'

CUERPO = '<path d="M50,31 C70,31 78.5,49 76.5,65 C74.5,80 63,90 50,92 C37,90 25.5,80 23.5,65 C21.5,49 30,31 50,31 Z" fill="#E0913F"/>'
GORRO = ('<circle cx="41.6" cy="20" r="7.6" fill="#FFF8E7"/><circle cx="58.4" cy="20" r="7.6" fill="#FFF8E7"/><circle cx="50" cy="14" r="9" fill="#FFF8E7"/>'
         '<circle cx="41.6" cy="20" r="5.6" fill="#FFF8E7" stroke="none"/><circle cx="58.4" cy="20" r="5.6" fill="#FFF8E7" stroke="none"/>'
         '<rect x="37" y="25.5" width="26" height="10" rx="3.4" fill="#FFF8E7"/>')
BRILLO_SVG = f'<path d="M62,43 C67,46 70,51 70,56" fill="none" stroke="{BRILLO}" stroke-width="3.2" stroke-linecap="round"/>'
MEJILLAS = f'<circle cx="35.4" cy="68.6" r="3.9" fill="{ROSA}" opacity=".9"/><circle cx="64.6" cy="68.6" r="3.9" fill="{ROSA}" opacity=".9"/>'

def ojos(dx=0, dy=0):
    return (f'<ellipse cx="{42+dx}" cy="{61+dy}" rx="2.7" ry="3.6" fill="{NAVY}"/><ellipse cx="{58+dx}" cy="{61+dy}" rx="2.7" ry="3.6" fill="{NAVY}"/>'
            f'<circle cx="{42.9+dx}" cy="{59.6+dy}" r=".95" fill="#fff"/><circle cx="{58.9+dx}" cy="{59.6+dy}" r=".95" fill="#fff"/>')

def cara(tipo):
    sonrisa = f'<path d="M44.2,68.8 Q50,75 55.8,68.8" fill="none" stroke="{NAVY}" stroke-width="1.9" stroke-linecap="round"/>'
    if tipo == "normal":
        return ojos() + MEJILLAS + sonrisa
    if tipo == "mira-izq":
        return ojos(-1.8) + MEJILLAS + sonrisa
    if tipo == "mira-der":
        return ojos(1.8) + MEJILLAS + sonrisa
    if tipo == "pensando":  # ojos hacia arriba, una ceja alzada y boca pequeña ladeada
        return (ojos(2.2, -2.2) + MEJILLAS + f'<path d="M54.6,54 Q58.6,51.4 62.4,53.6" fill="none" stroke="{NAVY}" stroke-width="1.7" stroke-linecap="round"/>'
                f'<path d="M46.4,70.2 Q50.6,71.8 55,69.4" fill="none" stroke="{NAVY}" stroke-width="1.9" stroke-linecap="round"/>')
    if tipo == "feliz":  # ojos en arco y boca abierta
        return (f'<path d="M38.6,62.6 Q42,57.2 45.4,62.6" fill="none" stroke="{NAVY}" stroke-width="2.1" stroke-linecap="round"/>'
                f'<path d="M54.6,62.6 Q58,57.2 61.4,62.6" fill="none" stroke="{NAVY}" stroke-width="2.1" stroke-linecap="round"/>' + MEJILLAS +
                f'<path d="M43.8,67.4 Q50,80 56.2,67.4 Z" fill="#8A3B34" stroke="{NAVY}" stroke-width="1.7" stroke-linejoin="round"/>'
                '<path d="M46.6,73.6 Q50,70.8 53.4,73.6 Q50,77 46.6,73.6 Z" fill="#E8828A"/>')
    if tipo == "preocupado":  # cejas inclinadas, boca ondulada y gotita de sudor
        return (ojos(1.8) + MEJILLAS +
                f'<path d="M38.4,54.4 L45.6,56.4" stroke="{NAVY}" stroke-width="1.7" stroke-linecap="round"/><path d="M61.6,54.4 L54.4,56.4" stroke="{NAVY}" stroke-width="1.7" stroke-linecap="round"/>'
                f'<path d="M43.6,72 Q46.8,68.6 50,72 T56.4,72" fill="none" stroke="{NAVY}" stroke-width="1.9" stroke-linecap="round"/>'
                f'<path d="M74,37 C76.6,41.2 78.2,43.6 74,47.6 C69.8,43.6 71.4,41.2 74,37 Z" fill="#A8DCF0" stroke="{NAVY}" stroke-width="1.3" stroke-linejoin="round"/>')
    raise ValueError(tipo)

def svg(titulo, vb, cuerpo, ancho=None):
    x, y, w, h = vb
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" width="{w*4}" height="{h*4}" role="img" aria-labelledby="t">\n'
            f'  <title id="t">{titulo}</title>\n  <!-- Rico, la mascota de RicoRico. Generado por generar_poses.py con las mismas piezas que saludando.svg -->\n{cuerpo}\n</svg>\n')

def figura(brazos, cara_tipo, extra_detras="", extra_delante="", sombra_svg=None, salto=0):
    g = (f'<g stroke="{NAVY}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{extra_detras}{pierna()}{brazos}{CUERPO}{GORRO}</g>'
         f'{BRILLO_SVG}{cara(cara_tipo)}{extra_delante}')
    if salto: g = f'<g transform="translate(0,{-salto})">{g}</g>'
    return f'  {sombra_svg or sombra()}\n  {g}'

POSES = {}

# Cocinando: sartén con un huevo y vapor, mirando la sartén.
sarten = (f'<g stroke="{NAVY}" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">'
          '<path d="M93.4,70.6 L106,66.4" fill="none" stroke-width="3.6"/><g transform="rotate(-7 113 67)"><ellipse cx="113" cy="67" rx="14" ry="5.4" fill="#4B5A70"/>'
          '<ellipse cx="113" cy="66.2" rx="10.6" ry="3.4" fill="#33415A" stroke="none"/><ellipse cx="113" cy="65.8" rx="6.6" ry="2.4" fill="#FFF8E7" stroke="none"/>'
          '<circle cx="113" cy="65.4" r="2.1" fill="#F6C846" stroke="none"/></g></g>'
          f'<g fill="none" stroke="{NAVY}" stroke-width="1.5" stroke-linecap="round" opacity=".45"><path d="M106,58 Q103,54 106,50 Q109,46 106,42"/><path d="M114,56 Q111,52 114,48 Q117,44 114,40"/></g>')
POSES["cocinando"] = ("Rico cocinando con una sartén", (0, 0, 128, 124),
    figura(brazo("M75.5,64 C82,66 86,69 89,70", 91, 70.6) + brazo("M24.5,66 C17,70 14.4,76 14.4,82", 14.4, 85.4), "mira-der", extra_delante=sarten))

# Pensando: mano en la barbilla y una nube de pensamiento con puntos suspensivos.
nube = (f'<g stroke="{NAVY}" stroke-width="1.6" stroke-linejoin="round"><circle cx="82.6" cy="34" r="2" fill="#fff"/><circle cx="88.6" cy="26.4" r="3.1" fill="#fff"/>'
        '<ellipse cx="102" cy="13.6" rx="15" ry="9.6" fill="#fff"/></g>'
        f'<g fill="{NAVY}"><circle cx="95.6" cy="13.8" r="1.5"/><circle cx="102" cy="13.8" r="1.5"/><circle cx="108.4" cy="13.8" r="1.5"/></g>')
POSES["pensando"] = ("Rico pensando, con la mano en la barbilla", (0, 0, 120, 124),
    figura(brazo("M24.5,66 C17,70 14.4,76 14.4,82", 14.4, 85.4), "pensando", extra_delante=nube +
    f'<g stroke="{NAVY}" stroke-width="1.9" stroke-linecap="round"><path d="M75,62 C80,68 76,74 68,75.4" fill="none"/><circle cx="64.6" cy="75.8" r="4.3" fill="{CARNE}"/></g>'))

# Celebrando: salta con los dos brazos arriba, ojos felices y confeti.
confeti = (f'<g stroke="none"><rect x="12" y="14" width="5" height="2.4" rx="1" fill="#E85D75" transform="rotate(-30 14 15)"/><circle cx="104" cy="18" r="2.3" fill="#00A89A"/>'
           '<rect x="106" y="52" width="5" height="2.4" rx="1" fill="#F6C846" transform="rotate(35 108 53)"/><circle cx="6" cy="58" r="2.2" fill="#8F7BFF"/>'
           '<rect x="62" y="-4" width="5" height="2.4" rx="1" fill="#F4A6A6" transform="rotate(20 64 -3)"/><rect x="20" y="46" width="2.4" height="5" rx="1" fill="#00A89A"/>'
           '<circle cx="96" cy="2" r="1.8" fill="#E85D75"/><rect x="84" y="62" width="2.4" height="5" rx="1" fill="#8F7BFF" transform="rotate(30 85 64)"/></g>')
POSES["celebrando"] = ("Rico celebrando con los brazos en alto y confeti", (0, -8, 112, 132),
    figura(brazo("M75.5,64 C84,58 90,48 92,38", 92.4, 34.6) + brazo("M24.5,64 C16,58 10,48 8,38", 7.6, 34.6), "feliz",
           extra_detras=confeti, sombra_svg=sombra(12, .09), salto=6))

# Con la lista de la compra: la lleva en una mano y la mira.
lista = (f'<g stroke="{NAVY}" stroke-width="1.7" stroke-linejoin="round"><g transform="rotate(-6 16 72)"><rect x="3" y="54" width="27" height="36" rx="3" fill="#FFFDF4"/>'
         '<g fill="none" stroke-linecap="round"><path d="M7,63 L9,65.2 L12.4,60.8" stroke="#00796B"/><path d="M15,63 L26,63" opacity=".55"/>'
         '<path d="M7,72 L9,74.2 L12.4,69.8" stroke="#00796B"/><path d="M15,72 L25,72" opacity=".55"/><path d="M7,81 L9,83.2 L12.4,78.8" stroke="#00796B"/><path d="M15,81 L24,81" opacity=".55"/></g></g></g>')
POSES["lista"] = ("Rico con la lista de la compra en la mano", (0, 0, 108, 124),
    figura(brazo("M24.5,66 C22,70.4 23.6,74 27.4,75.2", 29.2, 75.6) + brazo("M75.5,66 C83,70 85.6,76 85.6,82", 85.6, 85.4), "mira-izq", extra_detras=lista))

# Mirando una nevera vacía: nevera abierta con estantes sin nada, cara de apuro.
nevera = (f'<g stroke="{NAVY}" stroke-width="1.9" stroke-linejoin="round" stroke-linecap="round"><rect x="92" y="16" width="50" height="100" rx="5" fill="#EAF4F1"/>'
          '<rect x="97" y="22" width="40" height="88" rx="2.5" fill="#FFF6C9" stroke-width="1.3"/><g fill="none" stroke-width="1.6"><path d="M97,47 L137,47"/><path d="M97,72 L137,72"/><path d="M97,95 L137,95"/></g>'
          '<path d="M92,16 L83,21 L83,112 L92,116 Z" fill="#DCEBE6"/><rect x="85.2" y="58" width="2.6" height="20" rx="1.2" fill="#23395B" stroke="none"/></g>')
POSES["nevera-vacia"] = ("Rico mirando con apuro una nevera vacía", (0, 0, 148, 124),
    figura(brazo("M75.5,64 C77.6,62.4 79.4,62.2 81,62.6", 82.6, 62.8) + brazo("M24.5,66 C17,70 14.4,76 14.4,82", 14.4, 85.4), "preocupado", extra_detras=nevera))

if __name__ == "__main__":
    for nombre, (titulo, vb, cuerpo) in POSES.items():
        (AQUI / f"{nombre}.svg").write_text(svg(titulo, vb, cuerpo), encoding="utf8", newline="\n")
        print(nombre + ".svg")
