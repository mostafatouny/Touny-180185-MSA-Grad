from nltk.corpus import stopwords
import re

import module.filterData.constant_REs as con_REs


def ReFromReList(ReList_in):
  r = ""

  for re_i in ReList_in:
    r = r + '('
    r = r + re_i
    r = r + ')'
    r = r + '|'

  r = r[:-1]

  return r

def filterStrFromReList(ReList_in, str_in):
  ReList = ReList_in
  s = str_in

  r = ReFromReList(ReList)

  return re.sub(r, '', s)

#####

def replaceNewLinesWith(str_in, repBy_in):
  s = str_in
  repBy = repBy_in

  return re.sub(r'\n+', repBy, s)

def stripBegEnd(str_in, chars_in=" .,'"):
  s = str_in
  chars = chars_in

  return s.strip(chars)

def removeDuplicatedChar(str_in, char_in):
  s = str_in
  ch = char_in

  assert(ch!='.'), "dot, i.e period '.', should be used here"

  return re.sub(char_in+'+', char_in, s)

def removeDuplicatedCharList(str_in, charList_in):
  charList = charList_in
  s = str_in

  for ch in charList:
    s = removeDuplicatedChar(s, ch)

  return s

def removeDuplicatedPeriods(str_in):
  s = str_in

  return re.sub(con_REs.DUPLICATED_PERIODS, '.', s)

def removeDuplicatedCharSeq(str_in):
  s = str_in
  # alternatively, replace with '. '
  return re.sub(con_REs.SPECIAL_CHAR_SEQ, '.', s)

#####

def lowerAndTermsList_docList_in(docList_in):
  docList = docList_in

  return [el.lower().split(' ') for el in docList]

def removeStopwordsFromDocList(docList_in):
  docList = docList_in

  STOPWORDS = set(stopwords.words('english'))

  return [ [el for el in doc if el not in STOPWORDS] for doc in docList]

#####

#def filterEmojis(str_in):
#  stri = str_in
#
#  emoji_pattern = re.compile(con_REs.EMOJIS, flags=re.UNICODE)
#
#  return emoji_pattern.sub(r'', stri)

#def filterEmojis(str_in):
#  stri = str_in
#
#	# source: https://gist.github.com/slowkow/7a7f61f495e3dbb7e3d767f97bd7304b
#  emoji_pattern = re.compile("["
#                               u"\U0001F600-\U0001F64F"  # emoticons
#                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
#                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                               u"\U00002500-\U00002BEF"  # chinese char
#                               u"\U00002702-\U000027B0"
#                               u"\U00002702-\U000027B0"
#                               u"\U000024C2-\U0001F251"
#                               u"\U0001f926-\U0001f937"
#                               u"\U00010000-\U0010ffff"
#                               u"\u2640-\u2642"
#                               u"\u2600-\u2B55"
#                               u"\u200d"
#                               u"\u23cf"
#                               u"\u23e9"
#                               u"\u231a"
#                               u"\ufe0f"  # dingbats
#                               u"\u3030"
#                               "]+", flags=re.UNICODE)
#
#  return emoji_pattern.sub(r'', stri)