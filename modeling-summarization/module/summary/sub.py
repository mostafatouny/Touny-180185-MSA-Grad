def docsInd_To_rawDoc_tf(topicsLen_in, top_ind_in, bow_in, text_in):
    bow = bow_in

    # via indices, Get concrete raw docs and their corresponding tf vectors
    top_tf = []
    top_rawDoc = []

    for i in range(topicsLen_in):
        # for topic i, get its sorted indices
        indicesList = top_ind_in[i]
        # sorted raw docs
        top_tf.append(bow.getVectorsFromIndices(indicesList))
        # sorted tf vectors

        top_rawDoc.append(bow.getRawDocsFromIndices(indicesList, text_in))

    return top_rawDoc, top_tf

    #top_tf

    # [ array of topic
    #    [ 1st doc
    #      [doc-tf]
    #    ]
    #    [ 2nd doc
    #      []
    #    ]
    #    [ 3rd doc
    #      []
    #    ]
    #    ..
    #    .
    #
    # ]
    # use toarray() to print out data values

    # similar structure for top_rawDoc and top_ind