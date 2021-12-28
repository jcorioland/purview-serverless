from azure.purview.scanning import PurviewScanningClient
from azure.core.paging import ItemPaged
from azure.core.exceptions import AzureError
from utils.purview_client import get_purview_client
from utils.request_validation import RequestValidation

import logging
import uuid
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    required_params_names = ["ds_name", "scan_name"]
    rv = RequestValidation(req, required_params_names)
    rv.validate_request()

    if not rv.valid:
        return func.HttpResponse(
            "This HTTP triggered function to create or update a scan executed successfully. " + rv.message,
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
                "kind":"AzureStorageMsi",
                "properties": { 
                    "scanRulesetName": "AzureStorage", 
                    "scanRulesetType": "System", 
                    "collection": 
                        {
                            "referenceName": "purviewideasharing", 
                            "type": "CollectionReference"
                        }
                }
            }
        ds_name = rv.params["ds_name"]
        scan_name = rv.params["scan_name"]
        try:
            response = client.scans.create_or_update(data_source_name=ds_name, scan_name=scan_name, body=body_input)
            logging.info(response)
            return func.HttpResponse(f"Scan {scan_name} successfully created or updated")
        except AzureError as e:
            return func.HttpResponse(
                e.message, status_code=e.status_code
        )
            