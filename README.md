# 100 Days of Pythonic Engineering

Serie de LinkedIn de **Mateo Soto** sobre Data Engineering con Python, Spark, Databricks y Azure, en español.
Cada día tiene su carpeta en [`days/`](days/) con el post listo para copiar, el código del tema y el carrusel.

> Plan base: [Plan Maestro V3](docs/Plan_Maestro_V3_100_Days_of_Pythonic_Engineering.docx). Reglas de diseño, copy y código: [CLAUDE.md](CLAUDE.md). Temas de reserva: [ideas.md](ideas.md).

## Dónde vamos

**Ritmo:** 2 posts por semana, martes y jueves a las 9:00 a.m. hora Colombia.

**Último publicado:** Día 03 · **Siguiente:** Día 04 (Data Skew, PDF de 8 láminas listo en [`days/day04_data_skew/`](days/day04_data_skew/))

## Tabla de seguimiento

| Día | Tema | Tipo de post | Formato | Archivo que se sube | Estado | Publicado | Link |
|---|---|---|---|---|---|---|---|
| 01 | [UDFs: jerarquía del rendimiento](days/day01_udf_performance/) | Errores | Post de texto + reto | Texto | ✅ Publicado | antes del repo | [post](https://lnkd.in/p/eJkNmXQK) |
| 02 | [dbutils.jobs.taskValues entre tareas](days/day02_task_values/) | Errores | Post de texto + debate | Texto | ✅ Publicado | antes del repo | [post](https://lnkd.in/p/eRmBhjUh) |
| 03 | [Broadcast Join vs Shuffle Join](days/day03_broadcast_join/) | Errores | Post de texto | Texto | ✅ Publicado | antes del repo | [post](https://lnkd.in/p/emV3d4gM) |
| 04 | [Data Skew en Spark](days/day04_data_skew/) | Errores que cuestan plata | Carrusel | PDF, 8 láminas: [`day04_data_skew.pdf`](days/day04_data_skew/day04_data_skew.pdf) | 🎨 Listo | — | — |
| 05 | [repartition() vs coalesce()](days/day05_repartition_vs_coalesce/) | Pregunta de entrevista | Carrusel | PDF (por hacer) | ⏳ Pendiente | — | — |
| 06 | [ZORDER vs Liquid Clustering](days/day06_zorder_vs_liquid_clustering/) | Opinión / Debate | Infografía | GIF animado, se sube como foto (por hacer) | ⏳ Pendiente | — | — |
| 07 | [Medallion: 5 errores comunes](days/day07_medallion_mistakes/) | Arquitectura en una imagen | Infografía | GIF animado, se sube como foto (por hacer) | ⏳ Pendiente | — | — |
| 08 | [Auto Loader vs COPY INTO](days/day08_auto_loader_vs_copy_into/) | Errores que cuestan plata | Infografía | GIF animado, se sube como foto (por hacer) | ⏳ Pendiente | — | — |
| 09 | [SCD Tipo 2 con MERGE](days/day09_scd2_merge/) | Arquitectura en una imagen | Carrusel | PDF (por hacer) | ⏳ Pendiente | — | — |
| 10 | [Generadores y yield](days/day10_generators_yield/) | Antes vs. Después | Carrusel corto / imagen | PDF o PNG (por decidir) | ⏳ Pendiente | — | — |
| 11 | [5 checks de calidad antes de Silver](days/day11_data_quality_checks/) | Guardable | Carrusel | PDF (por hacer) | ⏳ Pendiente | — | — |
| 12 | [DefaultAzureCredential](days/day12_default_azure_credential/) | Errores que cuestan plata | Carrusel corto / imagen | PDF o PNG (por decidir) | ⏳ Pendiente | — | — |
| 13 | [Senior vs Junior](days/day13_senior_vs_junior/) | Opinión / Debate | Texto largo + 1 imagen | Texto + PNG imagen única (por hacer) | ⏳ Pendiente | — | — |
| 14 | [Unity Catalog](days/day14_unity_catalog/) | Pregunta de entrevista | Carrusel | PDF (por hacer) | ⏳ Pendiente | — | — |
| 15 | [Roadmap Data Engineer 2026](days/day15_roadmap_2026/) | Guardable | Carrusel | PDF (por hacer) | ⏳ Pendiente | — | — |

Estados: ⏳ Pendiente → 🎨 Listo (archivo renderizado y revisado) → ✅ Publicado.
Nivel y paleta de cada día están en su `post.md`.

## Métricas

Se llena unos días después de publicar (LinkedIn → "Ver analíticas"). Sirve para la revisión del Día 08: ¿qué tipo de post y qué formato generan más guardados y comentarios?

| Día | Tipo de post | Formato | Publicado (día y hora) | Impresiones | Guardados | Comentarios | Reacciones | Notas |
|---|---|---|---|---|---|---|---|---|
| 01 | Errores | Texto | | | | | | |
| 02 | Errores | Texto | | | | | | |
| 03 | Errores | Texto | | | | | | |

## Estructura del repo

```
CLAUDE.md                     # reglas de diseño, copy, código y flujo (leer primero)
design/theme.css              # 3 paletas + componentes (fuente de verdad visual)
design/fonts/                 # Montserrat, Roboto, Roboto Mono (OFL), embebidas en el HTML
days/dayNN_slug/
├── post.md                   # metadatos, checklist, copy y primer comentario
├── example.py | example.sql  # script completo del tema
├── build.py                  # genera el HTML de las láminas (días con carrusel)
├── dayNN_slug.pdf            # carrusel final
└── preview/slide-N.png       # PNG de cada lámina para revisión
scripts/render.sh             # build.py → HTML → PDF → PNG
scripts/preview_pdf.swift     # PDF → PNG en macOS cuando no hay pdftoppm
docs/                         # Plan Maestro V3
```

Render: `scripts/render.sh days/day04_data_skew pino`

## Revisión de métricas

Después del Día 08 (5 posts del plan V3): comparar guardados y comentarios por tipo de post y ajustar el calendario.
