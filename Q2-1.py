import nltk, collections
from nltk.util import ngrams
from nltk.collocations import BigramCollocationFinder
from  nltk.metrics import BigramAssocMeasures


def ngram_probs(filename='raw_sentences.txt'):
    f = open(filename,'r')
    content = f.read()
    text = content.lower()
    #tokensize = nltk.word_tokenize(text)
    tokensize = text.split()

    bigrams = ngrams(tokensize,2)
    bigramfreq = collections.Counter(bigrams)
    tigrams = ngrams(tokensize,3)
    tigramfreq = collections.Counter(tigrams)
    return bigramfreq, tigramfreq
    
    


if __name__ == '__main__':
     cnt2, cnt3= ngram_probs()
     print(cnt2, cnt3)
    # print(cnt2.most_common(10))
# finder = BigramCollocationFinder.from_words(text)


# print(finder.nbest(BigramAssocMeasures.likelihood_ratio,20))

# print(text)