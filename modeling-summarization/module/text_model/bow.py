from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

# Extending the CountVectorizer class with a lemmatizer
# Luckily for us, we have the latter option where we can extend the CountVectorizer class by overwriting the "build_analyzer" method
class LemmaCountVectorizer(CountVectorizer):
    def stem_lemm(self, w_in):
        w = w_in

        w = self.lemm.lemmatize(w)
        #w = self.stemm.stem(w)

        return w

    def __init__(self, *args, **kwargs):
        super(LemmaCountVectorizer, self).__init__(*args, **kwargs)
        self.stemm = PorterStemmer()
        self.lemm = WordNetLemmatizer()

    def build_analyzer(self):
        analyzer = super(LemmaCountVectorizer, self).build_analyzer()
        return lambda doc: (self.stem_lemm(w) for w in analyzer(doc))

class bagOfWords():
    def __init__(self, docList_in):
        tf_vectorizer = LemmaCountVectorizer(max_df=0.95, 
                                     min_df=2,
                                     stop_words='english',
                                     decode_error='ignore')
        self.matrix = tf_vectorizer.fit_transform(docList_in)
        self.featureNames = tf_vectorizer.get_feature_names()

        # tf to array
        # [0, 3, 1, .., 2, 0]
        # [ .. ]
        # ..
        # [.. ]

        # row i represents document i
        # column j represents feature j
        # entry i,j is document-tf

    def getFeatureNames(self):
        return self.featureNames

    def getMatrix(self):
        return self.matrix

    def getTermIndFromTerm(self, term_in):
        termInd = self.featureNames.index(term_in)
        return termInd

    def getVectorFromTerm(self, term_in):
        termInd = self.getTermIndFromTerm(term_in)
        return [row[0] for row in self.matrix[:, termInd].toarray()]

    def getVectorsFromIndices(self, indices_in):
        indicesList = indices_in

        bowMat = self.getMatrix()

        # via indices, get its tf vector
        tfVec = bowMat[indicesList] #tf is a numpy array

        return tfVec

    def getRawDocsFromIndices(self, indices_in, text_in):
        indicesList = indices_in
        text = text_in

        rawDocs = [text[i] for i in indicesList]  #text is a standard list

        return rawDocs

    #def getRawraw doc from indices