import logging
import json
import azure.functions as func
from utils.purview_client import get_catalog_client
from azure.core.exceptions import AzureError, ClientAuthenticationError, ResourceNotFoundError, ResourceExistsError
from utils.request_validation import RequestValidation


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    required_params_names = ["keywords"]
    rv = RequestValidation(req, required_params_names)
    rv.validate_request()

    if not rv.valid:
        return func.HttpResponse(
            "This HTTP triggered function to search the catalog executed successfully. " + rv.message,
            status_code=400
        )
    else:
        try:
            client_catalog = get_catalog_client()
        except AzureError as e:
            logging.warning(f"Error")
            logging.warning(e)
            return func.HttpResponse(
                "Internal Server Error", status_code=500
        )

        keywords = rv.params["keywords"]
        logging.warning(keywords)
        try:
            body_input={
                "keywords": keywords
            }
            response = client_catalog.discovery.query(search_request=body_input)
            return func.HttpResponse(body=json.dumps(response), mimetype="application/json")
        except AzureError as e:
            return func.HttpResponse(
                e.message, status_code=e.status_code
        )
