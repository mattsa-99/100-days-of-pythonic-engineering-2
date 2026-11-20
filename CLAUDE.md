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
- Cabecera: `DÍA NN / 100` a la izquierda y la píldora de nivel (`BÁSICO`, `INTERMEDIO`, `AVANZADO`) a la derecha, con una línea fina debajo.
- Kicker de 1 a 3 palabras (ej. `ARREGLO 3`), titular y contenido.
- Pie: `Mateo Soto` a la izquierda y `NN / TT` en Roboto Mono a la derecha.
- Barra de progreso segmentada en el borde inferior.
- `DESLIZA →` en todas las láminas menos la última.

**Estructura del carrusel** (de 5 a 8 láminas):
1. **Portada (oscura)**: hook en forma de problema concreto y un visual que lo demuestre (gráfico, diagrama). Nada de portadas solo con texto.
2. **El problema**: qué es, explicado en una frase y un visual.
3. a N-1. **Contenido**: una idea por lámina; si hay código, como máximo 8 líneas por lámina.
N. **Cierre (oscuro)**: pregunta para comentar y tres filas con etiquetas `GUARDA`, `DÍA NN+1` y `REPO`.

**Formatos alternativos**:
- Imagen única: el mismo lienzo y la misma cabecera y pie, sin barra de progreso ni "Desliza".
- Infografía animada (opcional): mismas paletas y fuentes; las animaciones solo se permiten en líneas conectoras (`stroke-dashoffset`).
- "Ventana macOS" del plan V3 (días 10 y 12): se resuelve como carrusel corto Antes/Después con bloques `.code` del tema, sin los tres puntos de ventana ni sombras.

**Límites prácticos para que nada se desborde** (aprendidos al renderizar):
- Código a 29 px dentro de `.code`: máximo unos 48 caracteres por línea; a 26 px, unos 54. Parte las líneas largas en lugar de bajar de 26 px.
- Como máximo 2 bloques de código por lámina.

---

## 4.1 Accesible para todos (obligatorio)

Los temas pueden ser avanzados, pero el carrusel debe entenderlo alguien que sabe SQL y nunca ha usado Spark. Sin agregar láminas:

- **Glosario en línea**: todo término técnico (partición, shuffle, AQE, broadcast, spill...) se define en lenguaje simple, en máximo ~15 palabras, **en la lámina donde aparece por primera vez**, aunque el copy también lo explique. La redundancia es intencional: mucha gente solo ve las láminas.
  - Con el componente `.defs` / `.def` de `theme.css` (término + definición), o dentro del lead o de una línea `.why`.
  - Máximo 2 definiciones por lámina. Si hacen falta más, la lámina tiene demasiadas ideas.
- **Terminología nativa de Spark**: usa el nombre que aparece en la Spark UI, la documentación o el código, y defínelo una vez. Nunca inventes paráfrasis.
  - Sí: `executor`, `key` (y "key caliente"), `shuffle`, `stage`, `broadcast`, `spill`, `driver`.
  - No: "máquina", "llave", "clave", "nodo" usado como sinónimo de executor.
  - Se mantienen en español las traducciones directas que todos reconocen: tarea, partición, tabla, clúster, job.
  - Ordena las láminas para que un término no aparezca antes de la lámina que lo define.
- **Primero el mecanismo, después el código**: la lámina del problema explica *por qué* pasa (ej. el skew existe porque el shuffle junta las filas de la misma llave), con un visual y no solo el nombre del problema.
- **Código narrado**:
  - Antes de cada bloque, una frase en español dice qué hace y por qué.
  - En el snippet de la lámina, los comentarios van en español y narran los pasos (`# Grande: cada fila recibe una sal`). `example.py` sigue en inglés.
  - Nada de variables auxiliares que no aporten (ej. `conf = spark.conf`).
- **Técnicas poco conocidas (salting, SCD2, MERGE, bucketing...)**: dos láminas en vez de una.
  - Lámina de la idea: un ejemplo con filas reales en mini tablas (ver `mini_table()` del Día 04), en pasos numerados y con el resultado ("Antes: ... Ahora: ..."). Sin código.
  - Lámina del código: los mismos pasos numerados, cada uno con una frase de qué hace la función menos obvia (ej. `rand()`, `explode`). Usa los mismos valores que el ejemplo (si el ejemplo tiene salts 0 a 3, `N = 4`).
- **Antes / Después** cuando una técnica transforma datos (ej. `ANTES: A · 1 tarea` → `DESPUÉS: A_0 A_1 A_2 A_3`).
- **Prueba final por lámina**: ¿alguien que no conoce el término entendería qué pasa y por qué importa? Si no, falta una definición o un visual.

Referencia: `days/day04_data_skew/build.py` (láminas 2, 3, 4 y 6) y su helper `defs()`.

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

Estructura:
1. **Primera línea**: `<emoji> Día N/100: Pythonic Data Engineering | <Tema>` (en "Pregunta de entrevista" se usa `🎯 Día N/100: Pregunta de entrevista | <Tema>`).
2. **Hook**: una pregunta o un error común en una línea (ej. "¿Tu job lleva una hora esperando por UNA sola tarea?").
3. **Cuerpo**: el porqué técnico en 2 a 3 frases y después una lista con `✅` o `1️⃣ 2️⃣ 3️⃣`. Las advertencias van con `⚠️`.
4. **Código** (opcional): máximo 10 líneas.
5. **Pregunta final** que pida una experiencia concreta, no un "¿qué opinas?".
6. **CTA**: `Sígueme para el Día N+1/100 📌`; en los guardables, además, `Guarda este post 📌`.
7. **Hashtags**: de 4 a 6, siempre incluyendo `#100DaysOfPythonicEngineering`.

Reglas:
- **Ningún link en el cuerpo del post.** La documentación oficial y el repo van en el **primer comentario**.
- Emojis solo en el copy (no en las láminas), y con moderación: como máximo uno por línea.
- Entre 700 y 2,000 caracteres.
- Nunca inventes anécdotas, cifras o experiencias de Mateo. Si el post necesita una, deja `[TU ANÉCDOTA: ...]`.
- Nunca menciones clientes, empresas ni datos de proyectos reales.

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

La tabla vive en **`README.md`** (una sola fuente de verdad) con columnas Día, Nivel, Tema, Tipo, Paleta, Formato, Estado y Link, más la línea "Dónde vamos".

Estados: `⏳ Pendiente` → `🎨 Listo` (visual renderizado y revisado) → `✅ Publicado`.

- **Visual terminado**: estado `🎨 Listo` en el README y `Listo (dayNN_slug.pdf)` en la tabla de `post.md`. Actualizar "Siguiente".
- **"Ya salió el Día X"** (con o sin link):
  1. `README.md`: estado `✅ Publicado`, Link `[post](<url>)`, actualizar "Último publicado" y "Siguiente".
  2. `days/dayNN_slug/post.md`: filas Estado y Link.
  3. Commit `Day NN: published`.
- **Días 01 a 03**: publicados antes del repo, con paleta "(antiguo)". Falta el texto publicado y el código: pedírselos a Mateo.
- **Días nuevos (16+)**: crear `days/dayNN_slug/` con `post.md` en el formato de la sección 6, agregar la fila al README y marcar en `ideas.md` el tema usado.
- **Revisión de métricas**: después del Día 08 (5 posts del plan V3), pedir guardados y comentarios por post y proponer ajustes.

Los temas del Día 16 en adelante los propone Claude siguiendo la rotación de la sección 2, priorizando lo que tenga más guardados y comentarios en los posts anteriores. Mateo aprueba la lista antes de producir.

---

## 10. Checklist antes de entregar

- [ ] El tipo de post y la paleta coinciden con la tabla de la sección 2.
- [ ] Ningún color fuera de `theme.css`; un solo resaltado por titular.
- [ ] Portada oscura con un visual; cierre oscuro con pregunta, `GUARDA`, `DÍA NN+1` y `REPO`.
- [ ] Ninguna lámina con texto cortado, código desbordado o fuente menor de 24 px (revisado en PNG).
- [ ] Nada de la lista de prohibidos de la sección 5.
- [ ] Cada término técnico está definido en la lámina donde aparece por primera vez, y cada bloque de código va precedido de una frase que dice qué hace (sección 4.1).
- [ ] El copy sigue la estructura de la sección 6, sin links en el cuerpo, entre 700 y 2,000 caracteres.
- [ ] El código fue verificado contra la documentación oficial, o quedó marcado como `VERIFICAR:`.
- [ ] La tabla de seguimiento del `README.md` y el `post.md` quedaron actualizados.
- [ ] Commit hecho.

---

## 11. Git

- Proyecto personal: identidad `Mateo Soto` del git config local. Las reglas de identidad de KOF no aplican.
- Rama `main`. Remoto planeado: `github.com/mateosotoa/100-days-of-pythonic-engineering` (el link que ya sale en los primeros comentarios y en la lámina de cierre), todavía sin crear. No hacer push sin confirmación de Mateo. `gh` no está instalado.
- `preview/` y el HTML generado se versionan junto con el PDF para poder revisar sin volver a renderizar.
