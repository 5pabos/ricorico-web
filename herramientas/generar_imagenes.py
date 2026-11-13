"""Genera los favicon y la imagen para compartir (1200x630) a partir del icono de la app. Solo hace falta Pillow.
Uso:  python herramientas/generar_imagenes.py "F:/Apk/publicacion/recursos/icono_512.png"
Las fuentes son las de Windows (Georgia): las imágenes ya hechas se guardan en img/, la web no carga ninguna fuente."""
import pathlib, sys
from PIL import Image, ImageDraw, ImageFont

raiz = pathlib.Path(__file__).resolve().parents[1]
icono = Image.open(sys.argv[1]).convert("RGB")
img = raiz / "img"

icono.save(img / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
icono.resize((180, 180), Image.LANCZOS).save(img / "apple-touch-icon.png", optimize=True)

# Imagen para compartir: crema, icono a la izquierda, nombre y frase a la derecha (colores de la app).
CREMA, TINTA, APAGADO, TERRACOTA = (255, 251, 230), (18, 48, 58), (63, 90, 85), (191, 79, 42)
lienzo = Image.new("RGB", (1200, 630), CREMA)
d = ImageDraw.Draw(lienzo)
mascara = Image.new("L", (300, 300), 0)
ImageDraw.Draw(mascara).rounded_rectangle((0, 0, 299, 299), radius=64, fill=255)
lienzo.paste(icono.resize((300, 300), Image.LANCZOS), (110, 165), mascara)
d.rounded_rectangle((110, 165, 410, 465), radius=64, outline=TINTA, width=5)
titulo = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 104)
frase = ImageFont.truetype("C:/Windows/Fonts/georgia.ttf", 40)
pie = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 30)
d.text((470, 150), "RicoRico", font=titulo, fill=TINTA)
for i, linea in enumerate(["Escanea tu ticket y descubre", "qué cocinar con lo que tienes"]):
    d.text((474, 290 + i * 56), linea, font=frase, fill=TINTA)
d.rounded_rectangle((474, 440, 474 + 400, 440 + 64), radius=32, fill=TERRACOTA)
d.text((474 + 200, 440 + 32), "Muy pronto en Google Play", font=pie, fill=(255, 255, 255), anchor="mm")
lienzo.save(img / "compartir.png", optimize=True)
print("imágenes generadas")
