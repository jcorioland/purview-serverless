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
    
    required_params_names = ["ds_name"]
    rv = RequestValidation(req, required_params_names)
    rv.validate_request()

    if not rv.valid:
        return func.HttpResponse(
            "This HTTP triggered function to delete a datasource executed successfully. " + rv.message,
            status_code=400
        )
    else:
        try:
            client = get_purview_client()
        except AzureError as e:
            return func.HttpResponse(
                e.message, status_code=e.status_code
        )
    
        ds_name = rv.params["ds_name"]
        try:
            response = client.data_sources.delete(ds_name)
            logging.info(response)
            return func.HttpResponse(f"Data source {ds_name} successfully deleted")
        except AzureError as e:
            return func.HttpResponse(
                e.message, status_code=e.status_code
        )
            