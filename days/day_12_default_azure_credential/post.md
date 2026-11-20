# Día 12: Azure Identity: DefaultAzureCredential

| Campo | Valor |
|---|---|
| Nivel | Intermedio |
| Tipo de post | Errores que cuestan plata |
| Formato visual | Ventana macOS Antes/Después (Opción D) + mini diagrama de la cadena de credenciales |
| Estado | Pendiente |
| Link | — |

## Estructura visual

- 1. ANTES: connection string con key en el código
- 2. DESPUÉS: DefaultAzureCredential
- 3. Diagrama: local (az login) vs Azure (Managed Identity)

## Hook alternativo

> Si hay un password en tu código, tienes un incidente de seguridad esperando.

## Antes de publicar

- [ ] Revisa los nombres de roles RBAC en tu suscripción antes de publicar.

## Post (copiar y pegar)

```text
🔐 Día 12/100: Pythonic Data Engineering | DefaultAzureCredential

Si tienes un password o una key en tu código, tienes un incidente esperando a ocurrir. 🚨

# ❌ Antes
client = BlobServiceClient.from_connection_string("DefaultEndpointsProtocol=...;AccountKey=...")
 
# ✅ Después
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
 
client = BlobServiceClient(
    account_url="https://<account>.blob.core.windows.net",
    credential=DefaultAzureCredential(),
)

💡 DefaultAzureCredential prueba una cadena de métodos hasta que uno funciona:
✅ En local: tu sesión de az login
✅ En Azure: Managed Identity
✅ En CI/CD: variables de entorno o service principal

Mismo código en tu laptop y en producción. Cero secretos en el repositorio.

⚠️ Acuérdate de asignar el rol RBAC adecuado a la identidad (ej. Storage Blob Data Contributor).

¿Cuántos secretos has encontrado en un repo? 😅 👇

#Azure #Python #DataEngineering #Security #100DaysOfPythonicEngineering
```

## Primer comentario

Documentación: Azure Identity client library for Python (learn.microsoft.com).
