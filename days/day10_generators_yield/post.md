# Día 10: Generadores y yield: archivos de 10 GB sin saturar la RAM

| Campo | Valor |
|---|---|
| Nivel | Avanzado |
| Tipo de post | Antes vs. Después (código) |
| Paleta | `pino` |
| Formato visual | Ventana macOS tipo Ray.so/Carbon con transición animada Antes → Después (Opción D) |
| Estado | Pendiente |
| Link | — |

## Estructura visual

- 1. Ventana ANTES: readlines() carga todo
- 2. Ventana DESPUÉS: generador con yield
- 3. Gráfica de memoria: pico vs. línea plana

## Hook alternativo

> Tu script murió con MemoryError. El archivo "solo" pesaba 10 GB.

## Antes de publicar

- [ ] Demo real para la gráfica de memoria: `python3 example.py` → read_all ≈ 18.5 MB vs read_rows ≈ 0.17 MB de pico (300k filas).
- [ ] Código con tipado: añade `from collections.abc import Iterator` al snippet si lo muestras en imagen (cumple tu estándar de tipado).

## Post (copiar y pegar)

```text
🐍 Día 10/100: Pythonic Data Engineering | Generadores y yield

¿Tu script muere con MemoryError al leer un archivo grande? 💥

# ❌ Antes: carga TODO en RAM
lines = open("big.csv").readlines()
 
# ✅ Después: procesa fila por fila
def read_rows(path: str) -> Iterator[str]:
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line
 
valid = (parse(line) for line in read_rows("big.csv"))

Un generador produce un valor a la vez y no guarda la lista completa. Memoria casi constante, sin importar el tamaño del archivo.

☁️ En Azure funciona igual con blobs grandes: puedes consumir el contenido por trozos (download_blob().chunks()) en lugar de bajarlo entero.

⚠️ En Spark no lo necesitas: Spark ya es perezoso y distribuido. Los generadores brillan en scripts de Python del lado del driver o en utilidades de ingesta.

¿Cuál es el archivo más grande que has intentado cargar de golpe? 😅 👇

#Python #DataEngineering #Azure #CleanCode #100DaysOfPythonicEngineering
```

## Primer comentario

Documentación: Python generators (docs.python.org) y azure-storage-blob (StorageStreamDownloader.chunks).
