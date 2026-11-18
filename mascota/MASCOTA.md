# Rico, la mascota de RicoRico

Un muslito de pollo con gorro de cocinero. Sale del icono de la app. Por ahora vive solo en la web (y redes); más adelante podrá entrar en la app.

## Personalidad
Cocinillas gracioso. Bromista, con ingenio de cocina y de nevera, nunca pesado ni sabelotodo. Se ríe de las situaciones (la nevera vacía, el yogur olvidado), no de la gente.
- **Nunca** bromas sobre comer carne ni sobre otros alimentos como «víctimas». Rico es amigo de todas las dietas: también de quien es vegetariano.
- Tono cercano y positivo. Frases cortas. Un chiste por mensaje como máximo.
- No da lecciones: propone («¿Y si cocinamos…?»).

## Cómo habla
Tutea. Español de España, sencillo. Exclamaciones con medida. Juegos de palabras de cocina («estoy a punto», «esto huele a éxito», «a fuego lento»).

## 10 frases de ejemplo
1. ¡Hola! ¿Qué cocinamos hoy?
2. Escanea el ticket y yo me encargo de la despensa.
3. Esa nevera está más vacía que mi plato después de postre… ¡vamos a la compra!
4. Hmm… con lo que tienes sale una cena estupenda. Dame un segundo.
5. ¡Plato cocinado! Esto merece un tenedor de oro.
6. A este yogur le quedan dos días. ¡Es hora de que sea el protagonista!
7. Apunta: huevos, tomate y pan. Lo demás ya lo tienes.
8. No pasa nada, a todos se nos olvida algo al fondo de la nevera.
9. Lo que sobró del cocido tiene una segunda vida. ¡Ropa vieja!
10. Hoy cocino yo… bueno, tú cocinas y yo animo desde el gorro.

## Reglas de estilo
- **Cuerpo**: el muslo (forma de huevo) es el cuerpo. El hueso son las piernas, con las dos puntas como pies. Gorro de cocinero. Brazos finos con manos redondas.
- **Colores** (los del icono): contorno `#23395B` (trazo 1,9), muslo `#E0913F`, brillo `#F6C27A`, hueso y gorro `#FFF8E7`, mejillas `#F4A6A6`. Colores planos, sin degradados; un brillo suave en el muslo.
- **Cara**: ojos ovalados negros con punto de brillo, mejillas rosas redondas, sonrisa de una línea. La expresión cambia con la pose: ojos en arco al reír, gota de sudor ante la nevera vacía, ceja alzada al pensar.
- **Formato**: SVG, con título accesible. Sin estilo anime ni sombras duras.
- **Movimiento**: si tiene que andar, **salta** (pequeños brincos con los dos pies a la vez).

## Poses (carpeta `mascota/`)
`saludando.svg` (a mano), `cocinando.svg`, `pensando.svg`, `celebrando.svg`, `lista.svg`, `nevera-vacia.svg`.
Las cinco últimas se generan con `python mascota/generar_poses.py`; si se cambia el cuerpo o la cara, se cambia ahí y se regeneran todas.

## Rico en los errores
Siempre se dice **qué ha pasado** y **qué puede hacer la persona** (volver al inicio, pedir un enlace nuevo, comprobar la conexión). Nunca textos técnicos.

**Cuándo SÍ hay humor (suave, una frase como máximo):** cosas sin consecuencias: página 404, ticket que no se lee, búsqueda de recetas sin resultados, sin internet al sincronizar la casa, enlace de «confirmar correo» caducado, usado o roto.
**Cuándo NO hay humor:** seguridad y dinero (contraseña, cambio de correo, entrar, borrar la cuenta, pagos, Premium, regalos), copias de seguridad, datos que no se guardan, borrados. Ahí Rico, como mucho, sale pequeño de adorno y el texto es claro y serio.

### Frases aprobadas
**404 (una al azar en cada visita):**
1. Aquí no hay nada… ni siquiera un yogur caducado.
2. Esta página se ha ido de compras y todavía no ha vuelto.
3. He mirado en toda la nevera y esta página no está.
4. Hmm… esto no sale en ninguna receta que yo conozca.
5. A todos se nos olvida algo al fondo de la nevera. A esta página, también.
Debajo, siempre en claro: «Esta página no existe o se ha movido», con «Volver al inicio» y «Descargar RicoRico». Pose: Rico ante la nevera vacía.

**Enlace de confirmar correo (humor suave):** caducado «Uy, a este enlace se le pasó el punto.» · ya usado «¡Repetir plato no vale!» · no válido «No me suena este enlace… ¿lo copiaste entero?»
**Enlaces de contraseña y cambio de correo:** sin frases de Rico (solo el mensaje claro y Rico pequeño).
**Mensajes claros de los enlaces:** caducado «Este enlace ya ha caducado (duran 30 minutos). Pide uno nuevo desde la app.» · usado «Este enlace ya se ha usado. Si ya confirmaste, todo está bien.» · no válido «Este enlace no es válido. Pide uno nuevo desde la app.»

**En la app:** ticket que no se lee «Hmm… este ticket se me resiste. Prueba otra vez con más luz y bien plano.» · recetas sin resultado «No encuentro «x» en mis recetas… ¿probamos con otra palabra?» · sin internet al sincronizar «Sin internet por ahora; yo sigo intentándolo.»
