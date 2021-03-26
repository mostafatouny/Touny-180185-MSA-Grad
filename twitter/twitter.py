import json

from module.feed.userFeed import userFeed
from module.feed.originFeed import originFeed
from module.feed.trendFeed import trendFeed

def main():
    try:
        #userFeedOb = userFeed("amazon", 5)
        #json_response = userFeedOb.call()
        originFeedOb = originFeed("amazon", 5)
        json_response = originFeedOb.call()
        #trendFeedOb = trendFeed(["trump", "playstation"], 10, 22)
        #json_response = trendFeedOb.call()
    except AssertionError as asEr:
        print(asEr)
    except ConnectionError as coEr:
        messageStr = coEr.args[0]
        print(messageStr)
    else:
        print(json.dumps(json_response, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
