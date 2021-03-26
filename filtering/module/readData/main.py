import json

def readJson(filePath_in):
    with open(filePath_in, 'r') as file:
        jsonAsDict = json.load(file)
    
    return jsonAsDict
