# Día 09: SCD Tipo 2 con MERGE en Delta

| Campo | Valor |
|---|---|
| Nivel | Avanzado |
| Tipo de post | Arquitectura en una imagen |
| Formato visual | Carrusel PDF (7 láminas) con tabla antes/después de los registros |
| Estado | Pendiente |
| Link | — |

## Estructura visual

- 1. Portada: Historial de cambios sin perder datos
- 2. Qué es SCD2 (tabla ejemplo con 2 versiones de un cliente)
- 3. El truco: UNION ALL con merge_key NULL
- 4. El MERGE completo
- 5. Qué pasa con nuevos, cambiados y sin cambios
- 6. Errores comunes (hash, fechas, is_current)
- 7. CTA Día 10

## Hook alternativo

> El cliente se mudó de ciudad. ¿Sobrescribes el dato o guardas la historia?

## Antes de publicar

- [ ] PROBAR el MERGE en un notebook con 3 casos (cliente nuevo, cambiado, sin cambios) antes de publicar. La lógica fue revisada, pero siempre valida con tu runtime.

## Post (copiar y pegar)

```text
🕰️ Día 9/100: Pythonic Data Engineering | SCD Tipo 2 con MERGE en Delta

El cliente cambió de ciudad. ¿Sobrescribes el dato o guardas la historia? 🤔

Con SCD Tipo 2 conservas cada versión: una fila "cerrada" con su fecha fin y otra "vigente".

El truco con MERGE: unir el staging dos veces.
✅ Una vez con la llave real → cierra la fila vigente si cambió
✅ Otra con llave NULL → no hace match, así se inserta la nueva versión

MERGE INTO dim_customer t
USING (
  SELECT customer_id AS merge_key, customer_id, city, row_hash
  FROM stg_customer
  UNION ALL
  SELECT NULL, s.customer_id, s.city, s.row_hash
  FROM stg_customer s
  JOIN dim_customer d
    ON s.customer_id = d.customer_id AND d.is_current
  WHERE s.row_hash <> d.row_hash
) u
ON t.customer_id = u.merge_key AND t.is_current
WHEN MATCHED AND t.row_hash <> u.row_hash THEN
  UPDATE SET is_current = false, end_date = current_date()
WHEN NOT MATCHED THEN
  INSERT (customer_id, city, row_hash, start_date, end_date, is_current)
  VALUES (u.customer_id, u.city, u.row_hash, current_date(), NULL, true)

💡 El row_hash te evita comparar columna por columna.

¿Cómo manejas el historial en tus dimensiones? 👇

#DataEngineering #DeltaLake #Databricks #DataModeling #SQL #100DaysOfPythonicEngineering
```

## Primer comentario

Documentación de MERGE INTO en Delta Lake / Azure Databricks.
