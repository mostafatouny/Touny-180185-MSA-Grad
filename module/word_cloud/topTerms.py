
def getTopTopicsTerms(ldaOb_in, dictionary_in, termNum_in):
    ldaOb = ldaOb_in
    dictionary = dictionary_in
    termNum = termNum_in

    topicNum = ldaOb.get_topicsNum()
    topic_terms = {}

    for topicInd in range(topicNum):

        # top terms of a given topic index
        topTerms = ldaOb.get_topicIndTerms(topicInd, termNum)
        
        topTermsTuples = [el for el in topTerms['data'] ]
        topTermsDict = {}
        for el in topTermsTuples:
            topTermsDict[dictionary[el[0]]] = el[1]
            #topTermsDict[dictionary[el[0]]] = int(el[1]*(10**9))

        topic_terms[topicInd] = topTermsDict

    return topic_terms