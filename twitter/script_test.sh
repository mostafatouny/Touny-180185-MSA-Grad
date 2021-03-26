# given a user screen name, find his author_id
#curl --request GET \
#  --url 'https://api.twitter.com/2/users/by/username/facebook' \
#  --header "authorization: Bearer $BEARER_TOKEN"

# given a user id, query his recent timeline
#curl --request GET \
#  --url "https://api.twitter.com/2/users/2425151/tweets?tweet.fields=referenced_tweets,lang" \
#  --header "authorization: Bearer $BEARER_TOKEN"

# given tweet id, query it (whole tweet is shown)
#curl --request GET \
#  --url 'https://api.twitter.com/2/tweets?tweet.fields=lang&ids=1319988764240977926,1319988764240977926' \
#  --header "authorization: Bearer $BEARER_TOKEN"

# given tweet id, query its conversation thread
# source: https://developer.twitter.com/en/docs/twitter-api/conversation-id
#curl --request GET \
#  --url 'https://api.twitter.com/2/tweets?ids=1336293917659189249&tweet.fields=author_id,conversation_id,created_at,in_reply_to_user_id,referenced_tweets&expansions=author_id,in_reply_to_user_id,referenced_tweets.id&user.fields=name,username' \
#  --header "Authorization: Bearer $BEARER_TOKEN"

# given a conversation id, query its thread
#curl --request GET \
#  --url 'https://api.twitter.com/2/tweets/search/recent?query=conversation_id:1336293917659189249&tweet.fields=in_reply_to_user_id,author_id,created_at,conversation_id' \
#  --header "Authorization: Bearer $BEARER_TOKEN"

# given a user name, obtain his pinned tweet
#curl --request GET \
#  --url 'https://api.twitter.com/2/users/by?usernames=twitterdev&expansions=pinned_tweet_id&tweet.fields=author_id' \
#  --header "authorization: Bearer $BEARER_TOKEN"

# given a user name, obtain recent tweets, v2
#   limited to 7 days ago by
#curl --request GET \
#  --url 'https://api.twitter.com/2/tweets/search/recent?query=from:TwitterDev&expansions=author_id&user.fields=id&max_results=20&start_time=2020-10-01T12:00:00Z' \
#  --header "authorization: Bearer $BEARER_TOKEN"
# id of author is returned by default anyway

# given a user name, obtain recent tweets, v1
#curl --request GET \
#  --url 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=SophieHuiberts&trim_user=1&count=20' \
#  --header "authorization: Bearer $BEARER_TOKEN"

# given a keyword, search tweet's body of it but tokenized
#curl --request GET \
#  --url 'https://api.twitter.com/2/tweets/search/recent?query=trump' \
#  --header "authorization: Bearer $BEARER_TOKEN"
# for next call, add &next_token=<previous response, meta, next_token>

# given a user name, obtain recent home-timeline, v1  
#  FAILED
#curl --request POST \
#  --url 'https://api.twitter.com/1.1/statuses/update.json?status=Hello%20world' \
#  --header 'authorization: OAuth oauth_consumer_key="NOsfTLJwlHYdu7kcyscX3MTUA", oauth_token="1111144729599766528-bNY11MaMypbJBMnsf3Rup8zz1jDxNW", oauth_signature_method="HMAC-SHA1", oauth_version="1.0", oauth_timestamp="1607613916", oauth_nonce="kYjzVBB8Y0ZFabxSWbWovY3uYSQ2pTgmZeNu2VS4cg", oauth_signature="tnnArxj06cWHq44gCs1OSKk%2FjLY%3D"' \
