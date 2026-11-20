# Día 04: Data Skew: el enemigo silencioso de tus jobs en Spark

| Campo | Valor |
|---|---|
| Nivel | Avanzado |
| Tipo de post | Errores que cuestan plata |
| Paleta | `pino` |
| Formato visual | Carrusel PDF (8 láminas, 1080x1350) |
| Estado | Listo (`day04_data_skew.pdf`) |
| Link | — |

## Estructura visual

- 1. Portada (oscura): ¿Tu job espera una hora por UNA sola tarea? + barras de tareas
- 2. El problema (clara): qué es el skew, por qué pasa (shuffle junta la misma key) + definiciones
- 3. Cómo detectarlo (oscura): 3 señales en la Spark UI, cada una explicada
- 4. Arreglos 1 y 2 (clara): quitar keys NULL + AQE
- 5. Arreglo 3 (oscura): broadcast (conexión con Día 3) + definición de executor
- 6. Arreglo 4, la idea (clara): salting con mini tablas en 3 pasos
- 7. Arreglo 4, el código (oscura): los mismos 3 pasos en PySpark
- 8. Cierre (oscura): pregunta + GUARDA / DÍA 05 / REPO

## Hook alternativo

> Tu cluster tiene 200 cores y 199 están de brazos cruzados. 😴

## Antes de publicar

- [ ] Completa o borra la línea `[TU ANÉCDOTA: ...]` del post.
- [ ] Publicar martes, miércoles o jueves entre 9:00 y 11:00 a.m. hora Colombia, y anotar día y hora en la tabla de Métricas.
- [ ] Revisa en tu runtime que AQE esté habilitado (suele venir activo en Databricks recientes). El salting usa N = 4 para coincidir con el ejemplo de las láminas; en un caso real ajusta N según el tamaño de la key caliente.

## Post (copiar y pegar)

```text
¿Tu job lleva una hora esperando por UNA sola tarea?

Casi siempre es data skew, y se arregla con 4 cambios. De menos a más esfuerzo 👇

En un join, Spark junta las filas con la misma key (la columna del join, ej. customer_id).

Si una key concentra casi todas las filas, una sola partición recibe casi todo. Y todo el stage (cada etapa del job) espera a esa tarea.

Cómo detectarlo en la Spark UI:

1. Una tarea dura 10x más que la mediana
2. Shuffle Read gigante → esa tarea recibió muchos más datos por la red que el resto
3. Spill a disco en pocas tareas → no le cabe en memoria y usa el disco

Cómo arreglarlo, de menos a más esfuerzo:

1. Filtrar keys nulas → nunca hacen match, pero viajan juntas a una sola partición
2. AQE (Adaptive Query Execution) → Spark divide sola las particiones gigantes mientras corre
3. Broadcast → si la otra tabla es pequeña, Spark la copia a cada executor y no hay shuffle (lo vimos en el Día 3)
4. Salting → agregas una columna al azar, el salt, para partir la key caliente en N pedazos

⚠️ El salting tiene un costo: la tabla pequeña se copia N veces. Úsalo cuando lo demás no alcance.

El código de cada arreglo está en el carrusel.

[TU ANÉCDOTA: 1 o 2 líneas sobre un job con skew que te tocó arreglar. Si no tienes una, borra esta línea.]

¿Cuál ha sido tu peor caso de skew? Cuéntame qué tan grande era la tabla y cómo lo resolviste.

Si le sirve a alguien de tu equipo, compártelo ♻️

Día 4/100 de Pythonic Data Engineering. Sígueme para el Día 5: repartition() vs coalesce().

#DataEngineering #ApacheSpark #100DaysOfPythonicEngineering
```

## Primer comentario

Documentación oficial de ajuste de rendimiento en Spark SQL: https://spark.apache.org/docs/latest/sql-performance-tuning.html  |  Repo: github.com/mattsa-99/100-days-of-pythonic-engineering-2
