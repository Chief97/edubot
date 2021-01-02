"""
    Pre processing the user input by tokenizing and stemming,
    create bag of array that contain 0 or 1 for each word in
    the bag that exists in the user input,
    predict the intent id for the user question
"""

import pickle
import json
import nltk
import numpy as np

from nltk.stem.lancaster import LancasterStemmer
from General.Self_Learn_Doubt_Detection.DoubtDetection import DoubtDetection

stemmer = LancasterStemmer()
model = DoubtDetection.model


class ClassifyInput(object):
    # restoring all the data structures from the trained model
    data = pickle.load(open("training_data", "rb"))
    stemmed_words = data['stemmed_words']
    intent_ids = data['intent_ids']
    train_x = data['train_x']
    train_y = data['train_y']

    with open('../intents.json') as json_data:
        intents = json.load(json_data)

    def preProcessInput(self, sentence):

        """
        Pre-processing the user input : Tokenizing and stemming
        :param sentence: user input
        :return: list of stemmed words in the input
        """

        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words

    def bow(self, sentence, s_words, show_details=False, ):
        """
        returning bag of words array: 0 or 1 for each word in
        the bag that exists in the sentence
        :param show_details:
        :param sentence : input text or user question
        :param s_words : stemmed words in the training dataset
        :return : bag of words array
        """
        sentence_words = self.preProcessInput(sentence)
        bag = [0] * len(s_words)
        for s in sentence_words:
            for i, w in enumerate(s_words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print("found in bag: %s" % w)

        return np.array(bag)

    def classify(self, sentence):
        """
        Predict the intent_id for the user question using
        the trained model,
        return intent id, if probability value greater than
        THRESHOLD value
        :param sentence: input text or user question
        :return: intent_id for the input
        """
        THRESHOLD = 0.5

        results = model.predict([self.bow(sentence, self.stemmed_words)])[0]
        results = [[i, r] for i, r in enumerate(results) if r > THRESHOLD]
        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append((self.intent_ids[r[0]]))

        return return_list
