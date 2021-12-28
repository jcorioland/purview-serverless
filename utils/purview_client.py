from azure.purview.scanning import PurviewScanningClient
from azure.purview.catalog import PurviewCatalogClient
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import HttpResponseError


def get_purview_client():
    credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
    client = PurviewScanningClient(endpoint="https://purviewideasharing.scan.purview.azure.com", credential=credential)  #Add PurviewScanningClient(endpoint="https://purviewideasharing.scan.purview.azure.com", credential=credential)?
    return client

def get_catalog_client():
    credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
    client = PurviewCatalogClient(endpoint="https://purviewideasharing.purview.azure.com/", credential=credential)  #Add PurviewScanningClient(endpoint="https://purviewideasharing.scan.purview.azure.com", credential=credential)?
    return client
