from module.feed.feed import feed
from module.user.user import user

from module.feed.userFeed import userFeed
from module.handy import getStatusesFromIds

class originFeed(feed):

    def setUser(self, userScreenName_in):
        # creating object validates user name
        self.user = user(userScreenName_in)

    def getUserScreenName(self):
        return self.user.getScreenName()

    def setCount(self, count_in):
        self.count = count_in

    def getCount(self):
        return self.count

    #####

    def originIdsFromStatuses(self, json_response_in):
        json_response = json_response_in

        originIds = []

        for st in json_response:
            #assert(st is not None), "st is none"
            # st is is either a quote, retweet, or reply
            originId = st.getOriginStId()

            assert(originId is not None), "OriginId is None"
            originIds.append(originId)

        return originIds


    def filter(self, statusesList_in):
        statusesList = statusesList_in["data"]

        filteredStatusesList = []

        for st in statusesList:
            if st["lang"] == "en":
                filteredStatusesList.append(st)

        return filteredStatusesList
    
    def call(self):
        screenName = self.getUserScreenName()
        count = self.getCount()

        userFeedOb = userFeed(screenName, count, False)
        userFeed_json = userFeedOb.call()
        originIds = self.originIdsFromStatuses(userFeed_json)
        json_response = getStatusesFromIds(originIds)
        filteredResponse = self.filter(json_response)

        return filteredResponse

    #####

    def __init__(self, userScreenName_in, count_in):
        self.setUser(userScreenName_in)
        self.setCount(count_in)
