# 🐍 100 Days of Pythonic Engineering

Serie de LinkedIn sobre Data Engineering con Python, Spark, Databricks y Azure, en español.
Cada día tiene su carpeta en [`days/`](days/) con el post listo para copiar, el código del snippet y el material visual.

> Plan base: *Plan Maestro V3* (19 de noviembre de 2026). Banco de temas extra en [ideas.md](ideas.md).

## 📍 Dónde vamos

**Último publicado:** Día 03 · **Siguiente:** Día 04 (Data Skew, carrusel PDF listo en `days/day_04_data_skew/carousel/`)

## Tabla de seguimiento

| Día | Nivel | Tema | Tipo | Formato | Estado | Link |
|---|---|---|---|---|---|---|
| 01 | Avanzado | [UDFs: jerarquía del rendimiento](days/day_01_udf_performance/) | Errores | Post de texto + reto | ✅ Publicado | [post](https://lnkd.in/p/eJkNmXQK) |
| 02 | Intermedio | [dbutils.jobs.taskValues entre tareas](days/day_02_task_values/) | Errores | Post de texto + debate | ✅ Publicado | [post](https://lnkd.in/p/eRmBhjUh) |
| 03 | Avanzado | [Broadcast Join vs Shuffle Join](days/day_03_broadcast_join/) | Errores | Post de texto | ✅ Publicado | [post](https://lnkd.in/p/emV3d4gM) |
| 04 | Avanzado | [Data Skew en Spark](days/day_04_data_skew/) | Errores que cuestan plata | Carrusel PDF | 🎨 Visual listo | — |
| 05 | Intermedio | [repartition() vs coalesce()](days/day_05_repartition_vs_coalesce/) | Pregunta de entrevista | Carrusel PDF | ⏳ Pendiente | — |
| 06 | Avanzado | [ZORDER vs Liquid Clustering](days/day_06_zorder_vs_liquid_clustering/) | Debate | Infografía animada | ⏳ Pendiente | — |
| 07 | Avanzado | [Medallion: 5 errores comunes](days/day_07_medallion_mistakes/) | Arquitectura en una imagen | Infografía animada | ⏳ Pendiente | — |
| 08 | Intermedio | [Auto Loader vs COPY INTO](days/day_08_auto_loader_vs_copy_into/) | Errores que cuestan plata | Infografía animada | ⏳ Pendiente | — |
| 09 | Avanzado | [SCD Tipo 2 con MERGE](days/day_09_scd2_merge/) | Arquitectura en una imagen | Carrusel PDF | ⏳ Pendiente | — |
| 10 | Avanzado | [Generadores y yield](days/day_10_generators_yield/) | Antes vs. Después | Ventana macOS | ⏳ Pendiente | — |
| 11 | Intermedio | [5 checks de calidad antes de Silver](days/day_11_data_quality_checks/) | Guardable (checklist) | Carrusel PDF | ⏳ Pendiente | — |
| 12 | Intermedio | [DefaultAzureCredential](days/day_12_default_azure_credential/) | Errores que cuestan plata | Ventana macOS | ⏳ Pendiente | — |
| 13 | Básico | [Senior vs Junior](days/day_13_senior_vs_junior/) | Opinión | Post de texto + imagen | ⏳ Pendiente | — |
| 14 | Avanzado | [Unity Catalog](days/day_14_unity_catalog/) | Pregunta de entrevista | Infografía animada | ⏳ Pendiente | — |
| 15 | Básico | [Roadmap Data Engineer 2026](days/day_15_roadmap_2026/) | Guardable (roadmap) | Carrusel PDF | ⏳ Pendiente | — |

Estados: ⏳ Pendiente → 🎨 Visual listo → ✅ Publicado

## Rotación de tipos de post

| Tipo | Para qué sirve |
|---|---|
| Errores que cuestan plata | Costos y rendimiento en Spark, Databricks y Azure. Buenos guardados. |
| Pregunta de entrevista | Autoridad como entrevistador técnico. Genera comentarios. |
| Antes vs. Después (código) | Quick wins de Python en ventana estilo macOS. |
| Arquitectura en una imagen | Diagramas y pipelines. Los más compartibles. |
| Opinión / Debate | Pregunta final fuerte. Los que más comentarios generan. |

## Plantilla de post

1. **Hook:** una pregunta o un error común en la primera línea.
2. **Cuerpo:** beneficio concreto (rendimiento, costo, legibilidad, memoria).
3. **Código o imagen:** snippet corto o la pieza visual del día.
4. **Pregunta final:** invita a comentar una experiencia concreta.
5. **CTA:** "Sígueme para el Día X/100"; en los guardables, "Guarda este post".
6. **Primer comentario:** documentación oficial + link a este repo (nunca links en el cuerpo).

## Estructura del repo

```
days/day_XX_<tema>/
├── post.md          # metadatos, checklist "antes de publicar", post y primer comentario
├── *.py / *.sql     # código del snippet, completo y con tipado
└── carousel/        # HTML fuente + PDF (cuando el formato es carrusel)
tools/render_carousel.sh   # HTML → PDF 1080x1350 con Chrome headless
```

## Reglas de código

Nombres en inglés, tipado completo, docstrings estilo Google y PEP 8.

## Revisión de métricas

Después del Día 08 (5 posts del plan V3): comparar guardados y comentarios por tipo de post y ajustar el calendario.
