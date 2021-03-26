import module.basic_conn as basic_conn

def isEng(st_in):
    if st_in["lang"] == "en":
        return True
    return False

def isQuote(st_in):
    # true/false
    return st_in["is_quote_status"]

def isRetweet(st_in):
    # a key exists or not
    return "retweeted_status" in st_in

def isReply(st_in):
    # null or some number
    if st_in["in_reply_to_status_id_str"] is None:
        return False
    return True

#####

def StatusesFromIdsUrl(idsList_in):
    idsList = idsList_in

    url = 'https://api.twitter.com/2/tweets?tweet.fields=lang&ids='

    for st_id in idsList:
        url = url + st_id
        url = url + ','

    # remove last "," from the url
    url = url[:-1]

    return url

def getStatusesFromIds(IdsList_in):
    IdsList = IdsList_in

    url = StatusesFromIdsUrl(IdsList)
    json_response = basic_conn.connect_to_endpoint(url)
    
    return json_response

#####

def getConcreteStatuses(list_in):
    concrete_statuses = []

    for st in list_in:
        concSt = st.getStatusObject()
        concrete_statuses.append(concSt)

    return concrete_statuses
