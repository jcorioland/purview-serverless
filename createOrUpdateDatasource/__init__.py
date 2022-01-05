from azure.purview.scanning import PurviewScanningClient
from azure.core.paging import ItemPaged
from azure.core.exceptions import AzureError, HttpResponseError,ClientAuthenticationError, ResourceNotFoundError, ResourceExistsError
from utils.purview_client import get_purview_client
from utils.request_validation import RequestValidation

import os
import logging
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
            logging.warning("Error")
            logging.warning(e)
            return func.HttpResponse(
                "Internal Server Error", status_code=500
        )
        
        body_input = {
            "kind": "AzureStorage",
            "properties": {
                "endpoint": f"https://{os.environ['StorageName']}.blob.core.windows.net/",
                "resourceGroup": os.environ['ResourceGroup'],
                "location": os.environ['ResourceGroupLocation'],
                "resourceName": os.environ['StorageName'],
                "resourceId": os.environ['StorageId'],
                "collection": {
                    "type": "CollectionReference",
                    "referenceName": os.environ['ReferenceNamePurview']
                },
                "dataUseGovernance": "Disabled"
            }
        }
        ds_name = rv.params["ds_name"]
        try:
            response = client.data_sources.create_or_update(ds_name, body=body_input)
            logging.info(response)
            return func.HttpResponse(f"Data source {ds_name} successfully created or updated")
        except (ClientAuthenticationError, ResourceNotFoundError, ResourceExistsError) as e:
            logging.warning(f"Error - Status code : {e.status_code} ")
            logging.warning(e.message)
            return func.HttpResponse(
                e.message, status_code=e.status_code
        )
        except AzureError as e:
            logging.warning("Error")
            logging.warning(e)
            return func.HttpResponse(
                "Internal Server Error", status_code=500
        )