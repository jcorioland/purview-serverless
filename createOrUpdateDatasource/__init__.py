from azure.purview.scanning import PurviewScanningClient
from azure.core.paging import ItemPaged
from azure.core.exceptions import AzureError
from utils.purview_client import get_purview_client
from utils.request_validation import RequestValidation

import os
import logging
import uuid
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    required_params_names = ["ds_name"]
    rv = RequestValidation(req, required_params_names)
    rv.validate_request()

    if not rv.valid:
        return func.HttpResponse(
            "This HTTP triggered function to create or update a datasource executed successfully. " + rv.message,
            status_code=400
        )
    else:
        try:
            client = get_purview_client()
        except AzureError as e:
            return func.HttpResponse(
                e.message, status_code=e.status_code
        )
    
        body_input = {
            "kind": "AzureStorage",
            "properties": {
                "endpoint": "https://storagideasharingtwo.blob.core.windows.net/",
                "resourceGroup": "idea_sharing",
                "location": "francecentral",
                "resourceName": "storageideasharingtwo",
                "resourceId": "/subscriptions/0504a9a7-25cb-4269-86d2-a36d9149025f/resourceGroups/idea_sharing/providers/Microsoft.Storage/storageAccounts/storagideasharingtwo",
                "collection": {
                    "type": "CollectionReference",
                    "referenceName": "purviewideasharing"
                },
                "dataUseGovernance": "Disabled"
            }
        }
        ds_name = rv.params["ds_name"]
        try:
            response = client.data_sources.create_or_update(ds_name, body=body_input)
            logging.info(response)
            return func.HttpResponse(f"Data source {ds_name} successfully created or updated")
        except AzureError as e:
            return func.HttpResponse(
                e.message, status_code=e.status_code
        )