import numpy as np

class docsScoreSummary():

    def topics_docsScore(self, topicsLen_in, n_rep_in, top_tf_in):
        topicsLen = topicsLen_in
        n_rep = n_rep_in
        top_tf = top_tf_in

        # score for docs 0, 1, .., n_rep, For each topic
        topic_docsScore = []

        # loop on docs of each topic, and sum
        for i in range(topicsLen):
            docsScore = []
            for j in range(n_rep):
                docSum = np.sum(top_tf[i][j])
                docsScore.append(docSum)
            
            topic_docsScore.append(docsScore)

        return topic_docsScore

    def topics_average(self, topic_docsScore_in, topicsLen_in, n_rep_in):
        topic_docsScore = topic_docsScore_in
        topicsLen = topicsLen_in
        n_rep = n_rep_in

        # average for each topic
        topic_average = []

        # compute averages
        for i in range(topicsLen):
            avg = 0
            for j in range(n_rep):
                avg += topic_docsScore[i][j]
            avg /= n_rep
            
            topic_average.append(avg)

        return topic_average

    # Docs Score & Average, For Each Topic
    def topics_docsScore_average(self, topicsLen_in, n_rep_in, top_tf_in):
        topicsLen = topicsLen_in
        n_rep = n_rep_in
        top_tf = top_tf_in

        # score for docs 0, 1, .., n_rep, For each topic
        topic_docsScore = self.topics_docsScore(topicsLen_in, n_rep_in, top_tf_in)
        # average for each topic
        topic_average = self.topics_average(topic_docsScore, topicsLen_in, n_rep_in)

        return topic_docsScore, topic_average

    # Generating Summarized Text
    def genSummary(self, topicsLen_in, n_rep_in, top_rawDoc_in):
        topicsLen = topicsLen_in
        n_rep = n_rep_in
        top_rawDoc = top_rawDoc_in
        topic_average = self.topic_average
        topic_docsScore = self.topic_docsScore

        summary = """"""

        for i in range(topicsLen):
            for j in range(n_rep):
                if topic_docsScore[i][j] > topic_average[i]:
                    summary += top_rawDoc[i][j]
            
            summary += '\n\n'

        self.summary = summary

    def __init__(self, topicsLen_in, n_rep_in, top_tf_in, top_rawDoc_in):
        topicsLen = topicsLen_in
        n_rep = n_rep_in
        top_tf = top_tf_in
        top_rawDoc = top_rawDoc_in

        self.topic_docsScore, self.topic_average = self.topics_docsScore_average(topicsLen, n_rep, top_tf)
        self.genSummary(topicsLen, n_rep, top_rawDoc)

    def getSummary(self):
        return self.summary