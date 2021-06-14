from module.twitterCaller.feed.feed import feed
from module.twitterCaller.user.user import user

import module.twitterCaller.basic_conn as basic_conn

class userFeed(feed):

    def setUser(self, userScreenName_in):
        # creating object validates user name
        self.user = user(userScreenName_in)

    def getUserScreenName(self):
        return self.user.getScreenName()

    def getUserId(self):
        return self.user.getId()

    def setMode(self, mode_in):
        assert(mode_in==1 or mode_in==2 or mode_in==3), "invalid mode is entered"
        self.mode = mode_in

    def getMode(self):
        return self.mode

    def setNextToken(self, nextToken_in):
        self.nextToken = nextToken_in

    def getNextToken(self):
        tem = self.nextToken
        self.nextToken = None
        return tem

    #####

    def filterRefsIds(self, json_response_in):
        json_response = json_response_in

        refsIds = []

        for st in json_response:
            
            if not "referenced_tweets" in st:
                continue

            refId = st["referenced_tweets"][0]["id"]
            refsIds.append(refId)
            
        return refsIds

    def filterIds(self, json_response_in):
        json_response = json_response_in

        ids = []

        for st in json_response:
            stId = st["id"]
            ids.append(stId)

        return ids

    #####

    def appendNextTokenUrl(self, url_in):
        url = url_in

        nextToken = self.getNextToken()
        if nextToken is not None:
            url = url + '&pagination_token=' + nextToken

        return url

    def url(self):
        userId = self.getUserId()
        feedSize = self.getFeedSize()

        max_results = min(100, feedSize)

        url = 'https://api.twitter.com/2/users/{}/tweets?tweet.fields=referenced_tweets,lang&max_results={}'.format(
            userId, max_results
        )
        
        url = self.appendNextTokenUrl(url)

        return url

    def callReq(self):
        url = self.url()
        mode = self.getMode()

        json_response = basic_conn.connect_to_endpoint(url, getData=False)
        
        if 'next_token' in json_response['meta']:
            self.setNextToken(json_response['meta']['next_token'])

        json_response = json_response['data']

        json_response = self.filterEng(json_response)

        if mode == 1:
            return self.filterTexts(json_response)
        elif mode == 2:
            return self.filterRefsIds(json_response)
        elif mode == 3:
            ids = self.filterIds(json_response)
            return self.extractCompleteTextFromIds(ids)
        
        raise Exception("invalid mode. This line should not be executed")


    #####

    def __init__(self, userScreenName_in, feedSize_in, maxReq_in, mode_in=1):
        self.setUser(userScreenName_in)
        self.setFeedSize(feedSize_in)
        self.setMaxReq(maxReq_in)
        self.setMode(mode_in)
        self.setNextToken(None)

# mode
# 1 text
# 2 refs ids
# 3 complete text