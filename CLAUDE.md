# CLAUDE.md: 100 Days of Pythonic Engineering

Este repo produce los posts de LinkedIn de **Mateo Soto** (Data Engineer, Azure + Databricks) para la serie **"100 Days of Pythonic Engineering"**, y los scripts de código que los acompañan.

Toda pieza nueva (copy, carrusel, infografía, script) **debe** seguir este documento. Si una petición choca con una regla, avisa del conflicto antes de romperla.

---

## 1. Flujo de trabajo por día

1. Lee `docs/Plan_Maestro_V3_100_Days_of_Pythonic_Engineering.docx` (calendario) y la tabla de seguimiento del `README.md` (sección 9).
2. Identifica el **tipo de post** (sección 2). Ese tipo define la **paleta** (sección 3) y el **formato** (sección 4).
3. La carpeta `days/dayNN_slug/` ya existe para los días 04 a 15 (con `post.md` y `example.py`/`example.sql`). Agrega `build.py` copiando el de `days/day04_data_skew/` (ejemplo de referencia aprobado): reutiliza `font_css()`, `chrome()`, `slide()` y `main()`, y cambia `TOTAL`, el número de día, el nivel y las funciones de cada lámina.
4. Revisa o ajusta el copy (sección 6) en `days/dayNN_slug/post.md`, con el primer comentario al final.
5. Construye y renderiza: `scripts/render.sh days/dayNN_slug <paleta>`.
6. **Revisa visualmente cada lámina** (abre los PNG de `preview/`): sin texto cortado, sin código desbordado, sin huecos grandes.
7. Pasa el checklist de la sección 10.
8. Actualiza el seguimiento (sección 9) a "Listo" y, cuando Mateo confirme, a "Publicado" con el link.
9. Commit en git (sección 11).

---

## 2. Tipos de post (rotación)

| Tipo | Objetivo | Paleta | Formato preferido |
|---|---|---|---|
| **Errores que cuestan plata** | Costo y rendimiento en Spark, Databricks y Azure | `pino` | Carrusel PDF |
| **Antes vs. Después (código)** | Quick wins de Python y refactors | `pino` | Carrusel corto (4 a 5 láminas) o imagen única |
| **Arquitectura en una imagen** | Pipelines, Medallion, SCD, flujos | `bosque` | Carrusel PDF o imagen única |
| **Guardable** | Checklists, roadmaps, cheat sheets | `bosque` | Carrusel PDF |
| **Pregunta de entrevista** | Autoridad de Mateo como entrevistador técnico | `medianoche` | Carrusel PDF |
| **Opinión / Debate** | Generar comentarios | `medianoche` | Texto largo + 1 imagen |

Regla de mezcla: no publicar más de 2 días seguidos del mismo tipo.

---

## 3. Sistema de color

Las paletas viven en `design/theme.css`, se activan con `<body data-theme="...">` y **no se inventan colores nuevos**. Solo existen estas tres:

| Token | Uso | `pino` | `bosque` | `medianoche` |
|---|---|---|---|---|
| `--inkbg` | Fondo de láminas oscuras | `#071A22` | `#0A1F16` | `#070F24` |
| `--icebg` | Fondo de láminas claras | `#E7F3F1` | `#EAF4EC` | `#EDF1FA` |
| `--a1l` | Acento sobre fondo oscuro | `#5CD1B1` | `#7EE0A1` | `#8FA4FF` |
| `--a1` | Acento medio (barras, bordes de código) | `#2FA58A` | `#3FA968` | `#4361EE` |
| `--a1d` | Acento sobre fondo claro | `#11634F` | `#1F6B3F` | `#2B3FB8` |
| `--a2` | Acento secundario (casi no se usa) | `#4DA3DE` | `#5FB3C9` | `#44D7B6` |
| `--hl` | Resaltado de la palabra clave | `#D4F26A` lima | `#B8F0FF` celeste | `#7DF9FF` cian |

Reglas:
- **Una sola palabra o frase resaltada por titular** (`<span class="hl">`). En lámina clara se ve como subrayado de marcador; en lámina oscura, como texto de color.
- El resaltado `--hl` se usa también para **el dato crítico** de un gráfico (la barra culpable, el valor máximo). Nada más.
- Las láminas **alternan oscuro / claro**: la portada y el cierre siempre son oscuros. Con un número par de láminas, la penúltima es oscura y queda junto al cierre (única excepción permitida).
- Colores derivados: usar `color-mix(in srgb, var(--a1) 45%, var(--icebg))`, nunca hex sueltos.

---

## 4. Tipografía y formato

**Fuentes** (embebidas desde `design/fonts/`, licencia OFL):
- **Montserrat 900**: titulares (`h1` 108 px portada, `h2` 84 px interiores, `letter-spacing:-.02em`, `line-height:1.02`).
- **Montserrat 700/800**: kicker, cabecera, etiquetas, en MAYÚSCULAS con `letter-spacing:.12em` a `.14em`.
- **Roboto 400/500/700**: texto (lead 38 px, captions 30 a 34 px). Nunca menos de 24 px.
- **Roboto Mono 400/500**: código, números, métricas (código 26 a 31 px).

**Lienzo**: 1080 x 1350 px (4:5), una lámina por página de PDF. Márgenes laterales de 84 px.

**Estructura fija de cada lámina** (ya implementada en `chrome()` del ejemplo):
- Cabecera: `PYTHONIC ENGINEERING · DÍA NN / 100` a la izquierda (nombre de la serie atenuado con `.series`, día en el acento) y la píldora de nivel (`BÁSICO`, `INTERMEDIO`, `AVANZADO`) a la derecha, con una línea fina debajo.
- Kicker de 1 a 3 palabras (ej. `ARREGLO 3`), titular y contenido.
- Pie: `Mateo Soto · Data Engineer` a la izquierda (nombre en Montserrat, rol en Roboto atenuado) y `NN / TT` en Roboto Mono a la derecha. Igual en todas las láminas, cierre incluido.
- Barra de progreso segmentada en el borde inferior.
- `DESLIZA →` en todas las láminas menos la última.

**Estructura del carrusel** (de 5 a 8 láminas):
1. **Portada (oscura)**: hook en forma de problema concreto y un visual que lo demuestre (gráfico, diagrama). Nada de portadas solo con texto.
2. **El problema**: qué es, explicado en una frase y un visual.
3. a N-1. **Contenido**: una idea por lámina; si hay código, como máximo 8 líneas por lámina.
N. **Cierre (oscuro)**: pregunta para comentar y tres filas con etiquetas `GUARDA`, `DÍA NN+1` y `REPO`.

**Firma y serie**: constantes `AUTHOR = "Mateo Soto"`, `ROLE = "Data Engineer"` y `SERIES = "Pythonic Engineering"` al inicio de `build.py`. Firma en el pie y serie en la cabecera de todas las láminas. El nombre completo ("100 Days of Pythonic Engineering") no cabe junto a la píldora de nivel: el `/ 100` ya lo comunica. No agregar más (ni stack, ni certificaciones, ni bloque de autor): Mateo lo prefiere así.
- La credibilidad viene del contenido: experiencia propia dentro del post ("lo he visto en...", "en entrevistas técnicas..."). Nunca se inventa: se deja `[TU ANÉCDOTA: ...]` en el copy para que Mateo la complete.

**Formatos alternativos**:
- Imagen única: el mismo lienzo y la misma cabecera y pie, sin barra de progreso ni "Desliza".
- Infografía animada: **GIF animado que se sube como foto** (botón "Añadir una foto", no como video). LinkedIn lo muestra como imagen: sin controles, en bucle infinito, y al hacer clic se abre en el visor de fotos. No se sube MP4: el MP4 sí trae reproductor con pausa y barra, y no es el efecto buscado.
  - Mismas paletas y fuentes. Varios bloques pequeños en movimiento a la vez (flujos, flechas, datos que viajan), porque la gente se queda leyendo cada flujo.
  - Entregables en `days/dayNN_slug/`: `dayNN_slug.gif` (el que se sube) y `dayNN_slug.png` (versión estática de respaldo).
  - Bucle corto: de 3 a 5 segundos a 15-20 FPS. El peso del GIF debe quedar por debajo de ~5 MB (límite de imágenes de LinkedIn, **VERIFICAR** el vigente antes de publicar). Si pesa de más: menos frames, menos colores o menos tamaño. El diseño plano y de pocos colores de este sistema comprime muy bien.
  - Cómo se produce (por probar en el primer día animado): `build.py` genera el HTML con la animación controlada por un progreso `t` de 0 a 1; Chrome headless captura un frame por cada valor de `t`; y Pillow arma el GIF (`pip install pillow`, en un entorno virtual). No hay `ffmpeg` ni Pillow instalados en esta máquina. Alternativa manual en Mac: grabar el HTML con Kap y exportar a GIF.
- "Ventana macOS" del plan V3 (días 10 y 12): se resuelve como carrusel corto Antes/Después con bloques `.code` del tema, sin los tres puntos de ventana ni sombras.

**Límites prácticos para que nada se desborde** (aprendidos al renderizar):
- Código a 29 px dentro de `.code`: máximo unos 48 caracteres por línea; a 26 px, unos 54. Parte las líneas largas en lugar de bajar de 26 px.
- Como máximo 2 bloques de código por lámina.

---

## 4.1 Claridad: avanzado, pero accesible para todos (obligatorio)

El tema puede ser avanzado, pero **el carrusel lo debe entender alguien que sabe SQL y nunca ha usado Spark ni Databricks**, sin que el carrusel se infle (máximo 8 láminas). Mucha gente solo ve las láminas y no lee el copy, así que cada lámina se explica sola.

### 1. Define cada término donde aparece

- Todo término técnico (partición, shuffle, executor, AQE, broadcast, spill, Delta, Unity Catalog...) se define en lenguaje simple, en máximo ~15 palabras, **en la lámina donde aparece por primera vez**. Aunque el copy también lo explique: la redundancia es intencional.
- Cómo: componente `.defs` / `.def` de `theme.css` (término + definición), dentro del lead, o en una línea `.why`.
- Máximo 2 definiciones por lámina. Si hacen falta más, la lámina tiene demasiadas ideas.
- Ordena las láminas para que ningún término aparezca antes de la lámina que lo define. Si una definición introduce otro término, reescríbela sin él (ej. shuffle = "mover filas por la red", sin mencionar executors todavía).
- Las métricas y señales también se explican: no basta "Shuffle Read enorme", hay que decir qué es el Shuffle Read.

### 2. Usa el lenguaje técnico nativo, nunca paráfrasis

Usa el nombre exacto que aparece en la Spark UI, la documentación oficial vigente de Databricks o Azure, o el código. Defínelo una vez y úsalo igual en todo el carrusel y en el copy.

| Ámbito | Sí (nombre nativo) | No (paráfrasis) |
|---|---|---|
| Spark | `executor`, `driver`, `key`, "key caliente", `shuffle`, `stage`, `broadcast`, `spill`, `salt` | "máquina", "llave", "clave", "nodo" como sinónimo de executor, "sal" |
| Databricks | Delta Lake / tabla Delta, Unity Catalog, `catalog.schema.table`, Auto Loader, notebook, workspace, cluster, SQL warehouse, Liquid Clustering, `OPTIMIZE`, `MERGE` | "base de datos de Databricks", "cargador automático", "el catálogo de datos" |
| Azure | storage account, container, ADLS Gen2, Managed Identity, service principal, Key Vault, RBAC | "cuenta de almacenamiento genérica", "usuario de la app", "la bóveda" |

- Se mantienen en español las traducciones directas que todos reconocen: tarea, partición, tabla, clúster, job, columna, fila.
- Nombres de productos tal como los escribe la documentación vigente (mayúsculas incluidas). Si un producto cambió de nombre, usa el actual y verifícalo (`VERIFICAR:` en `post.md`).
- Si una palabra es ambigua, acláralo. Ej. una "task" de un Job de Databricks no es lo mismo que una tarea de Spark.

### 3. Primero el mecanismo, después la solución

- La lámina del problema explica *por qué* pasa, con un visual, no solo cómo se llama (ej. el skew existe porque el shuffle junta en una partición todas las filas de la misma key).
- Cada arreglo dice en una frase por qué funciona antes de mostrar cómo se hace.

### 4. Técnicas poco conocidas: dos láminas, con un ejemplo de verdad

Para técnicas que la mayoría no ha usado (salting, SCD Tipo 2, MERGE con varias condiciones, bucketing, watermarks, Z-order...):

- **Lámina de la idea, sin código**: un ejemplo con filas reales en mini tablas (`mini_table()` del Día 04), en pasos numerados (1, 2, 3), y una línea final con el resultado: "Antes: ... Ahora: ...".
- **Lámina del código**: los mismos pasos con el mismo número, cada uno con una frase que explica la función menos obvia (ej. "`rand()` da un número entre 0 y 1", "`explode` convierte la lista en filas") y al final el costo o la advertencia.
- Los valores del código coinciden con los del ejemplo (si el ejemplo usa salts 0 a 3, el código usa `N = 4`).
- Las técnicas conocidas (filtrar nulos, activar una config) caben en una lámina, con una frase de por qué.

### 5. Código narrado

- Antes de cada bloque, una frase en español dice qué hace y por qué.
- En el snippet de la lámina, los comentarios van en español y narran los pasos (`# Grande: cada fila recibe un salt al azar`). `example.py` sigue en inglés.
- Nada de variables auxiliares ni atajos que no aporten (ej. `conf = spark.conf`). El código de la lámina se escribe para leerse, no para ahorrar caracteres.
- Nombres de ejemplo que se entiendan solos: `big`, `small`, `events`, `customer_id`.

### 6. Visuales que explican

- Antes / Después cuando una técnica transforma datos (ej. `ANTES: A · 1 tarea con todo` → `DESPUÉS: A·0 A·1 A·2 A·3`).
- Diagramas con nombres nativos en las cajas (`EXECUTOR 1`, no "Máquina 1") y contenido rotulado ("copia de small").
- Datos ilustrativos marcados como `Ilustrativo`.

### Prueba final por lámina

¿Alguien que sabe SQL pero no conoce el término entendería qué pasa, por qué pasa y por qué le importa? Si no, falta una definición, un ejemplo o un visual.

Referencia: `days/day04_data_skew/build.py`. Láminas 2 y 3 (definiciones), 4 (arreglos con su porqué), 5 (diagrama con executors), 6 y 7 (técnica poco conocida en dos láminas). Helpers `defs()` y `mini_table()`.

---

## 5. Anti-"parece hecho con IA" (obligatorio)

**Prohibido** en las piezas visuales:
- Emojis dentro de las láminas.
- Degradados de fondo, glow, sombras grandes, glassmorphism.
- Tarjetas redondeadas con sombra en cuadrícula (el look de "feature grid").
- Morados, rosados, naranjas o cualquier color fuera de la sección 3.
- Iconos genéricos (cohetes, bombillos, cerebros, robots).
- Más de una idea por lámina, o párrafos de más de 3 líneas.
- Fotos de stock o imágenes de personas.

**Sí**:
- Diseño plano, líneas finas (2 px), esquinas de 0 a 6 px.
- Visuales hechos para el tema: barras con datos, maquetas de la Spark UI, diagramas de particiones o nodos dibujados con divs o SVG.
- Números grandes en Montserrat 900 para listas (`01`, `02`, `03`).
- Una textura de ruido sutil (ya incluida en `theme.css`).
- Datos ilustrativos marcados como `Ilustrativo` en la lámina.

---

## 6. Copy del post (texto de LinkedIn)

Idioma: **español neutro**, tuteo, tono de colega senior (directo y sin exagerar).

Estructura (basada en posts de creadores grandes de Data, ej. Zach Wilson; ver "Por qué" abajo):
1. **Hook en la primera línea, sin etiqueta de serie**: el problema, un dato o una afirmación concreta, en máximo ~140 caracteres para que se vea completo en móvil antes del "ver más". Mejor si coincide con el titular de la portada (ej. "¿Tu job lleva una hora esperando por UNA sola tarea?"). En "Pregunta de entrevista", el hook es la pregunta entre comillas.
2. **Re-hook** (segunda línea, después de una línea en blanco): qué va a obtener quien siga leyendo (ej. "Casi siempre es data skew, y se arregla con 4 cambios. De menos a más esfuerzo 👇").
3. **Cuerpo**: el porqué técnico en 2 a 3 frases cortas, con una línea en blanco entre bloques. Bloques de 1 a 2 líneas.
4. **Listas** con números simples (`1.` `2.` `3.`) y el formato `Término → explicación corta`. Sin emojis como viñetas (nada de `✅` ni `1️⃣`). Cada lista va precedida de una frase que termina en dos puntos.
5. **Experiencia propia**: una línea con `[TU ANÉCDOTA: ...]` para que Mateo la complete o la borre. Los posts personales son los que más reacciones tienen.
6. **Sin código en el copy**: LinkedIn no muestra el código en monoespaciado y se ve mal. El código va en las láminas y en el repo. Como mucho, una config o un comando de una línea dentro de una frase.
7. **Pregunta final** que pida una experiencia concreta, no un "¿qué opinas?". Se mantiene porque los comentarios pesan en el algoritmo.
8. **CTA**: compartir (`Si le sirve a alguien de tu equipo, compártelo ♻️`) y la etiqueta de la serie al final: `Día N/100 de Pythonic Data Engineering. Sígueme para el Día N+1: <tema>.` En los guardables, además, `Guarda este post`.
9. **Hashtags**: máximo 3, siempre incluyendo `#100DaysOfPythonicEngineering`.

Reglas:
- **Ningún link en el cuerpo del post.** La documentación oficial y el repo van en el **primer comentario**.
- Emojis solo en el copy (no en las láminas): **máximo 3 en todo el post**, solo en el re-hook, las advertencias (`⚠️`) o el CTA. Como máximo uno por línea.
- Entre 700 y 2,000 caracteres.
- Nunca inventes anécdotas, cifras o experiencias de Mateo. Si el post necesita una, deja `[TU ANÉCDOTA: ...]`.
- Nunca menciones clientes, empresas ni datos de proyectos reales.
- **Claridad también en el copy**: la primera vez que aparece un término técnico clave, defínelo en pocas palabras entre paréntesis o en la misma frase (ej. "AQE (Adaptive Query Execution): Spark divide sola las particiones gigantes"). Mismo vocabulario nativo que las láminas (sección 4.1).

**Por qué este formato** (revisión del 19 nov 2026): se analizaron posts públicos de Zach Wilson y de una creadora de Data con 83k seguidores. Patrones: hook directo sin etiquetas, listas numeradas `Término → explicación`, entre 0 y 3 emojis, 0 o 1 hashtag, sin código en el cuerpo, y los posts personales con más reacciones. La muestra es pequeña (4 posts): se valida con la tabla de Métricas en la revisión del Día 08.

**Cuándo publicar** (decidido por Mateo el 19 nov 2026; ajustar con las métricas propias):
- **3 posts por semana** (hora Colombia; CDMX una hora menos): **lunes 11:00 a.m.** la noticia de "Databricks esta semana" (sección 12), y **martes y jueves 9:00 a.m.** la serie de los 100 días. No más de 2 posts de la serie por semana.
- Los dos días están en la mejor ventana de los estudios (martes a jueves por la mañana) y separados por un día, para que un post no le quite alcance al otro.
- Evitar fines de semana y festivos (ej. 8 de diciembre en Colombia; 24, 25 y 31 de diciembre, y 1 de enero): ese día se salta al siguiente martes o jueves.
- Anotar día y hora real de cada post en la tabla de Métricas del README para comparar después.

**Formato de `post.md`**:
1. `# Día NN: <tema>`
2. Tabla de metadatos: Nivel, Tipo de post, Paleta, Formato visual, **Estado**, **Link**.
3. `## Estructura visual` (guion de láminas del plan V3).
4. `## Hook alternativo`.
5. `## Antes de publicar`: checklist `- [ ]` con los `VERIFICAR:` y avisos (ej. longitud del copy fuera de rango).
6. `## Post (copiar y pegar)`: bloque ```` ```text ```` exacto para LinkedIn.
7. `## Primer comentario`: documentación oficial + repo.

Los posts de los días 04 a 15 vienen tal cual del plan V3. Si se edita un snippet del copy, mantenerlo alineado con `example.py`.

---

## 7. Estándares de código (scripts y snippets)

- **Python**: nombres en inglés, tipado completo en parámetros y retorno, docstrings estilo Google en funciones públicas, PEP 8 / `black` (88 a 100 caracteres), nada de `except:` genérico, imports agrupados (stdlib, terceros, locales).
- **PySpark**: `import pyspark.sql.functions as F`; evitar `.collect()` innecesarios; transformaciones encadenadas.
- **Snippets en las láminas**: pueden omitir imports y tipos por espacio, pero el script completo en `days/dayNN_slug/example.py` debe cumplir todo lo anterior y ejecutarse.
- **Verificación técnica**: toda función o configuración de Databricks, Spark o Azure se contrasta con la documentación oficial vigente antes de publicar. Si algo no se pudo verificar, se marca en `post.md` como `VERIFICAR:`.
- **Verificación local**: `python3 -m py_compile days/*/example.py`. En esta máquina no hay Spark, Databricks ni Azure: el código PySpark, Azure y SQL se marca para probar en el workspace de Mateo (ej. los 3 casos de prueba de `day09_scd2_merge/example.sql`). Los días de solo SQL usan `example.sql`.
- `day10_generators_yield/example.py` sí corre en local y da los datos reales de la gráfica de memoria (`python3 example.py 300000` → ~18.5 MB vs ~0.17 MB de pico).

---

## 8. Estructura del repo

```
CLAUDE.md
README.md                       # tabla de seguimiento + "Dónde vamos" (fuente de verdad del avance)
ideas.md                        # banco de temas de reserva (plan V2), columna "Usado"
design/
  theme.css                     # paletas + componentes (fuente de verdad visual)
  fonts/                        # woff2 de Montserrat, Roboto y Roboto Mono (OFL)
days/
  day04_data_skew/              # EJEMPLO DE REFERENCIA
    build.py                    # genera el HTML de las láminas
    post.md                     # copy + primer comentario
    example.py                  # script ejecutable del tema (example.sql en días de solo SQL)
    day04_data_skew.pdf         # carrusel final
    preview/                    # PNG de cada lámina
  day01_* a day03_*             # publicados antes del repo: solo post.md con link y TODO
scripts/
  render.sh                     # build.py -> HTML -> PDF -> PNG
  preview_pdf.swift             # PDF -> PNG en macOS cuando no hay pdftoppm
docs/
  Plan_Maestro_V3_100_Days_of_Pythonic_Engineering.docx
```

Render: `scripts/render.sh days/day04_data_skew pino` (requiere Chrome/Chromium; para los PNG usa `pdftoppm` de Poppler y, si no está, `scripts/preview_pdf.swift`, que genera los mismos `preview/slide-N.png`).

---

## 9. Seguimiento

La tabla vive en **`README.md`** (una sola fuente de verdad), con dos tablas:
- **Seguimiento**: Día, Tema, Tipo de post, Formato, **Archivo que se sube** (PDF de N láminas, PNG imagen única o Texto, con link al archivo cuando existe), Estado, **Publicado** (fecha) y Link, más la línea "Dónde vamos". Nivel y paleta están en el `post.md` de cada día.
- **Métricas**: impresiones, guardados, comentarios y reacciones por post, para la revisión del Día 08.

Estados: `⏳ Pendiente` → `🎨 Listo` (archivo renderizado y revisado) → `✅ Publicado`.

- **Visual terminado**: estado `🎨 Listo` en el README y `Listo (dayNN_slug.pdf)` en la tabla de `post.md`. Actualizar "Siguiente".
- **"Ya salió el Día X"** (con o sin link):
  1. `README.md`: estado `✅ Publicado`, fecha en "Publicado", Link `[post](<url>)`, y agregar la fila del día a la tabla de Métricas. Actualizar "Último publicado" y "Siguiente".
  2. `days/dayNN_slug/post.md`: filas Estado y Link.
  3. Commit `Day NN: published`.
- **Días 01 a 03**: publicados antes del repo, con paleta "(antiguo)". Falta el texto publicado y el código: pedírselos a Mateo.
- **Días nuevos (16+)**: crear `days/dayNN_slug/` con `post.md` en el formato de la sección 6, agregar la fila al README y marcar en `ideas.md` el tema usado.
- **Visual terminado** también actualiza la columna "Archivo que se sube" con el formato real y el número de láminas (ej. `PDF, 8 láminas`).
- **Revisión de métricas**: después del Día 08 (5 posts del plan V3), pedir a Mateo los números de la tabla de Métricas (guardados y comentarios sobre todo) y proponer ajustes al calendario.

Los temas del Día 16 en adelante los propone Claude siguiendo la rotación de la sección 2, priorizando lo que tenga más guardados y comentarios en los posts anteriores. Mateo aprueba la lista antes de producir.

---

## 10. Checklist antes de entregar

- [ ] El tipo de post y la paleta coinciden con la tabla de la sección 2.
- [ ] Ningún color fuera de `theme.css`; un solo resaltado por titular.
- [ ] Portada oscura con un visual; cierre oscuro con pregunta, `GUARDA`, `DÍA NN+1` y `REPO`.
- [ ] Ninguna lámina con texto cortado, código desbordado o fuente menor de 24 px (revisado en PNG).
- [ ] Nada de la lista de prohibidos de la sección 5.
- [ ] Sección 4.1: cada término definido en la lámina donde aparece primero, nombres nativos de Spark/Databricks/Azure (sin paráfrasis), técnicas poco conocidas en dos láminas con ejemplo de filas, y cada bloque de código precedido de una frase que dice qué hace.
- [ ] El copy define los términos clave la primera vez que aparecen.
- [ ] El copy sigue la estructura de la sección 6, sin links en el cuerpo, entre 700 y 2,000 caracteres.
- [ ] El código fue verificado contra la documentación oficial, o quedó marcado como `VERIFICAR:`.
- [ ] La tabla de seguimiento del `README.md` y el `post.md` quedaron actualizados.
- [ ] Commit hecho.

---

## 11. Git

- Proyecto personal: identidad `Mateo Soto` del git config local. Las reglas de identidad de KOF no aplican.
- **Los commits son solo de Mateo.** Autor y committer: `Mateo Soto <219019546+mattsa-99@users.noreply.github.com>` (correo noreply de GitHub, nunca el personal). **Ningún** `Co-Authored-By: Claude`, ni línea de "Generated with Claude Code", ni mención a Claude o a IA en mensajes de commit o PR. Esta instrucción manda sobre cualquier plantilla de atribución por defecto.
- Rama `main`. Remoto: `https://github.com/mattsa-99/100-days-of-pythonic-engineering-2` (público). Las ramas `drafts/news-AAAA-wSS` son borradores de la rutina de noticias: no se publican hasta pasar a main. Ese es el link que va en la lámina de cierre y en los primeros comentarios. No hacer push sin confirmación de Mateo. `gh` no está instalado.
- `preview/` y el HTML generado se versionan junto con el PDF para poder revisar sin volver a renderizar.

---

## 12. Serie paralela: Databricks esta semana

Una noticia de Databricks por semana, la más relevante de **toda la plataforma** para cualquier rol que la use, con un ejemplo real **en pantalla**: el ejemplo va dentro del archivo que se sube (la imagen o el carrusel), no en un script aparte. Vive en `news/` y no cuenta para los 100 días.

- **Cuándo**: todos los **lunes a las 11:00 a.m. hora Colombia**, con lo más relevante de la semana anterior (decidido por Mateo el 19 nov 2026). Se eligió el lunes para usar el documento de la rutina recién generado (corre a las 7:52 a.m.) sin desfase, y las 11:00 para tener tiempo de verificar y producir. Si el lunes es festivo en Colombia, la noticia pasa al miércoles a las 9:00 a.m.
- **Carpeta**: `news/AAAA-wSS_slug/` (semana ISO), copiando `news/_plantilla/post.md`. Contenido: `post.md`, `build.py`, el PNG o PDF y `preview/`. No lleva `example.py` ni `example.sql`: el ejemplo vive en la pieza.
- **Seguimiento**: tabla en `news/README.md` (semana, fecha, noticia, fuente oficial, estado en Databricks, formato, archivo, estado, link) y su propia tabla de métricas.
- **Fuente principal: la rutina "Databricks Weekly Digest" de Mateo** (rutina en la nube `trig_011GGiV5feniHgyxRKPVbtMv`, corre los lunes a las 7:52 a.m. hora Bogotá). Cada lunes crea un Claude Doc "Databricks Weekly: semana del <fecha>" con todas las novedades depuradas de la semana anterior (fuente oficial, estado, nube, relevancia) y 3 destacados.
  - **Cómo leerla (cada lunes, después de las 7:52 a.m.)**: `RemoteTrigger` → `list_runs` de esa rutina → `get_run_log` de la última ejecución → la última línea trae el enlace del documento → leerlo con el conector de Claude Docs (cargar antes el skill `docs`).
  - **Si la rutina falló o no hay documento ese lunes**: hacer la búsqueda equivalente en las release notes oficiales de la semana anterior (Azure Databricks y docs.databricks.com) y el blog oficial, con las mismas reglas de precisión. Si no da el tiempo para las 11:00, se publica el miércoles a las 9:00 a.m.
  - **No modificar la rutina**: es un entregable del trabajo de Mateo (comunidad de Databricks de Wizeline). Su horario, plantilla y correo no se tocan desde este repo.
  - **Separación trabajo / marca personal**: de la rutina solo se toman las novedades públicas con su enlace oficial. Nunca se menciona Wizeline ni KOF, ni se reutilizan sus entregables (decks, memes, flyers con estilo Wizeline). Su puntaje de relevancia está pensado para ese equipo de ingeniería: para LinkedIn se vuelve a evaluar con el criterio de abajo, que abarca a todos los roles.
- **Borrador automático: rutina "LinkedIn · Borrador noticia Databricks"** (`trig_01AghBRPJYP2B9qSqJrLkg7Z`, lunes 8:15 a.m. hora Bogotá, Opus 5.5, conectores Gmail y Claude-Docs). Busca el correo del digest, lee el documento, elige y verifica la noticia, crea `news/AAAA-wSS_slug/` (post.md, build.py, PNG con el ejemplo en pantalla), la sube a la rama `drafts/news-AAAA-wSS` (nunca a main) y manda un correo a Mateo con la lámina y el copy.
  - **Después de la revisión de Mateo**: traer la rama, aplicar sus cambios, pasarla a main (merge o cherry-pick, sin trailers de Claude), borrar la rama de borrador y actualizar `news/README.md`.
  - La rutina se edita en https://claude.ai/code/routines/trig_01AghBRPJYP2B9qSqJrLkg7Z. Su prompt remite a este CLAUDE.md, así que las reglas de diseño y copy se cambian aquí, no en la rutina.
- **Cómo elegir la noticia**: revisar lo publicado esa semana en fuentes oficiales (blog de Databricks, release notes de la plataforma, documentación). Elegir la de mayor impacto en **toda la plataforma**, para cualquier rol: Data Engineering (Lakeflow, Delta, jobs), análisis y BI (Databricks SQL, AI/BI, Genie), ciencia de datos, ML e IA generativa (Mosaic AI, model serving, agentes), gobierno y seguridad (Unity Catalog), costos y administración. Criterios, en este orden: (1) a cuánta gente le cambia el día a día, (2) que se pueda probar ya (GA o Public Preview por encima de Beta privada), (3) que se pueda mostrar con un ejemplo real en la lámina. Anotar en `post.md` por qué se eligió, para qué rol es y qué se descartó.
  - En el copy y en la lámina, decir para qué rol es la noticia (ej. `PARA ANALISTAS`, `PARA ML ENGINEERS`) y definir los términos de ese mundo con la sección 4.1, porque la audiencia de Mateo es sobre todo de Data Engineering.
  - Hashtags según el rol (ej. `#Databricks #GenAI` o `#Databricks #BusinessIntelligence`), siempre con `#Databricks`. Nunca usar como fuente única un post de terceros.
- **Precisión (obligatorio)**:
  - Indicar siempre el estado oficial (`Public Preview`, `GA`, `Beta`) y las nubes donde está disponible. Si no está claro en la fuente, no se afirma.
  - El ejemplo de la lámina se contrasta con la documentación oficial (sintaxis, nombres, parámetros) o se prueba en un workspace. Mientras no, queda `VERIFICAR:` en `post.md`.
  - Nombres de productos exactamente como los escribe Databricks en la fuente (sección 4.1).
- **Formato**: imagen única (PNG) o carrusel corto (PDF, 4 o 5 láminas), con las reglas de diseño (secciones 3 a 5) y de claridad (4.1).
  - Paleta fija `medianoche`, para que la serie se reconozca.
  - **El ejemplo real va en pantalla, siempre.** Es el centro de la pieza: un caso concreto con nombres que se entienden solos (tablas, columnas, valores), en la forma que mejor muestre la novedad: snippet de código o SQL narrado (sección 4.1), configuración o UI recreada, o un antes / después con filas en `mini_table()`. Debe responder "¿cómo se ve esto en mi trabajo?" sin abrir otro archivo.
  - Imagen única: el ejemplo ocupa al menos un tercio de la lámina. Carrusel: tiene su propia lámina ("Ejemplo real"), y si el código es largo, una lámina con el caso en filas y otra con el código (sección 4.1, técnicas poco conocidas).
  - Cabecera: `DATABRICKS ESTA SEMANA · SEMANA SS` en lugar de `PYTHONIC ENGINEERING · DÍA NN / 100` (en `build.py`: `SERIES = "Databricks esta semana"` y la etiqueta del día cambiada por la semana). Píldora de nivel igual que en la serie.
  - Cierre: `GUARDA`, `PRÓXIMA SEMANA` y `REPO`.
- **Copy**: misma estructura de la sección 6. La etiqueta final es `Databricks esta semana · Semana SS` y el CTA invita a seguir la serie de los 100 días.
