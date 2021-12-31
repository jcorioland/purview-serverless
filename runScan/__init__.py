from azure.purview.scanning import PurviewScanningClient
from azure.core.paging import ItemPaged
from azure.core.exceptions import AzureError, ClientAuthenticationError, ResourceNotFoundError, ResourceExistsError
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
            "This HTTP triggered function run a scan executed successfully. " + rv.message,
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
    
        ds_name = rv.params["ds_name"]
        scan_name = rv.params["scan_name"]
        run_id = uuid.uuid4()
        try:
            response = client.scan_result.run_scan(data_source_name=ds_name, scan_name=scan_name, run_id=run_id)
            logging.info(response)
            return func.HttpResponse(f"Scan {scan_name} successfully started")
        except AzureError as e:
            logging.warning(e)
            return func.HttpResponse(
                e.message, status_code=e.status_code
        )
            