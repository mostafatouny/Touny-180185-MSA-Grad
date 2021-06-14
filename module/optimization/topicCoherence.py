from module.topic_modeling.latentDirichletAllocation import lda
from gensim.models import CoherenceModel

class topicCoherence():

    def setOptimalModel(self, model_in):
        self.ldaOpt = model_in

    def getOptimalModel(self):
        return self.ldaOpt

    def topic_model_coherence_generator(self, bow_in, doc_terms_in, dictionary_in, start_topic_count_in, end_topic_count_in, step_in):
        bow = bow_in
        doc_terms = doc_terms_in
        dictionary = dictionary_in
        start_topic_count = start_topic_count_in
        end_topic_count = end_topic_count_in
        step = step_in

        doc_term_matrix = bow.get_doc_term_matrix()

        prev_model = None
        prev_coherenceScore = 0

        for topic_nums in (range(start_topic_count, end_topic_count+1, step)):
            ldaOb = lda(bow, dictionary, topic_nums)

            coherence_model = CoherenceModel(model=ldaOb.get_lda(), corpus=doc_term_matrix, texts=doc_terms, dictionary=dictionary) #topn=20
            coherence_score = coherence_model.get_coherence()

            assert(coherence_score > 0), "a coherence score is equal or less than zero"
            if coherence_score < prev_coherenceScore:
                self.setOptimalModel(prev_model)
                return
            
            prev_model = ldaOb
            prev_coherenceScore = coherence_score

        self.setOptimalModel(prev_model) #latest model in this case
        

    def __init__(self, bow_in, doc_terms_in, dictionary_in, start_topic_count_in=2, end_topic_count_in=9, step_in=3):
        bow = bow_in
        doc_terms = doc_terms_in
        dictionary = dictionary_in
        start_topic_count = start_topic_count_in
        end_topic_count = end_topic_count_in
        step = step_in

        self.topic_model_coherence_generator(bow, doc_terms, dictionary, start_topic_count, end_topic_count, step)
