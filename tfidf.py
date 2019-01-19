import collections
import math
import util


def tfidf(corpus, top_n):
  #num of documents for idf
  doc_len = len(corpus)

  words = {}
  idfs = {}
  chapcount = 1


  for chapter in corpus:
    prepped_tokens = util.tokenize_prep(chapter)
    tokens = util.split_into_tokens(prepped_tokens)
    #dict of terms and # of apperances, for calculating idf
    for i in tokens:
      if not i in words:
        words[i] = 0
    #list of words in chapter
    uniq_tokens = []
    for i in tokens:
      if not i in uniq_tokens:
        uniq_tokens.append(i)
    #determine number of chapters a word appears in
    for i in uniq_tokens:
      if i in words:
        words[i] += 1

  #calculate idfs
  for key, val in words.items():
    idf = -1.0 * (math.log10(val/doc_len))
    idfs[key] = idf

  for chapter in corpus:
    tfidf = {}
    prepped_tokens = util.tokenize_prep(chapter)
    tokens = util.split_into_tokens(prepped_tokens)
    length = len(tokens)
    #generates tf map
    tf_map = collections.Counter(tokens)
    for k,v in tf_map.items():
      #calculate tfs
      tf = v/length
      #print(k, tf)
      idf = idfs[k]
      tf_idf = tf * idf
      tfidf[k] = tf_idf
    sorted_tfidf = sorted(tfidf.items(), key = lambda v: v[1], reverse=True)
    top = sorted_tfidf[0:top_n]
    print("Document: {}".format(chapcount))
    for i in top:
      print(" Word: {:14.12} TF-IDF: {:10.5f}".format(i[0], round(i[1], 5)))
    chapcount += 1



  
