# Día 05: repartition() vs coalesce()

| Campo | Valor |
|---|---|
| Nivel | Intermedio |
| Tipo de post | Pregunta de entrevista |
| Paleta | `medianoche` |
| Formato visual | Carrusel PDF (6 láminas) o infografía comparativa lado a lado + tabla |
| Estado | Pendiente |
| Link | — |

## Estructura visual

- 1. Portada: La pregunta que más separa a los candidatos
- 2. Respuesta que se queda corta
- 3. repartition: qué hace y cuándo
- 4. coalesce: qué hace y cuándo
- 5. El error clásico: coalesce(1) al escribir
- 6. Tabla resumen + CTA

## Hook alternativo

> "¿Diferencia entre repartition y coalesce?" Si respondes "una sube y otra baja", te falta la mitad.

## Antes de publicar

- [ ] Longitud del copy: 1047 caracteres (regla: 1,200 a 2,000). Ajustar.
- [ ] Si quieres sumar tu autoridad: agrega una línea como "Como entrevistador técnico, esta es de las que más separa perfiles" (solo si es cierta en tu experiencia).

## Post (copiar y pegar)

```text
🎯 Día 5/100: Pregunta de entrevista | repartition vs coalesce

"¿Cuál es la diferencia entre repartition() y coalesce()?"

La respuesta que suena bien pero se queda corta: "una sube y la otra baja las particiones".

La respuesta que impresiona 👇

🔄 repartition(n)
✅ Hace un shuffle completo
✅ Puede subir o bajar particiones
✅ Deja las particiones de tamaño parejo
✅ Puede repartir por columna: repartition(n, "col")

📉 coalesce(n)
✅ Solo baja particiones
✅ Evita el shuffle completo: junta particiones vecinas
⚠️ Puede dejar particiones desbalanceadas

🚨 El error clásico:
df.coalesce(1).write.parquet(path)  # "quiero un solo archivo"
Toda la escritura pasa por UNA tarea (y puede reducir el paralelismo del stage anterior). Con datos grandes, es tu cuello de botella.

Regla práctica: coalesce para reducir al final, justo antes de escribir; repartition cuando necesitas balancear o preparar un join.

¿Qué otra pregunta te hicieron que te dejó pensando? 👇

#DataEngineering #PySpark #Databricks #EntrevistaTecnica #100DaysOfPythonicEngineering
```

## Primer comentario

Referencia: documentación de PySpark DataFrame.repartition y DataFrame.coalesce (spark.apache.org).
