from module.twitterCaller.feed.feed import feed

import module.twitterCaller.basic_conn as basic_conn
from module.twitterCaller.term.trend import trend_te 

class trendFeed(feed):

    def setTermsList(self, termsList_in):
        self.termsList = termsList_in

    def getTermsList(self):
        return self.termsList

    #####


    def callReq(self):
        termsList = self.getTermsList()
        maxReq = self.getMaxReq()
        feedSize = self.getFeedSize()

        response = []

        termsList = [trend_te(x) for x in termsList]

        for tr in termsList:
            url = tr.getUrl(feedSize)
            json_response = basic_conn.connect_to_endpoint(url, getData=False)

            filteredFeed = self.filterEng(json_response['data'])
            filteredFeed = self.filterTexts(filteredFeed)
            response = response + filteredFeed

            nextToken = json_response['meta']['next_token']
            tr.setNextToken(nextToken)

        return response

    #####

    def __init__(self, termsList_in, feedSize_in, maxReq_in):
        self.setTermsList(termsList_in)
        self.setFeedSize(feedSize_in)
        self.setMaxReq(maxReq_in)
