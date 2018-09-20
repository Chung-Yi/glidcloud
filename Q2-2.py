import nltk
import math
from nltk.util import ngrams


def calc_probabilities(text):
    tokensize = text.split()
    unigram_p = {}
    bigram_p = {}
    trigram_p = {}


    unigram = {}
    bigram = {}
    trigram = {}


    uni_count = 0

    # for sentence in content:
    #     sentence += 'STOP'
    #     tokens = nltk.word_tokenize(sentence)


    # build unigram dictionary
    for word in tokensize:
        uni_count += 1
        if word in unigram:
            unigram[word] += 1
        else:
            unigram[word] = 1

    # build bigram dictionary
    bigrams = ngrams(tokensize,2)
    bigram_tuples = tuple(bigrams)
    for item in bigram_tuples:
            if item in bigram:
                bigram[item] += 1
            else:
                bigram[item] = 1
    
    # build trigram dictionary
    trigrams = ngrams(tokensize,3)
    trigram_tuples = tuple(trigrams)
    for item in trigram_tuples:
            if item in bigram:
                trigram[item] += 1
            else:
                trigram[item] = 1


    # calculate unigram probability
    for word in unigram:
        temp = [word]
        unigram_p[tuple(temp)] = math.log(float(unigram[word])/uni_count)

    # calculate bigram probability
    for word in bigram:
            bigram_p[tuple(word)] = math.log(float(bigram[word])/unigram[word[0]])

    # calculate trigram probability
    for word in trigram:
            trigram_p[tuple(word)] = math.log(float(trigram[word])/bigram[(word[0], word[1])])
   
    return unigram_p, bigram_p, trigram_p

def prob3(unigrams, bigrams, trigrams):
    #output probabilities
    outfile = open('prob.txt', 'w')
    for unigram in unigrams:
        outfile.write('UNIGRAM ' + unigram[0] + ' ' + str(unigrams[unigram]) + '\n')
    for bigram in bigrams:
        outfile.write('BIGRAM ' + bigram[0] + ' ' + bigram[1]  + ' ' + str(bigrams[bigram]) + '\n')
    for trigram in trigrams:
        outfile.write('TRIGRAM ' + trigram[0] + ' ' + trigram[1] + ' ' + trigram[2] + ' ' + str(trigrams[trigram]) + '\n')
    outfile.close()


if __name__ == '__main__':
    # open data
    f = open('raw_sentences.txt','r')
    content = f.read()
    text = content.lower()
    f.close()
    # text = content.lower()
    unigrams, bigrams, trigrams = calc_probabilities(text)
    prob3(unigrams, bigrams, trigrams)
    