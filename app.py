# source
# -1:None, 1:userTweets, 2:userInteractedTweets, 3:global, 4:global manually
#####

# Flask
#####

from flask import Flask, redirect, url_for, render_template, session, request, jsonify

import config as config

# Feed Number of Posts
feedSize = 100
reqNum = 1

# Local Components
#####
from module.twitterCaller.feed.main import fetchFeed

# Pipeline
from handy import nTerms_from_topicsTerms, tweetsToResult_pipeline

# Global Variables
#####

app = Flask(__name__)
app.config.from_object("config.Config")  # not loaded into other blueprints


# Temporary User's Buffer
#####

temBuf = {}

def saveObject(key_in, object_in):
    temBuf[key_in] = object_in
    #session[key_in] = object_in

def getObject(key_in):
    assert(key_in in temBuf), "a key isn't found in temBuf"
    return temBuf[key_in]
    #assert(key_in in session), "a key isn't found in session"
    #return session[key_in]

def resetSession():
    for key in ["source", "personalization_topicTerms"]:
        if key in temBuf:
            del temBuf[key]
    #for key in ["source", "personalization_tweets", "personalization_topicTerms"]:
    #    if key in session:
    #        del session[key]

#####

@app.route('/')
def home():
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    resetSession()
    return render_template('welcome.html')

@app.route('/fetchPersonalizationSource', methods=["POST"])
def fetchPersonalizationSource():
    source = int(request.form["source_in"])

    saveObject("source", source)

    if source == -1:
        return render_template('personalization_tweets.html', source=source)

    userScreenName = request.form["userScreenName_in"]
    
    # user screen name validation is handled in userFeed
    #   it seems reasonable to be here, anyway

    #columnsNames = ["tweets"]

    try:
        if source == 1:
            text_list = fetchFeed(1, [userScreenName], feedSize, reqNum, mode_in=1)
        elif source == 2:
            text_list = fetchFeed(2, [userScreenName], feedSize, reqNum)
        topic_terms = tweetsToResult_pipeline(text_list, onlyTopicTerms=True) ##
    except AssertionError as asEr:
        messageStr = asEr.args[0]
        return render_template('error.html', header = 'Assertion Error', message = messageStr)
    except ConnectionError as coEr:
        messageStr = coEr.args[0]
        return render_template('error.html', header = 'Connection Error', message = messageStr)
    except ValueError as vaEr:
        messageStr = vaEr.args[0]
        return render_template('error.html', header = 'Value Error', message = messageStr)
    else:
        saveObject("personalization_topicTerms", topic_terms)

        list2d = [[st] for st in text_list] # 2d representation
        list2d = list2d[:10] # sample only 10
        return render_template('personalization_tweets.html', source=source, list_2d=list2d)
    
    return 'this line should not be executed'

@app.route('/fetchTargetSource', methods=["POST"])
def fetchTargetSource():

    source = getObject("source")
    target = int(request.form["target_in"])

    if source == 1 or source == 2:
        if target == 3:
            topic_terms = getObject("personalization_topicTerms")
            topics_termsList = nTerms_from_topicsTerms(topic_terms)
            topics_termsList = [lis[0] for lis in topics_termsList] # only first term of each topic

            try:
                text_list = fetchFeed(3, topics_termsList, feedSize, reqNum)
                topic_terms, topic_summary, imgSumList = tweetsToResult_pipeline(text_list) ##
            except AssertionError as asEr:
                messageStr = asEr.args[0]
                return render_template('error.html', header = 'Assertion Error', message = messageStr)
            except ConnectionError as coEr:
                messageStr = coEr.args[0]
                return render_template('error.html', header = 'Connection Error', message = messageStr)
            except ValueError as vaEr:
                messageStr = vaEr.args[0]
                return render_template('error.html', header = 'Value Error', message = messageStr)
            else:
                return render_template('target_tweets.html', imgSumList=imgSumList)
    elif source == -1:
        if target == 1:
            userScreenNameList = [request.form["userScreenName_in_0"], request.form["userScreenName_in_1"], request.form["userScreenName_in_2"]]

            try:
                text_list = fetchFeed(1, userScreenNameList, feedSize, reqNum, mode_in=1)
                topic_terms, topic_summary, imgSumList = tweetsToResult_pipeline(text_list) ##
            except AssertionError as asEr:
                messageStr = asEr.args[0]
                return render_template('error.html', header = 'Assertion Error', message = messageStr)
            except ConnectionError as coEr:
                messageStr = coEr.args[0]
                return render_template('error.html', header = 'Connection Error', message = messageStr)
            except ValueError as vaEr:
                messageStr = vaEr.args[0]
                return render_template('error.html', header = 'Value Error', message = messageStr)
            else:
                return render_template('target_tweets.html', imgSumList=imgSumList)
        elif target == 2:
            userScreenNameList = [request.form["userScreenName_in_0"], request.form["userScreenName_in_1"], request.form["userScreenName_in_2"]]

            try:
                text_list = fetchFeed(2, userScreenNameList, feedSize, reqNum)
                topic_terms, topic_summary, imgSumList = tweetsToResult_pipeline(text_list) ##
            except AssertionError as asEr:
                messageStr = asEr.args[0]
                return render_template('error.html', header = 'Assertion Error', message = messageStr)
            except ConnectionError as coEr:
                messageStr = coEr.args[0]
                return render_template('error.html', header = 'Connection Error', message = messageStr)
            except ValueError as vaEr:
                messageStr = vaEr.args[0]
                return render_template('error.html', header = 'Value Error', message = messageStr)
            else:
                return render_template('target_tweets.html', imgSumList=imgSumList)
        elif target == 4:
            entityList = [request.form["entity_in_0"], request.form["entity_in_1"], request.form["entity_in_2"]]

            try:
                text_list = fetchFeed(3, entityList, feedSize, reqNum)
                topic_terms, topic_summary, imgSumList = tweetsToResult_pipeline(text_list)
            except AssertionError as asEr:
                messageStr = asEr.args[0]
                return render_template('error.html', header = 'Assertion Error', message = messageStr)
            except ConnectionError as coEr:
                messageStr = coEr.args[0]
                return render_template('error.html', header = 'Connection Error', message = messageStr)
            except ValueError as vaEr:
                messageStr = vaEr.args[0]
                return render_template('error.html', header = 'Value Error', message = messageStr)
            else:
                return render_template('target_tweets.html', imgSumList=imgSumList)


    return 'this line should not be executed'


if __name__ == "__main__":
    app.run()
