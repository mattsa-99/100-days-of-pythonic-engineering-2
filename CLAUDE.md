# 100 Days of Pythonic Engineering: guía del repo

Serie de LinkedIn en español sobre Data Engineering (Python, Spark, Databricks, Azure).
Plan base: *Plan Maestro V3* (19 nov 2026), en `../Plan_Maestro_V3_100_Days_of_Pythonic_Engineering.docx`.

## Estructura

```
README.md                  # tabla de seguimiento + "📍 Dónde vamos" (fuente de verdad del avance)
ideas.md                   # banco de temas de reserva (plan V2), columna "Usado"
days/day_XX_<slug>/
├── post.md                # metadatos, checklist, post y primer comentario
├── *.py / *.sql           # versión completa del snippet del post
└── carousel/              # solo días con carrusel: carousel.html + day_XX_<slug>.pdf
tools/render_carousel.sh   # HTML → PDF con Chrome headless
tools/preview_pdf.swift    # PDF → PNG por página, para revisar el resultado
```

- Días 01–03: publicados antes del repo. `post.md` solo tiene el link y un TODO: falta el texto publicado y el código (pedírselo al usuario).
- Días 04–15: `post.md` sacado tal cual del plan V3. Si se edita un post, mantener el snippet alineado con el archivo de código de la carpeta.

## Formato de `post.md`

1. `# Día XX: <tema>`
2. Tabla de metadatos: Nivel, Tipo de post, Formato visual, **Estado**, **Link**.
3. `## Estructura visual` (láminas o partes de la pieza visual).
4. `## Hook alternativo` (cita).
5. `## Antes de publicar`: checklist `- [ ]`. Los días 06, 08, 09 y 14 tienen puntos marcados como VERIFICAR.
6. `## Post (copiar y pegar)`: bloque ```` ```text ```` exacto para LinkedIn.
7. `## Primer comentario`: documentación oficial + repo. Nunca links en el cuerpo del post.

Reglas del post: hook en la primera línea, pregunta final, CTA "Sígueme para el Día X/100" (y "Guarda este post" en los guardables), hashtag `#100DaysOfPythonicEngineering`.

## Llevar la cuenta

Estados: `⏳ Pendiente` → `🎨 Visual listo` → `✅ Publicado`.

- **Visual terminado:** estado `🎨 Visual listo` en la fila del README y en `post.md` (en `post.md` con la ruta del archivo, ej. `` 🎨 Visual listo (`carousel/day_04_data_skew.pdf`) ``). Actualizar "Siguiente" en "📍 Dónde vamos".
- **"Ya salió el Día X"** (con o sin link):
  1. `README.md`: estado `✅ Publicado`, Link `[post](<url>)`, actualizar "Último publicado" y "Siguiente".
  2. `days/day_XX_*/post.md`: filas Estado y Link.
  3. Commit `Day XX: published`.
- **Días 16+:** crear `days/day_XX_<slug>/post.md` con el formato de arriba, agregar la fila al README, rotar los 5 tipos de post y marcar en `ideas.md` el tema usado.
- **Revisión de métricas:** después del Día 08 (5 posts del plan V3), pedir guardados y comentarios por post y proponer ajustes al calendario.

## Carruseles PDF

- Un `<section class="slide">` por lámina, 1080x1350 px, `@page { size: 1080px 1350px; margin: 0; }`. 6 a 8 láminas.
- Partir de `days/day_04_data_skew/carousel/carousel.html` como plantilla. Sistema visual:
  - Fondo `#0b1220` con gradientes radiales azul/amarillo; paneles `#121b2e`, bordes `#23304a`.
  - Acentos: amarillo Python `#ffd43b`, azul `#4b8bbe`, rojo `#ff5d5d`, verde `#3ddc97`.
  - Fuentes: Inter (texto) y JetBrains Mono (código), vía Google Fonts.
  - Componentes: `.top` (tag + "N/7"), `.foot` ("Desliza →"), `.card`, `.badge` numerado, `.win` (ventana macOS con resaltado manual `.k .s .n .f .c`), `.callout`, `.split`.
  - Portada: pill con el tipo de post + título grande + "Día X/100". Cierre: resumen + pregunta + CTA del día siguiente.
- **Errores conocidos al renderizar:**
  - No usar `box-shadow`: Chrome lo pinta en el PDF como bandas oscuras.
  - Código a 29px: máximo ~48 caracteres por línea dentro de `.win`, si no se corta. Partir las líneas largas.
  - No más de 2 bloques de código + 2 tarjetas por lámina.
- **Generar y revisar:**
  ```bash
  tools/render_carousel.sh days/day_XX_*/carousel/carousel.html days/day_XX_*/carousel/day_XX_<slug>.pdf
  swift tools/preview_pdf.swift <pdf> <scratchpad>/png   # luego mirar cada PNG
  ```
  Debe dar las páginas esperadas y tamaño 810x1013 pt (= 1080x1350 px). Revisar cada lámina antes de dar el visual por listo.
- Otros formatos (infografía animada opciones A/B/C, ventana macOS opción D, post de texto) todavía no tienen plantilla en el repo. Al hacer el primero, documentarlo aquí.

## Código

- Python: nombres en inglés, tipado completo, docstrings Google con `Args:`/`Returns:`, PEP 8, imports en 3 bloques. SQL con comentarios en inglés.
- Sin datos, nombres ni detalles de clientes.
- Verificación local: `python3 -m py_compile days/*/*.py`. Aquí no hay Spark, Databricks ni Azure: el código PySpark, Azure y SQL se marca para probar en el workspace del usuario (ej. los 3 casos de prueba de `scd2_merge.sql`).
- `day_10_generators_yield/generators.py` corre localmente y da los números de la gráfica de memoria (`python3 generators.py 300000` → ~18.5 MB vs ~0.17 MB).

## Git

- Proyecto personal: identidad `Mateo Soto` del git config local. Las reglas de identidad de KOF no aplican.
- Rama `main`. Remoto planeado `github.com/mateosotoa/100-days-of-pythonic-engineering` (el link que ya sale en los primeros comentarios), todavía sin crear ni conectar. No hacer push sin confirmación del usuario. `gh` no está instalado.
