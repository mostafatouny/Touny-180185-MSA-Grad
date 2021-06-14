import module.twitterCaller.basic_conn as basic_conn

listChunkSize = 100

def divide_chunks(l, n):
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 

def StatusesFromIdsUrl(idsList_in):
    idsList = idsList_in

    url = "https://api.twitter.com/2/tweets?tweet.fields=lang&ids="

    for st_id in idsList:
        url = url + st_id
        url = url + ','

    # remove last "," from the url
    url = url[:-1]

    #idsStr = ''
    #for idSt in idsList:
    #    idsStr = idsStr + idSt + ','
    #idsStr[:-1]

    #url = 'https://api.twitter.com/2/tweets?ids={}&tweet.fields=lang'.format(
    #    idsStr
    #)

    return url

def statusesFromChunkedIds(IdsList_in):
    IdsList = IdsList_in
    #assert(len(IdsList_in) <= 100), "more than 100 ids are given"

    url = StatusesFromIdsUrl(IdsList)
    json_response = basic_conn.connect_to_endpoint(url)
    
    return json_response


def getStatusesFromIds(IdsList_in):
    IdsList = IdsList_in
    chunkedIdsLists = list(divide_chunks(IdsList, listChunkSize)) 

    json_response = []

    for idsLis in chunkedIdsLists:
        json_response = json_response + statusesFromChunkedIds(idsLis)

    return json_response