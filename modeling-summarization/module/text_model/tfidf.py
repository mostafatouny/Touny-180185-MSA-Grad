from sklearn.feature_extraction.text import TfidfTransformer

#import numpy as np
#from math import log as log

class tfidf():
    # numpy, log here
    #def tfVecTOtfidfVec(self, a): #numpy array in
    #    corpusSize = len(a)
    #    idfMap = lambda x: log(float(corpusSize)/(x+1))
    #    return np.array([idfMap(x) for x in a])

    def setMat(self, Mat_in):
        self.Mat = Mat_in

    def getMat(self):
        return self.Mat

    def setFeatureNames(self, featureNames_in):
        self.featureNames = featureNames_in

    def getFeatureNames(self):
        return self.featureNames

    #####

    def getTermIndFromTerm(self, term_in):
        termInd = self.featureNames.index(term_in)
        return termInd

    def getVectorFromTerm(self, term_in):
        termInd = self.getTermIndFromTerm(term_in)
        tfidfMat = self.getMat()
        return [row[0] for row in tfidfMat[:, termInd].toarray()]

    #####

    def __init__(self, bow_in):
        bow = bow_in

        self.setFeatureNames( bow.getFeatureNames() )

        tfidfTr = TfidfTransformer()
        tfidfMat = tfidfTr.fit_transform(X=bow.getMatrix(), y=self.getFeatureNames)
        self.setMat(tfidfMat)
        