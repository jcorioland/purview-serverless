from azure.core.exceptions import AzureError, ClientAuthenticationError, ResourceNotFoundError, ResourceExistsError
from utils.purview_client import get_purview_client

import logging
import json
import azure.functions as func


# client.scan_result.list_scan_history(data_source_name=ds_name, scan_name=scan_name)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('This HTTP function to get scans executed successfully.')

    ds_name = req.route_params.get('ds_name')
    scan_name = req.route_params.get('scan_name')

    try:
        client = get_purview_client()
    except AzureError as e:
        logging.warning("Error")
        logging.warning(e)
        return func.HttpResponse(
            "Internal Server Error", status_code=500
    )

    try:
        result = {}
        response = client.scan_result.list_scan_history(data_source_name=ds_name, scan_name=scan_name)

    except (ClientAuthenticationError, ResourceNotFoundError, ResourceExistsError) as e:
        logging.warning(f"Error - Status code : {e.status_code} ")
        logging.warning(e.message)
        return func.HttpResponse(
            e.message, status_code=e.status_code
    )
    except AzureError as e:
        logging.warning(f"Error")
        logging.warning(e)
        return func.HttpResponse(
            "Internal Server Error", status_code=500
    )
    else:
        list_items = [item for item in response]

        result["n_runs"] = len(list_items)
        result["runs"] = list_items
        
        logging.info(response)
        return func.HttpResponse(body=json.dumps(result), mimetype="application/json", status_code=200) 
        

