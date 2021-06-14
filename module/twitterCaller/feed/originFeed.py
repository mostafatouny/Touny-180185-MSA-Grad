from module.twitterCaller.feed.feed import feed

from module.twitterCaller.feed.userFeed import userFeed
from module.twitterCaller.feed.handy import getStatusesFromIds

class originFeed(feed):
    def setOriginIds(self, originIds_in):
        self.originIds = originIds_in

    def getOriginIds(self):
        return self.originIds

    #####
    
    def call(self):
        originIds = self.getOriginIds()
        response = self.extractCompleteTextFromIds(originIds)
        
        return response

    #####

    def __init__(self, userScreenName_in, feedSize_in, maxReq_in):
        userFeedOb = userFeed(userScreenName_in, feedSize_in, maxReq_in, mode_in=2)
        userFeed_json = userFeedOb.call()

        self.setOriginIds(userFeed_json)