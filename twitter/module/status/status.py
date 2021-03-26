

class status():
    def __init__(self, status_in):
        self.status = status_in
        pass

    def getStatusId(self):
        return status["id_str"]

    def getStatusObject(self):
        return self.status