from sklearn.decomposition import LatentDirichletAllocation

class LDA():
    def __init__(self, bow_in, k_in):
        self.bow = bow_in
        bowMat = self.bow.getMatrix()

        lda = LatentDirichletAllocation(n_components=k_in, max_iter=5,
                            learning_method = 'online',
                            learning_offset = 50.,
                            random_state = 0)

        self.mod = lda.fit(bowMat)

    def getModel(self):
        return self.mod

    def getNumberOfTopics(self):
        return len(self.mod.components_)

    def getTopWordsOfTopicInd(self, topicIndex_in, n_top_words_in):
        bogFeaNam = self.bow.getFeatureNames()
        topicIndex = topicIndex_in
        n_top_words = n_top_words_in

        #for index, topic in enumerate(model.components_):    
        topList = [bogFeaNam[i] for i in self.mod.components_[topicIndex].argsort()[:-n_top_words - 1 :-1]]
        
        return topList

    def getTopWordsOfTopics(self):
        pass

    # topics' relevance of documents
    def getDocs_topicDist(self):
        bowMat = self.bow.getMatrix()

        docs_topicDist = self.mod.transform(bowMat)
        return docs_topicDist

        # loop on documents,
        # for each, loop on its topics distribution,
        # if topic's score is greater than 0.5 print it


        #for docInd, doc_topicDist in enumerate(docs_topicDist):
        #    print("Doc #{}".format(docInd))
        #    for topInd, topicScore in enumerate(doc_topicDist):
        #       if topicScore > 0.3:
        #           print("Topic #{}: {}".format(topInd, topicScore))
        #   print("\n")

    def topNDocsIndForTopic(self, topicIndex, n_rep_in):
        # number of representative docs
        n_rep = n_rep_in
        # topics' relevance of documents
        docs_topicDist = self.getDocs_topicDist()

        # via numpy, get indices of sorted documents
        sortedDocs_ind = docs_topicDist[:,topicIndex].argsort()
        # slice only top n_rep
        sortedDocs_ind = sortedDocs_ind[-n_rep:]    
        # return generated list
        return sortedDocs_ind

    def topNDocsIndForTopics(self, n_rep_in):
        # number of representative docs
        n_rep = n_rep_in
        # length of topics
        topicsLen = self.getNumberOfTopics()

        # 2d-list, where for each topic, there's a list of docs indices
        top_ind = []

        for index, topic in enumerate(self.mod.components_):
            # append generated list
            top_ind.append(self.topNDocsIndForTopic(index, n_rep))

        return top_ind
