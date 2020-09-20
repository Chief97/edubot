"""
    NLP techniques for pre-processing,
    encode the pre-processed words by creating training data,
    Build Random Forest Classifier model,
    train the model
"""

import random
import nltk
import json
import numpy as np
import pickle
from nltk.stem.lancaster import LancasterStemmer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

nltk.download('punkt')
stemmer = LancasterStemmer()


class DoubtDetection(object):
    # import dataset as JSON file
    file = open('../intents.json', )
    intents = json.load(file)

    # Tokenizing the sentences in the dataset
    token_words = []  # assigning array for tokenized words
    intent_ids = []   # assigning array for intent IDs
    corpus = []       # assigning array for tokenized words, respective intent ID

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            words = nltk.word_tokenize(pattern)
            token_words.extend(words)
            corpus.append((words, intent['intent_id']))

            if intent['intent_id'] not in intent_ids:
                intent_ids.append(intent['intent_id'])

    # Stemming the tokenized words
    stemmed_words = [stemmer.stem(word.lower()) for word in token_words
                     if word not in ["?", "'s", "+", ",", "(", ")", "-"]]
    stemmed_words = sorted(list(set(stemmed_words)))  # remove duplicate stemmed words
    intent_ids = sorted(list(set(intent_ids)))  # remove duplicate intent_id words

    # Create training data in encoded form
    training = []
    output_empty = [0] * len(intent_ids)

    # Create training set, bag of words for each sentence
    for doc in corpus:
        bag = []
        intent_words = doc[0]
        intent_words = [stemmer.stem(word.lower()) for word in intent_words]

        # Create bag of words array
        for w in stemmed_words:
            bag.append(1) if w in intent_words else bag.append(0)

        output_feature = list(output_empty)
        output_feature[intent_ids.index(doc[1])] = 1
        training.append([bag, output_feature])

    random.shuffle(training)  # Shuffling features
    training = np.array(training)

    # Creating training lists
    train_x = list(training[:, 0])
    train_y = list(training[:, 1])

    # Split the data into training and testing sets
    train_x, test_x, train_y, test_y = train_test_split(train_x, train_y, test_size=0.02)

    # Instantiate model with 10 decision trees
    rf = RandomForestRegressor(n_estimators=10, random_state=1)

    # Train the model on training data
    rf.fit(train_x, train_y)

    # Test the models accuracy on the training data
    model = rf
    print("Train Accuracy : ", model.score(train_x, train_y))
    print("Test Accuracy : ", model.score(test_x, test_y))

    # save the model using pickle
    pickle.dump({
        "stemmed_words": stemmed_words,
        "intent_ids": intent_ids,
        "train_x": train_x,
        "train_y": train_y},
        open('training_data', 'wb')
    )

