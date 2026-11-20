"""Day 12: no secrets in code, use DefaultAzureCredential.

Requires: ``pip install azure-identity azure-storage-blob`` and the RBAC role
``Storage Blob Data Reader`` (or Contributor) assigned to the identity.
"""

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient


def get_blob_client(account_name: str) -> BlobServiceClient:
    """Build a Blob Storage client without keys or connection strings.

    The credential tries, in order: environment variables (CI/CD service
    principal), Managed Identity (Azure), and developer logins such as
    ``az login`` (local). Same code everywhere.

    Args:
        account_name: Storage account name.

    Returns:
        Authenticated ``BlobServiceClient``.
    """
    return BlobServiceClient(
        account_url=f"https://{account_name}.blob.core.windows.net",
        credential=DefaultAzureCredential(),
    )


def list_blob_names(account_name: str, container: str, prefix: str = "") -> list[str]:
    """List blob names in a container folder.

    Args:
        account_name: Storage account name.
        container: Container name.
        prefix: Optional folder prefix to filter by.

    Returns:
        Names of the matching blobs.
    """
    container_client = get_blob_client(account_name).get_container_client(container)
    return [blob.name for blob in container_client.list_blobs(name_starts_with=prefix)]
