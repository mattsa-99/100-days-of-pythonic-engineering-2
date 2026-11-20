# Cómo llevar la cuenta de la serie

- La fuente de verdad del avance es la tabla de seguimiento de `README.md` y la sección "📍 Dónde vamos".
- Cuando el usuario diga "ya salió el Día X" (con o sin link):
  1. En `README.md`: estado → `✅ Publicado`, columna Link → `[post](<url>)`, y actualizar "Último publicado" / "Siguiente".
  2. En `days/day_XX_*/post.md`: filas `Estado` y `Link` de la tabla de metadatos.
  3. Commit: `Day XX: published`.
- Cuando se termine el visual de un día: estado → `🎨 Visual listo`.
- Días nuevos (16+): crear `days/day_XX_<slug>/post.md` con la misma estructura y agregar la fila a la tabla. Temas de reserva en `ideas.md`.
- Carruseles: HTML en `days/day_XX_*/carousel/carousel.html` (láminas 1080x1350) y PDF con `tools/render_carousel.sh <html> <pdf>`.
- Código Python: inglés, tipado completo, docstrings Google, PEP 8. Sin datos ni nombres de clientes.
- Después de 5 posts del plan V3 (Día 08), pedir métricas (guardados, comentarios) y proponer ajustes al calendario.
