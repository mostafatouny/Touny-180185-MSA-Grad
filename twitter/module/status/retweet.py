from module.status.status import status

class retweet_st(status):

    def getOriginStId(self):
        retweet_st = self.status["retweeted_status"]
        retweet_id = retweet_st["id_str"]

        return retweet_id