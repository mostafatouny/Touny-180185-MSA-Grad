# Constants
#topicNum = 3
termNum = 10
topDocsNum = 3

# Filter Tweets
from module.filterData.main import filterTweets as filterTweets

# Gensim
from gensim import corpora

from module.text_model.bagOfWords import bow
from module.topic_modeling.latentDirichletAllocation import lda
from module.optimization.topicCoherence import topicCoherence

# Summary
from module.summary.main import genSummaryFromTopDocs

# Word Cloud
from module.word_cloud.topTerms import getTopTopicsTerms as wordCloudTopicsTopTerms
from module.word_cloud.main import createWordCloudImgEnc as wordCloudImgEnc


def tweetsToResult_pipeline(text_list_in, onlyTopicTerms=False):
    text_list = text_list_in

    # filter
    text_list, new_text_list = filterTweets(text_list)

    # raise exception if no English data is fetched
    if len(new_text_list) < 10:
        raise ValueError("No sufficient English data is fetched")

    #gensim
    dictionary = corpora.Dictionary(new_text_list)
    bowOb = bow(new_text_list, dictionary)
    coh = topicCoherence(bowOb, new_text_list, dictionary, 3, 10, 2)
    ldaOb = coh.getOptimalModel()

    # topic terms
    topic_terms = wordCloudTopicsTopTerms(ldaOb, dictionary, termNum)

    if onlyTopicTerms:
        return topic_terms

    topic_summary = genSummaryFromTopDocs(ldaOb, topDocsNum, text_list)

    assert(len(topic_terms) == len(topic_summary)), "unequal topic_terms and topic_summary lengths"

    imgSumList = []
    for ind in range(len(topic_terms)):
        imgSumList.append(  (    wordCloudImgEnc(topic_terms[ind]) , topic_summary[ind])  )

    # log
    #print("\n==========\ntext_list:\n", text_list, "\n=============\n")
    #print("\n==========\nAll Topics Dist:\n", ldaOb.printTopics(), "\n=============\n")
    #print("\n==========\ntopic_terms:\n", topic_terms, "\n=============\n")
    #print("\n==========\nsummary:\n", topic_summary, "\n============\n")

    return topic_terms, topic_summary, imgSumList


def nTerms_from_topicsTerms(topic_terms_in):
    topic_terms = topic_terms_in

    # only first term is selected
    topics_termsList = []
    for topic in topic_terms:
        top_termNum = list(topic_terms[topic])[:termNum] 
        topics_termsList.append(top_termNum)

    return topics_termsList