import logging
import json
import azure.functions as func
from utils.purview_client import get_catalog_client
from azure.core.exceptions import AzureError
from utils.request_validation import RequestValidation


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    required_params_names = ["keywords"]
    rv = RequestValidation(req, required_params_names)
    rv.validate_request()

    if not rv.valid:
        return func.HttpResponse(
            "This HTTP triggered function to create or update a datasource executed successfully. " + rv.message,
            status_code=400
        )
    else:
        try:
            client_catalog = get_catalog_client()
        except AzureError as e:
            return func.HttpResponse(
                e.message, status_code=e.status_code
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

# his HTTP triggered function search the catalog executed successfully. Please add your keywords name in the query string or in the request body.3