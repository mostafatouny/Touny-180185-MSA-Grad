from module.twitterCaller.basic_conn import connect_to_endpoint

class user():
    def getScreenName(self):
        return self.userScreenName

    def setScreenName(self, userScreenName_in):
        self.userScreenName = userScreenName_in

    def getId(self):
        return self.userId

    def setId(self, id_in):
        self.userId = id_in
    
    def setResponse(self, response_in):
        self.response = response_in

    def getResponse(self):
        return self.response

    #####

    def isValidUser(self):
        json_response = self.getResponse()
        userScreenName = self.getScreenName()
        #print(json_response)
        assert ("data" in json_response), "{} user screen name is not found".format(userScreenName)
        #raise Exception('{} user screen name is not found'.format(userScreenName))

    def queryUserDetails(self, userScreenName_in):
        userScreenName = userScreenName_in

        url = "https://api.twitter.com/2/users/by/username/{}".format(
            userScreenName
        )

        json_response = connect_to_endpoint(url, getData=False)

        self.setResponse(json_response)
        self.setScreenName(userScreenName)

        self.isValidUser()

        author_id = json_response["data"]["id"]
        self.setId(author_id)

    #####

    def __init__(self, userScreenName_in, checkValidName=True):
        self.queryUserDetails(userScreenName_in)