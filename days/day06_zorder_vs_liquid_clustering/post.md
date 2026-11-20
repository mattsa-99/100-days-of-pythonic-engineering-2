# Día 06: ZORDER vs Liquid Clustering en Delta Lake

| Campo | Valor |
|---|---|
| Nivel | Avanzado |
| Tipo de post | Debate |
| Paleta | `medianoche` |
| Formato visual | Infografía animada lado a lado + tabla inferior (Opción A del prompt maestro) |
| Estado | Pendiente |
| Link | — |

## Estructura visual

- 1. Columna izquierda: Partitioning + ZORDER (problemas)
- 2. Columna derecha: Liquid Clustering (ventajas)
- 3. Tabla: Cambio de llaves, archivos pequeños, mantenimiento, caso de uso

## Hook alternativo

> Particionar por fecha y país parecía buena idea... hasta que tuviste 40,000 archivos pequeños.

## Antes de publicar

- [ ] VERIFICAR antes de publicar: sintaxis y requisitos de runtime de Liquid Clustering en tu versión de Databricks. Es una función que evoluciona rápido.

## Post (copiar y pegar)

```text
⚡ Día 6/100: Pythonic Data Engineering | ZORDER vs Liquid Clustering

¿Sigues particionando y haciendo ZORDER en tablas nuevas de Delta? 🤔

Particionar por columnas de alta cardinalidad te llena de archivos pequeños. Y cambiar después la llave de partición o de ZORDER duele.

💡 Liquid Clustering:
✅ Reemplaza el particionado y el ZORDER (no se combinan en la misma tabla)
✅ Puedes cambiar las claves de clustering sin recrear la tabla
✅ Pensado para tablas que crecen y cuyos patrones de consulta cambian

CREATE TABLE sales (id BIGINT, country STRING, sale_date DATE)
CLUSTER BY (country, sale_date);
 
OPTIMIZE sales;
 
-- ¿Cambió el patrón de consulta?
ALTER TABLE sales CLUSTER BY (id);

⚠️ Revisa los requisitos de runtime y las limitaciones en la documentación antes de migrar tablas existentes.

¿Ya lo usas en producción o sigues con ZORDER? 👇

#Databricks #DeltaLake #DataEngineering #LakehouseArchitecture #100DaysOfPythonicEngineering
```

## Primer comentario

Documentación oficial de Liquid Clustering en Azure Databricks (learn.microsoft.com/azure/databricks, busca "liquid clustering").
