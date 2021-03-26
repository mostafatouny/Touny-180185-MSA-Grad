import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

from itertools import combinations

import module.model.LDA as ldaModel
import module.text_model.tfidf as tfidfCl


def cosineSimilarity(a, b): #works with list and np.array
    # single row matrix
    a = np.array([a])
    b = np.array([b])
    #a = np.array(a)
    #b = np.array(b)
    #a = a.reshape(1, -1)
    #b = b.reshape(1, -1)
    return cosine_similarity(a, b)
    #return dot(a, b)/(norm(a)*norm(b))



def calculate_coherence( term_rankings_in, bow_in ):
    bow = bow_in

    #tfidfOb = tfidfCl.tfidf()
    tfidfOb = tfidfCl.tfidf(bow)

    overall_coherence = 0.0

    for topic_index in range(len(term_rankings_in)):
        # check each pair of terms
        pair_scores = []
        for pair in combinations( term_rankings_in[topic_index], 2 ):
            #pair0_tfidf_vec = tfidfOb.tfVecTOtfidfVec(bow.getVectorFromTerm(pair[0]))
            #pair1_tfidf_vec = tfidfOb.tfVecTOtfidfVec(bow.getVectorFromTerm(pair[1]))
            pair0_tfidf_vec = tfidfOb.getVectorFromTerm(pair[0])
            pair1_tfidf_vec = tfidfOb.getVectorFromTerm(pair[1])
            pair_scores.append( cosineSimilarity(pair0_tfidf_vec, pair1_tfidf_vec) )
        # get the mean for all pairs in this topic
        topic_score = sum(pair_scores) / len(pair_scores)
        overall_coherence += topic_score
    # get the mean score across all topics
    return overall_coherence / len(term_rankings_in)



# generate models for a set of ks
# dependant on LDA
def genModels(ks_in, bog_in):
    bog = bog_in
    
    models = []

    for k in ks_in:
        lda = ldaModel.LDA(bog, k)
        models.append((k, lda))
    
    return models

# compute coherences of all models
def modelsCoherences(models_in, bog_in, n_of_top_terms_in):
    bogMat = bog_in.getMatrix()
    bogFeaNam = bog_in.getFeatureNames()

    k_values = []
    coherences = []

    for (k, l) in models_in:
        # Get all of the topic descriptors - the term_rankings, based on top 5 terms
        term_rankings = []
        for topic_index in range(k):
            #term_rankings.append( util.get_top_words( l, bogFeaNam, topic_index, n_of_top_terms_in ) )
            term_rankings.append(l.getTopWordsOfTopicInd(topic_index, n_of_top_terms_in))

        # Now calculate the coherence
        k_values.append( k )
        coherences.append( calculate_coherence( term_rankings, bog_in ) )

    return k_values, coherences

# Choose The Model of Optimal Topics Number
def getModelInd(k_values_in, coherences_in):
    coh_prev = 0
    
    for i in range(len(k_values_in)):
        if coherences_in[i] < coh_prev:
            return i-1
        coh_prev = coherences_in[i]

    return len(k_values_in)-1



def coherenceOptimize(ks_in, bog_in, n_of_top_terms_in):
    models = genModels(ks_in, bog_in)
    k_values, coherences = modelsCoherences(models, bog_in, n_of_top_terms_in)
    lda = models[getModelInd(k_values, coherences)][1]

    return lda