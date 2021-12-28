import logging
import json
from azure.core.exceptions import AzureError
from utils.purview_client import get_purview_client
import azure.functions as func



def get_all_datasources(client):
    try:
        result = {}
        response = client.data_sources.list_all()
        list_items = [item for item in response]

        result["nb_datasources"] = len(list_items)
        result["datasources"] = list_items
        
        logging.info(response)
        return func.HttpResponse(body=json.dumps(result), mimetype="application/json", status_code=200)
    except AzureError as e:
        return func.HttpResponse(
            e.message, status_code=e.status_code
    )
    except Exception as e:
        return func.HttpResponse(
            str(e), status_code=500
    )


def get_datasource_by_name(client, ds_name:str):
    try:

        response = client.data_sources.get(ds_name)
        logging.info(response)

        return func.HttpResponse(body=json.dumps(response), mimetype="application/json", status_code=200)
    except AzureError as e:
        return func.HttpResponse(
            e.message, status_code=e.status_code
    )
    except Exception as e:
        return func.HttpResponse(
            str(e), status_code=500
    )

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    ds_name = req.route_params.get('ds_name')
    try:
        client = get_purview_client()
    except AzureError as e:
        return func.HttpResponse(
            e.message, status_code=e.status_code
    )

    #Check if we want to list all the datasource or check a specific datasource
    if ds_name:
        return get_datasource_by_name(client, ds_name)
    else:
        return get_all_datasources(client)


