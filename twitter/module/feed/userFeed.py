from module.feed.feed import feed
from module.user.user import user

import module.basic_conn as basic_conn
from module.handy import isEng, isQuote, isRetweet, isReply

from module.status.quote import quote_st
from module.status.retweet import retweet_st
from module.status.reply import reply_st

from module.handy import getConcreteStatuses

class userFeed(feed):

    def setUser(self, userScreenName_in):
        # creating object validates user name
        self.user = user(userScreenName_in)

    def getUserScreenName(self):
        return self.user.getScreenName()

    def setCount(self, count_in):
        self.count = count_in

    def getCount(self):
        return self.count

    def setIsConcreteSt(self, isConcreteSt_in):
        self.isConcreteSt = isConcreteSt_in

    def getIsConcreteSt(self):
        return self.isConcreteSt

    #####

    def filter(self, json_response_in):
        json_response = json_response_in

        filteredJson = []

        for st in json_response:
            # only English statuses are fetched
            if not isEng(st):
                continue

            newSt = None
            if isQuote(st):
                newSt = quote_st(st)
                filteredJson.append(newSt)
            elif isRetweet(st):
                newSt = retweet_st(st)
                filteredJson.append(newSt)
            elif isReply(st):
                newSt = reply_st(st)
                filteredJson.append(newSt)
            
        return filteredJson

    def url(self):
        screenName = self.getUserScreenName()
        count = self.getCount()

        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&trim_user=1&count={}'.format(
            screenName, count
        )

        return url

    def call(self, getConcreteSt_in=True):
        isConcreteSt = self.getIsConcreteSt()

        url = self.url()
        json_response = basic_conn.connect_to_endpoint(url)
        filteredResponse = self.filter(json_response)

        if isConcreteSt:
            filteredResponse = getConcreteStatuses(filteredResponse)

        return filteredResponse

    #####

    def __init__(self, userScreenName_in, count_in, isConcreteSt_in=True):
        self.setUser(userScreenName_in)
        self.setCount(count_in)
        self.setIsConcreteSt(isConcreteSt_in)