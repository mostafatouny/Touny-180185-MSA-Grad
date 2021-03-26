import numpy as np

import module.summary.sub as summarySub

import module.summary.docsScore as docsScoSummary

def docsScoreSummary(model_in, docs_topicDist_in, n_rep_in, topicsLen_in, bow_in, text_in):
    bow = bow_in

    topicsLen = topicsLen_in
    n_rep = n_rep_in

    # Get top *n_rep* representative documents for each topic
    top_ind = model_in.topNDocsIndForTopics(n_rep_in)
    top_rawDoc, top_tf = summarySub.docsInd_To_rawDoc_tf(topicsLen_in, top_ind, bow, text_in)

    docsScoSumm = docsScoSummary.docsScoreSummary(topicsLen, n_rep, top_tf, top_rawDoc)
    summary = docsScoSumm.getSummary()
    
    return summary