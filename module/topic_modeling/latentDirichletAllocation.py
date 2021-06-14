from gensim.models.ldamodel import LdaModel

class lda():

    def set_lda(self, lda_in):
        self.lda = lda_in

    def get_lda(self):
        return self.lda

    def set_document_topics_dist(self, document_topics_dist_in):
        self.document_topics_dist = document_topics_dist_in

    def get_document_topics_dist(self):
        return self.document_topics_dist

    def get_documentInd_topicDist(self, documentInd_in):
        documentInd = documentInd_in
        return self.document_topics_dist[documentInd]

    def set_topicsNum(self, topicsNum_in):
        self.topicsNum = topicsNum_in

    def get_topicsNum(self):
        return self.topicsNum

    def set_docsNum(self, docsNum_in):
        self.docsNum = docsNum_in

    def get_docsNum(self):
        return self.docsNum

    #####

    def get_topicIndTerms(self, topicInd_in, termsNum_in):
        topicInd = topicInd_in
        termsNum = termsNum_in

        lda = self.get_lda()
        sortedList = lda.get_topic_terms(topicInd)[:termsNum]

        return {"topicInd":topicInd, "data":sortedList}
        # test by
        # [dictionary[term[0]] for term in ldaOb.get_topicIndTerms(0, 3)["data"]]

    def get_TopDocs_topicInd(self, topicInd_in, docsNum_in):
        topicInd = topicInd_in
        docsNum = docsNum_in

        document_topics_dist = self.get_document_topics_dist()
        docInd_topicsDist = []

        for ind, doc in enumerate(document_topics_dist):
            topicDist = [topicDist[1] for topicDist in doc if topicDist[0]==topicInd]
            assert(len(topicDist)<=1), "the same topic is matched more than once"
            if len(topicDist)==0: #not found
                topicDist = 0
            else:
                topicDist = topicDist[0]
            docInd_topicsDist.append((ind, topicDist))

        # sort in place
        docInd_topicsDist.sort(key=lambda tup: tup[1], reverse=True)
        # slice top docsNum
        docInd_topicsDist = docInd_topicsDist[:docsNum]
        sortedIndices = {"topicInd":topicInd, "data":docInd_topicsDist}

        return sortedIndices
        # test by
        # [doc_clean[doc[0]] for doc in ldaOb.get_TopDocs_topicInd(1, 3)["data"]]

    #####

    def __init__(self, bow_in, dictionary_in, topicsNum_in):
        bow = bow_in
        dictionary = dictionary_in
        topicsNum = topicsNum_in

        doc_term_matrix = bow.get_doc_term_matrix()

        self.set_topicsNum(topicsNum)

        lda = LdaModel(doc_term_matrix, num_topics=topicsNum, id2word = dictionary, passes=50)
        self.set_lda(lda)

        document_topics_dist = lda.get_document_topics(doc_term_matrix)
        assert(len(document_topics_dist) == len(doc_term_matrix)), "document dist length is not equal to doc_term"

        self.set_document_topics_dist(document_topics_dist)

    #####

    def printTopics(self):
        return self.get_lda().print_topics()
