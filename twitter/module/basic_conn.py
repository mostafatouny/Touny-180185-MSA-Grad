import requests
import os

def auth():
    return os.environ.get("BEARER_TOKEN")

def create_headers():
    bearer_token = auth()
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url):
    headers = create_headers()

    try:
        response = requests.request("GET", url, headers=headers)
    except:
        raise ConnectionError("Connection with requests failed")
    else:
        if response.status_code != 200:
            raise ConnectionError("{} response from requests is received".format(response.status_code))
        #    # nothing should be processed here if an exception occured
        return response.json()
    
    # nothing should be processed here if an exception occured
    assert(True == False), "No processing should happen here as an exception is raised"
        
