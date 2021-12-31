from azure.purview.scanning import PurviewScanningClient
from azure.purview.catalog import PurviewCatalogClient
from azure.identity import DefaultAzureCredential
from azure.core.exceptions import HttpResponseError

import os

def get_purview_client():
    credential = DefaultAzureCredential(exclude_interactive_browser_credential=True)
    client = PurviewScanningClient(endpoint=f"https://{os.environ['ReferenceNamePurview']}.scan.purview.azure.com", credential=credential, logging_enable=True)  
    return client

def get_catalog_client():
    credential = DefaultAzureCredential(exclude_interactive_browser_credential=True)
    client = PurviewCatalogClient(endpoint=f"https://{os.environ['ReferenceNamePurview']}.purview.azure.com/", credential=credential, logging_enable=True)
    return client
