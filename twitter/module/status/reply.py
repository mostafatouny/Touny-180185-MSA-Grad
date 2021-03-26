from module.status.status import status

class reply_st(status):

    def getOriginStId(self):
        reply_id = self.status["in_reply_to_status_id_str"]

        return reply_id