def genSummaryFromTopDocs(ldaOb_in, topDocsNum_in, text_list_in):
    ldaOb = ldaOb_in
    topDocsNum = topDocsNum_in
    text_list = text_list_in

    topicNum = ldaOb.get_topicsNum()

    topic_summary = {}
    
    for topicInd in range(topicNum):
        summary = """"""

        # get top docs given a topic index
        topDocs = ldaOb.get_TopDocs_topicInd(topicInd, topDocsNum)

        topDocsIndices = []
        for el in topDocs['data']:
            topDocsIndices.append(el[0])


        for el in topDocsIndices:
            summary = summary + text_list[el] + ". "
        
        topic_summary[topicInd] = summary

    return topic_summary