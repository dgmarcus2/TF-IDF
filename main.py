import util
import tfidf


data     = util.read_data('book.txt')
chapters = util.split_chapters(data)
corpus   = util.clean_chapters(chapters)[0:3]
tfidf.tfidf(corpus, 10)


