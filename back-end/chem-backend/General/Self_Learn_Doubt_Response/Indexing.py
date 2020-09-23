import math
import numpy as np


class Indexing(object):

    def unique_words(self, plot_data):
        l = plot_data[0]
        flatten = [item for sublist in l for item in sublist]
        words = flatten
        unique_words = list(words)
        print("unique words")
        print(unique_words)
        return unique_words

    def tf(self, word1, doc):
        return doc.count(word1) / len(doc)

    def n_containing(self, word, document_list):
        return sum(1 for doc in document_list if word in doc)

    def idf(self, word, document_list):
        return math.log(len(document_list) / (0.01 + self.n_containing(word, document_list)))

    def tfidf(self, word, doc, document_list):
        return self.tf(word, doc) * self.idf(word, document_list)

    def index(self, plot_data):
        plottest = plot_data[0][0:1000]

        word_dic = {}
        words_unique = self.unique_words(plot_data)

        for doc in plottest:
            for word in words_unique:
                if word in doc:
                    word = str(word)
                    index = plottest.index(doc)
                    positions = list(np.where(np.array(plottest[index]) == word)[0])
                    idfs = self.tfidf(word, doc, plottest)
                    try:
                        word_dic[word].append([index, positions, idfs])
                    except:
                        word_dic[word] = []
                        word_dic[word].append([index, positions, idfs])
        np.save('word_dic.npy', word_dic)
        print('word dictionary')
        print(word_dic)
        return word_dic
