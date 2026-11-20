# 100 Days of Pythonic Engineering

Serie de LinkedIn de **Mateo Soto** sobre Data Engineering con Python, Spark, Databricks y Azure, en español.
Cada día tiene su carpeta en [`days/`](days/) con el post listo para copiar, el código del tema y el carrusel.

> Plan base: [Plan Maestro V3](docs/Plan_Maestro_V3_100_Days_of_Pythonic_Engineering.docx). Reglas de diseño, copy y código: [CLAUDE.md](CLAUDE.md). Temas de reserva: [ideas.md](ideas.md).

## Dónde vamos

**Último publicado:** Día 03 · **Siguiente:** Día 04 (Data Skew, carrusel listo en [`days/day04_data_skew/`](days/day04_data_skew/))

## Tabla de seguimiento

| Día | Nivel | Tema | Tipo | Paleta | Formato | Estado | Link |
|---|---|---|---|---|---|---|---|
| 01 | Avanzado | [UDFs: jerarquía del rendimiento](days/day01_udf_performance/) | Errores | (antiguo) | Post de texto + reto | ✅ Publicado | [post](https://lnkd.in/p/eJkNmXQK) |
| 02 | Intermedio | [dbutils.jobs.taskValues entre tareas](days/day02_task_values/) | Errores | (antiguo) | Post de texto + debate | ✅ Publicado | [post](https://lnkd.in/p/eRmBhjUh) |
| 03 | Avanzado | [Broadcast Join vs Shuffle Join](days/day03_broadcast_join/) | Errores | (antiguo) | Post de texto | ✅ Publicado | [post](https://lnkd.in/p/emV3d4gM) |
| 04 | Avanzado | [Data Skew en Spark](days/day04_data_skew/) | Errores que cuestan plata | `pino` | Carrusel PDF | 🎨 Listo | — |
| 05 | Intermedio | [repartition() vs coalesce()](days/day05_repartition_vs_coalesce/) | Pregunta de entrevista | `medianoche` | Carrusel PDF | ⏳ Pendiente | — |
| 06 | Avanzado | [ZORDER vs Liquid Clustering](days/day06_zorder_vs_liquid_clustering/) | Opinión / Debate | `medianoche` | Infografía | ⏳ Pendiente | — |
| 07 | Avanzado | [Medallion: 5 errores comunes](days/day07_medallion_mistakes/) | Arquitectura en una imagen | `bosque` | Infografía | ⏳ Pendiente | — |
| 08 | Intermedio | [Auto Loader vs COPY INTO](days/day08_auto_loader_vs_copy_into/) | Errores que cuestan plata | `pino` | Infografía | ⏳ Pendiente | — |
| 09 | Avanzado | [SCD Tipo 2 con MERGE](days/day09_scd2_merge/) | Arquitectura en una imagen | `bosque` | Carrusel PDF | ⏳ Pendiente | — |
| 10 | Avanzado | [Generadores y yield](days/day10_generators_yield/) | Antes vs. Después | `pino` | Carrusel corto / imagen | ⏳ Pendiente | — |
| 11 | Intermedio | [5 checks de calidad antes de Silver](days/day11_data_quality_checks/) | Guardable | `bosque` | Carrusel PDF | ⏳ Pendiente | — |
| 12 | Intermedio | [DefaultAzureCredential](days/day12_default_azure_credential/) | Errores que cuestan plata | `pino` | Carrusel corto / imagen | ⏳ Pendiente | — |
| 13 | Básico | [Senior vs Junior](days/day13_senior_vs_junior/) | Opinión / Debate | `medianoche` | Texto largo + 1 imagen | ⏳ Pendiente | — |
| 14 | Avanzado | [Unity Catalog](days/day14_unity_catalog/) | Pregunta de entrevista | `medianoche` | Carrusel PDF | ⏳ Pendiente | — |
| 15 | Básico | [Roadmap Data Engineer 2026](days/day15_roadmap_2026/) | Guardable | `bosque` | Carrusel PDF | ⏳ Pendiente | — |

Estados: ⏳ Pendiente → 🎨 Listo (visual renderizado y revisado) → ✅ Publicado

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
