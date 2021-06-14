import requests
import os

def auth():
    return os.environ.get("BEARER_TOKEN")

def create_headers():
    bearer_token = auth()
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, getData=True):
    headers = create_headers()

    try:
        response = requests.request("GET", url, headers=headers)
    except:
        #print(response.json())
        raise ConnectionError("Connection to requests failed")
    else:
        #print(response.json())
        if response.status_code != 200:
            raise ConnectionError("Connection to twitter failed: {}".format(
                    response.status_code, ''
                    #response.json()['errors']
                    )
                )

        if getData:
            return response.json()['data']

        return response.json()
    
    # nothing should be processed here if an exception occured
    assert(True == False), "No processing should happen here as an exception is raised"
        
