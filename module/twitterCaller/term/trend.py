from module.twitterCaller.term.term import term

class trend_te(term):

    def __init__(self, term_in):
        # assigns self.term
        super().__init__(term_in)
        
        self.nextToken = None
        self.url = None

    ##### private methods, indicated by "__" prefix

    def __getNextToken(self):
        tem = self.nextToken
        self.nextToken = None
        return tem

    def __genUrl(self, feedSize_in):
        feedSize = feedSize_in

        max_result = min(100, feedSize)

        self.url = 'https://api.twitter.com/2/tweets/search/recent?tweet.fields=lang&query={}&max_results={}'.format(
            self.term, max_result
        )

        nextToken = self.__getNextToken()
        if nextToken is not None:
            self.url = self.url + "&next_token=" + nextToken

    ##### public methods

    def setNextToken(self, nextToken_in):
        nextToken = nextToken_in
        self.nextToken = nextToken
    
    def getUrl(self, feedSize_in):
        feedSize = feedSize_in

        self.__genUrl(feedSize)
        urlTem = self.url
        self.url = None

        return urlTem