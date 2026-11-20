# Día 11: 5 checks de calidad de datos antes de pasar a Silver

| Campo | Valor |
|---|---|
| Nivel | Intermedio |
| Tipo de post | Guardable (checklist) |
| Paleta | `bosque` |
| Formato visual | Carrusel PDF (7 láminas): una lámina por check + portada + cierre |
| Estado | Pendiente |
| Link | — |

## Estructura visual

- 1. Portada: 5 checks antes de Silver
- 2. 1. Nulos en llaves
- 3. 2. Duplicados de PK
- 4. 3. Rangos y valores válidos
- 5. 4. Frescura y volumen
- 6. Código que junta todo + CTA

## Hook alternativo

> El dashboard del CEO está mal. ¿Quién se dio cuenta primero: tu pipeline o el CEO?

## Antes de publicar

- [ ] Tema ideal para conectar con tu trabajo en frameworks de calidad de datos, pero NO incluyas detalles ni nombres del cliente.

## Post (copiar y pegar)

```text
✅ Día 11/100: Pythonic Data Engineering | 5 checks de calidad antes de Silver

¿Quién se enteró primero de que el dato estaba mal: tu pipeline o el negocio? 😬

Estos 5 checks atrapan la mayoría de los problemas:
1️⃣ Nulos en llaves de negocio
2️⃣ Duplicados en la llave primaria
3️⃣ Valores fuera de rango (montos negativos, fechas futuras)
4️⃣ Frescura: ¿llegó el dato de hoy?
5️⃣ Volumen: ¿cuántas filas vs. lo normal?

checks = {
    "null_keys": df.filter(F.col("order_id").isNull()).count(),
    "duplicates": df.count() - df.dropDuplicates(["order_id"]).count(),
    "negative_amounts": df.filter(F.col("amount") < 0).count(),
}
failed = {name: n for name, n in checks.items() if n > 0}
if failed:
    raise ValueError(f"Data quality checks failed: {failed}")

⚠️ Cada .count() es una acción de Spark: cachea el DataFrame o calcula todo en una sola agregación si es grande.

¿Qué check agregarías a la lista? 👇

Guarda este post 📌 para tu próximo pipeline.

#DataEngineering #DataQuality #PySpark #Databricks #100DaysOfPythonicEngineering
```

## Primer comentario

Referencia: expectativas de calidad de datos en Databricks (busca "pipeline expectations" en la documentación).
