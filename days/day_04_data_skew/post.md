# Día 04: Data Skew: el enemigo silencioso de tus jobs en Spark

| Campo | Valor |
|---|---|
| Nivel | Avanzado |
| Tipo de post | Errores que cuestan plata |
| Formato visual | Carrusel PDF (7 láminas, 1080x1350) |
| Estado | 🎨 Visual listo (`carousel/day_04_data_skew.pdf`) |
| Link | — |

## Estructura visual

- 1. Portada: ¿Tu job espera una hora por UNA sola tarea?
- 2. Qué es el skew (dibujo de 4 particiones desiguales)
- 3. Cómo detectarlo en la Spark UI (3 señales)
- 4. Fix 1 y 2: filtrar nulos + AQE skew join
- 5. Fix 3: broadcast (conexión con Día 3)
- 6. Fix 4: salting con código
- 7. Cierre + pregunta + CTA Día 5

## Hook alternativo

> Tu cluster tiene 200 cores y 199 están de brazos cruzados. 😴

## Antes de publicar

- [ ] Revisa en tu runtime que AQE esté habilitado (suele venir activo en Databricks recientes). El código de salting es el patrón clásico: ajusta N según el tamaño de la llave caliente.

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
1️⃣ Filtra las llaves nulas antes del join
2️⃣ Verifica que AQE esté activo: spark.sql.adaptive.skewJoin.enabled
3️⃣ Haz broadcast si la otra tabla es pequeña (Día 3 👆)
4️⃣ Salting: reparte la llave "caliente" en N pedazos

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

Documentación oficial de ajuste de rendimiento en Spark SQL: https://spark.apache.org/docs/latest/sql-performance-tuning.html  |  Repo: github.com/mateosotoa/100-days-of-pythonic-engineering
