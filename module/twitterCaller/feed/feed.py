
from module.twitterCaller.feed.handy import getStatusesFromIds


class feed():
    
    def setFeedSize(self, feedSize_in):
        self.feedSize = feedSize_in

    def getFeedSize(self):
        return self.feedSize

    def setMaxReq(self, maxReq_in):
        self.maxReq = maxReq_in

    def getMaxReq(self):
        return self.maxReq


    #####

    def filterEng(self, json_response_in):
        json_response = json_response_in

        statusesList = []

        for st in json_response:
            if st['lang'] != "en":
                continue
            statusesList.append(st)
        
        return statusesList

    def filterTexts(self, json_response_in):
        json_response = json_response_in

        texts = []

        for st in json_response:
            text = st["text"]
            texts.append(text)

        return texts

    #####

    def extractCompleteTextFromIds(self, ids_in):
        ids = ids_in
        json_response = getStatusesFromIds(ids)
        response = self.filterEng(json_response)
        texts = self.filterTexts(response)
        
        return texts

    #####

    def call(self):
        feedSize = self.getFeedSize()
        maxReq = self.getMaxReq()

        response = []

        reqCounter = 0

        while len(response) < feedSize and reqCounter < maxReq:
            call_response = self.callReq()
            response = response + call_response
            reqCounter = reqCounter + 1

        return response


    def __init__(self):
        pass