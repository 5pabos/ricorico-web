# Recetas compartidas (preparado, sin generar)

Cada receta de la app podrá tener su página web, para que quien reciba el enlace sin tener la app la vea (foto, ingredientes y pasos) y pueda descargarla.

Aquí no hay páginas todavía. Se generan con el script (desde la carpeta de la web):

```
python herramientas/generar_recetas.py                                  # prueba en seco: cuenta qué se generaría
python herramientas/generar_recetas.py --generar --confirmo-fotos-propias
```

- **Fuente:** `recetas.json` y `fotos_creditos.json` de la app (`F:/Apk/app/src/main/assets`).
- **Solo fotos propias:** únicamente las recetas cuya foto está marcada «Foto aportada». Las de Wikimedia Commons no se usan.
- **Antes de generar:** confirma la licencia de esas fotos «aportadas». Por eso hace falta la segunda opción, `--confirmo-fotos-propias`.
- **Qué escribe:** `recetas/<nombre>-<id>.html`, `recetas/index.html` (lista), `img/recetas/<id>.jpg` y reescribe `sitemap.xml`.
- **Cada página:** título y descripción, vista previa para compartir, datos estructurados `Recipe` y el botón «Muy pronto en Google Play».
- **Cambio de dominio:** `herramientas/cambiar_dominio.py` también actualiza estas páginas.
- **Pendiente de decidir (más adelante):** el enlace de compartir dentro de la app, que llevaría a `recetas/<nombre>-<id>.html`.
