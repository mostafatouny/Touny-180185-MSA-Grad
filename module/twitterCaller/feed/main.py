
from module.twitterCaller.feed.userFeed import userFeed
from module.twitterCaller.feed.originFeed import originFeed
from module.twitterCaller.feed.trendFeed import trendFeed


# Feed Number of Posts
#feedSize = 100
#reqNum = 2

def callUser(userScreenName, feedSize, reqNum, mode):
    userFeedOb = userFeed(userScreenName, feedSize, reqNum, mode_in=mode)
    return userFeedOb.call()

def callOrigin(userScreenName, feedSize, reqNum):
    originFeedOb = originFeed(userScreenName, feedSize, reqNum)
    return originFeedOb.call()

def callTrend(termsList, feedSize, reqNum):
    trendFeedOb = trendFeed(termsList, feedSize, reqNum)
    return trendFeedOb.call()

def fetchFeed(feedType_in, inputList_in, feedSize_in, reqNum_in, mode_in=1):
    feedType = feedType_in
    inputList = inputList_in
    feedSize = feedSize_in
    reqNum = reqNum_in
    mode = mode_in

    # filter empty forms
    inputList = [screenName for screenName in inputList if screenName!=""]
    
    response = []

    if feedType == 1:
        for inp in inputList:
            response = response + callUser(inp, feedSize, reqNum, mode)
        
    elif feedType == 2:
        for inp in inputList:
            response = response + callOrigin(inp, feedSize, reqNum)
        
    elif feedType == 3:
        #for inp in inputList:
        response = response + callTrend(inputList, feedSize, reqNum)
        
    else:
        raise Exception("invalid feed type is entered")

    return response

# feed type
# 1: user tweets
# 2: origin tweets
# 3: trend tweets

# mode_in
# 1: text
# 2: ref ids
# 3: complete text