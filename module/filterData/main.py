import module.filterData.handy as filterData
import module.filterData.constant_REs as con_REs

def filterTweets(text_list_in):
    text_list = text_list_in

    # replace new lines with a fullstop
    text_list = [filterData.replaceNewLinesWith(x, '.') for x in text_list]

    # distill mentions, links, hashtags, emojis, numbers and special characters
    temReLis = [con_REs.MENTIONS, con_REs.LINKS, con_REs.HASHTAG, con_REs.EMOJIS, con_REs.NUMBERS, con_REs.SPECIAL_CHAR, con_REs.RT, con_REs.AMP]
    text_list = [filterData.filterStrFromReList(temReLis, x) for x in text_list]
    
    # strip beginning and ending
    text_list = [filterData.stripBegEnd(x) for x in text_list]
    
    # remove duplicated periods and spaces
    text_list = [filterData.removeDuplicatedCharList(x, [' ']) for x in text_list] # don't use dot, i.e period "." here
    text_list = [filterData.removeDuplicatedPeriods(x) for x in text_list]
    
    # ensure either a space or a period separates terms
    text_list = [filterData.removeDuplicatedCharSeq(x) for x in text_list]
    
    # Chunk Tweets of Multiple Sentences by separating on fullstops
    new_text_list = []
    for el in text_list:
        new_text_list = new_text_list + el.split('.')
    
    #####
    
    text_list = new_text_list

    # a doc as list of terms representation
    new_text_list = filterData.lowerAndTermsList_docList_in(new_text_list)
    
    # remove stop words
    new_text_list = filterData.removeStopwordsFromDocList(new_text_list)
    
    # lemmatize terms
    new_text_list = [ [filterData.lemmatizeTerm(term) for term in doc] for doc in new_text_list]

    return text_list, new_text_list