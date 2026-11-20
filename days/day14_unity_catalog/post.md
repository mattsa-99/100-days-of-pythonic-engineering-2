# Día 14: Unity Catalog: gobierno de datos en Databricks

| Campo | Valor |
|---|---|
| Nivel | Avanzado |
| Tipo de post | Pregunta de entrevista |
| Paleta | `medianoche` |
| Formato visual | Infografía animada de árbol/jerarquía: Metastore → Catalog → Schema → Table, con 5 tarjetas numeradas (Opción C adaptada) |
| Estado | Pendiente |
| Link | — |

## Estructura visual

- 1. Árbol de jerarquía a la izquierda
- 2. Tarjetas: permisos, managed vs external, lineage, row filters/column masks, auditoría

## Hook alternativo

> "¿Cómo gobiernas el acceso a los datos en Databricks?" Si empiezas por "con permisos", vas mal.

## Antes de publicar

- [ ] VERIFICAR nombres de funciones (row filters, column masks) y su disponibilidad en tu edición/región.

## Post (copiar y pegar)

```text
🎯 Día 14/100: Pregunta de entrevista | Unity Catalog

"¿Cómo gobiernas el acceso a los datos en Databricks?"

La respuesta senior empieza por la jerarquía:
Metastore → Catalog → Schema → Table / Volume
(namespace de tres niveles: catalog.schema.table)

🔐 Lo que debes poder explicar:
✅ Permisos con GRANT / REVOKE por catálogo, esquema o tabla
✅ Tablas managed vs external (quién controla el almacenamiento)
✅ Lineage: de dónde viene cada tabla y columna
✅ Row filters y column masks para datos sensibles
✅ Auditoría: quién accedió a qué y cuándo

GRANT SELECT ON TABLE main.sales.orders TO `data-analysts`;

💡 Tip: da el ejemplo de un caso real (por ejemplo, ocultar una columna sensible a un grupo) y tu respuesta pasa de teoría a experiencia.

¿Qué te preguntaron a ti sobre gobierno de datos? 👇

#Databricks #UnityCatalog #DataGovernance #DataEngineering #100DaysOfPythonicEngineering
```

## Primer comentario

Documentación oficial de Unity Catalog en Azure Databricks (learn.microsoft.com/azure/databricks).
