# Día 07: Arquitectura Medallion: 5 errores comunes

| Campo | Valor |
|---|---|
| Nivel | Avanzado |
| Tipo de post | Arquitectura en una imagen |
| Formato visual | Infografía animada de pipeline (Opción B): Bronze → Silver → Gold con 5 alertas numeradas |
| Estado | Pendiente |
| Link | — |

## Estructura visual

- 1. Pipeline Bronze → Silver → Gold con paquetes de datos viajando
- 2. 5 puntos rojos numerados sobre el diagrama
- 3. Leyenda con los 5 errores

## Hook alternativo

> Tu capa Gold es una copia de Silver con otro nombre. 😬

## Antes de publicar

- [ ] Contenido conceptual. Si puedes, agrega un ejemplo anonimizado de tu experiencia (sin datos del cliente).

## Post (copiar y pegar)

```text
🏗️ Día 7/100: Pythonic Data Engineering | 5 errores comunes en Arquitectura Medallion

Bronze, Silver, Gold... todos la usamos, pocos la aprovechamos bien.

1️⃣ Transformar en Bronze. Bronze es el dato crudo, append-only, con metadatos (fecha de ingesta, archivo origen).
2️⃣ Silver sin deduplicar ni forzar esquema. Aquí se limpia, se tipa y se valida.
3️⃣ Gold = copia de Silver. Gold son agregados y modelos pensados para el negocio.
4️⃣ Cero validaciones entre capas. Un dato malo en Bronze llega intacto al dashboard.
5️⃣ Sin trazabilidad. Si no sabes de dónde viene una columna, no puedes confiar en ella.

💡 Regla simple: cada capa debe poder responder "¿por qué existo?" en una frase.

¿Cuál de los 5 te has encontrado más? Cuéntame 👇

Guarda este post 📌 para tu próxima revisión de arquitectura.

#DataEngineering #Databricks #DeltaLake #Medallion #LakehouseArchitecture #100DaysOfPythonicEngineering
```

## Primer comentario

Referencia: Medallion Architecture en la documentación de Azure Databricks.
