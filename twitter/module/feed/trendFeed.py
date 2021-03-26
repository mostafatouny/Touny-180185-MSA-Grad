from module.feed.feed import feed

import module.basic_conn as basic_conn
from module.term.trend import trend_te 

class trendFeed(feed):

    def setTermsList(self, termsList_in):
        self.termsList = termsList_in

    def getTermsList(self):
        return self.termsList

    def setTerm_maxCountReq(self, term_maxCountReq_in):
        self.term_maxCountReq = term_maxCountReq_in

    def getTerm_maxCountReq(self):
        return self.term_maxCountReq

    def setTerm_minCoun(self, term_minCoun_in):
        self.term_minCoun = term_minCoun_in

    def getTerm_minCoun(self):
        return self.term_minCoun

    #####


    def filter(self, statusesList_in):
        statusesList = statusesList_in["data"]

        filteredList = []

        for st in statusesList:
            if st["lang"] == "en":
                filteredList.append(st)
        
        return filteredList

    def call(self):
        termsList = self.getTermsList()
        term_maxCountReq = self.getTerm_maxCountReq()
        term_minCoun = self.getTerm_minCoun()

        term_jsonRes = []

        termsList = [trend_te(x) for x in termsList]

        counter = 0

        while counter < term_minCoun:

            for tr in termsList:
                url = tr.getUrl(term_maxCountReq)
                json_response = basic_conn.connect_to_endpoint(url)
                filteredFeed = self.filter(json_response)
                term_jsonRes.append(filteredFeed)

                nextToken = json_response['meta']['next_token']
                tr.setNextToken(nextToken)

                counter = counter + json_response['meta']['result_count']


        return term_jsonRes


    #####

    def __init__(self, termsList_in, term_maxCountReq_in, term_minCoun_in):
        self.setTermsList(termsList_in)
        self.setTerm_maxCountReq(term_maxCountReq_in)
        self.setTerm_minCoun(term_minCoun_in)
