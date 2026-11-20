# Día 08: Auto Loader vs COPY INTO

| Campo | Valor |
|---|---|
| Nivel | Intermedio |
| Tipo de post | Errores que cuestan plata |
| Formato visual | Infografía animada de pipeline (Opción B): Cloud Storage → Auto Loader → Delta (Bronze) |
| Estado | Pendiente |
| Link | — |

## Estructura visual

- 1. Pipeline con archivos cayendo en ADLS y viajando hasta Bronze
- 2. Cuadro comparativo COPY INTO vs Auto Loader
- 3. Código mínimo de Auto Loader

## Hook alternativo

> Ingestar millones de archivos con COPY INTO es como regar un jardín con un vaso.

## Antes de publicar

- [ ] VERIFICAR: la regla "COPY INTO para miles, Auto Loader para millones" aparece en la guía de Databricks; confirma que sigue vigente en la doc actual.

## Post (copiar y pegar)

```text
📥 Día 8/100: Pythonic Data Engineering | Auto Loader vs COPY INTO

¿Sigues usando COPY INTO para ingestar millones de archivos en Databricks? 🤯

Los dos cargan archivos de forma incremental, pero escalan distinto:

📋 COPY INTO
✅ SQL simple e idempotente
✅ Ideal para miles de archivos o cargas puntuales
⚠️ A medida que crece el número de archivos, escala peor

🚀 Auto Loader (cloudFiles)
✅ Detecta archivos nuevos de forma incremental
✅ Pensado para millones de archivos
✅ Inferencia y evolución de esquema
✅ Checkpoint: sabe qué ya procesó

(spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "json")
    .option("cloudFiles.schemaLocation", schema_path)
    .load("abfss://raw@<account>.dfs.core.windows.net/orders/")
    .writeStream
    .option("checkpointLocation", checkpoint_path)
    .trigger(availableNow=True)
    .toTable("bronze.orders"))

💡 Con trigger(availableNow=True) lo corres como batch: sin clúster encendido 24/7.

¿Cuál usas hoy en tus pipelines? 👇

#Databricks #AutoLoader #DeltaLake #Azure #DataEngineering #100DaysOfPythonicEngineering
```

## Primer comentario

Documentación oficial de Auto Loader en Azure Databricks (learn.microsoft.com/azure/databricks, busca "Auto Loader").
