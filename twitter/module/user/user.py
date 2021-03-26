from module.basic_conn import connect_to_endpoint

class user():
    def getScreenName(self):
        return self.userScreenName

    def setScreenName(self, userScreenName_in):
        self.userScreenName = userScreenName_in

    def isValidUser(self):
        userScreenName = self.getScreenName()

        url = "https://api.twitter.com/2/users/by/username/{}".format(
            userScreenName
        )

        json_response = connect_to_endpoint(url)
        assert ("data" in json_response), "{} user screen name is not found".format(userScreenName)
        #raise Exception('{} user screen name is not found'.format(userScreenName))

    def __init__(self, userScreenName_in, checkValidName=True):
        self.setScreenName(userScreenName_in)

        if checkValidName:
            self.isValidUser()