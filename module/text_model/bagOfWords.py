
class bow():
    def set_doc_term_matrix(self, doc_term_matrix_in):
        self.doc_term_matrix = doc_term_matrix_in

    def get_doc_term_matrix(self):
        return self.doc_term_matrix

    def __init__(self, docs_terms_list_in, dictionary_in):
        docs_terms_list = docs_terms_list_in
        dictionary = dictionary_in

        doc_term_matrix = [dictionary.doc2bow(doc) for doc in docs_terms_list]

        self.set_doc_term_matrix(doc_term_matrix)
