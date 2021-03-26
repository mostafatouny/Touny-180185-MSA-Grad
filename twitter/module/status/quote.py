from module.status.status import status

class quote_st(status):

    def getOriginStId(self):
        quote_st = self.status["quoted_status"]
        quote_id = quote_st["id_str"]

        return quote_id