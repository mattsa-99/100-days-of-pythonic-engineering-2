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

- [ ] Claridad del copy (CLAUDE.md 4.1 y 6): definir en pocas palabras AQE, broadcast y salting la primera vez que aparecen.
- [ ] Revisa en tu runtime que AQE esté habilitado (suele venir activo en Databricks recientes). El código de salting es el patrón clásico: ajusta N según el tamaño de la key caliente.

## Post (copiar y pegar)

```text
🐍 Día 4/100: Pythonic Data Engineering | Data Skew, el enemigo silencioso de tus jobs

¿Tu job lleva una hora esperando por UNA sola tarea? 🐢

Casi siempre es data skew: tus datos están mal repartidos y una partición recibe muchísimo más que las demás. Todo el stage espera a la más lenta.

🔎 Cómo detectarlo en la Spark UI:
✅ Una tarea dura 10x más que la mediana
✅ Esa tarea tiene un Shuffle Read gigante
✅ Hay spill a disco solo en unas pocas tareas

🛠️ Cómo arreglarlo (de menos a más esfuerzo):
1️⃣ Filtra las keys nulas antes del join
2️⃣ Verifica que AQE esté activo: spark.sql.adaptive.skewJoin.enabled
3️⃣ Haz broadcast si la otra tabla es pequeña (Día 3 👆)
4️⃣ Salting: reparte la key "caliente" en N pedazos

N = 8
big = big.withColumn("salt", (F.rand() * N).cast("int"))
small = small.withColumn(
    "salt", F.explode(F.array(*[F.lit(i) for i in range(N)]))
)
joined = big.join(small, ["key", "salt"])

💬 ¿Cuál ha sido tu peor caso de skew? Cuéntame 👇

Sígueme para el Día 5/100 📌

#DataEngineering #Databricks #ApacheSpark #PySpark #Performance #100DaysOfPythonicEngineering
```

## Primer comentario

Documentación oficial de ajuste de rendimiento en Spark SQL: https://spark.apache.org/docs/latest/sql-performance-tuning.html  |  Repo: github.com/mattsa-99/100-days-of-pythonic-engineering-2
