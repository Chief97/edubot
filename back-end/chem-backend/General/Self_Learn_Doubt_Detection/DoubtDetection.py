import random
import nltk
import json
import numpy as np
import pickle
from nltk.stem.lancaster import LancasterStemmer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split  # Using Skicit-learn to split data into training and testing sets

nltk.download('punkt')
stemmer = LancasterStemmer()


class DoubtDetection(object):
    # opening JSON file
    file = open('../intents.json',)
    intents = json.load(file)

    # Tokenizing
    token_words = []  # each tokenized words
    pattern_id = []  # class name
    corpus = []  # stemmed words as class wise
    # ignore = ['?']

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            words = nltk.word_tokenize(pattern)
            token_words.extend(words)
            corpus.append((words, intent['class']))

            if intent['class'] not in pattern_id:
                pattern_id.append(intent['class'])  # add class to pattern_id
    # print(pattern_id)
    # print(token_words)
    # print(corpus)

    # Stemming
    stemmed_words = [stemmer.stem(word.lower()) for word in token_words if
                     word not in ["?", "'s", "+", ",", "(", ")", "-"]]
    stemmed_words = sorted(list(set(stemmed_words)))  # set used remove duplicate stemmed words

    pattern_id = sorted(list(set(pattern_id)))  # remove deplicate class words

    # print(len(corpus), " Tokenized sentence class wise : ", corpus)
    # print(len(pattern_id) ," Classes : ", pattern_id)
    # print(" unique stemmed words : ", stemmed_words)
    # print(len(stemmed_words))

    # Create training data
    training = []
    output = []

    # Create an empty array for output
    output_empty = [0] * len(pattern_id)

    # Create training set, bag of words for each sentence
    for doc in corpus:
        # initialize bag of words
        bag = []
        # List of tokenized words for the pattern
        pattern_words = doc[0]
        # Stemming each word
        pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]

        # Create bag of words array
        for w in stemmed_words:
            bag.append(1) if w in pattern_words else bag.append(0)
        # print(bag)
        output_feature = list(output_empty)
        output_feature[pattern_id.index(doc[1])] = 1

        training.append([bag, output_feature])
    # print(training)
    # s Shuffling features and training it into np.array
    random.shuffle(training)
    training = np.array(training)

    # Creating training lists
    train_x = list(training[:, 0])
    train_y = list(training[:, 1])

    # print(train_x)
    # print(train_y)

    # Split the data into training and testing sets
    train_x, test_x, train_y, test_y = train_test_split(train_x, train_y, test_size=0.25)

    # Import the model we are using

    # Instantiate model with 1000 decision trees
    rf = RandomForestRegressor(n_estimators=10, random_state=1)

    # Train the model on training data
    rf.fit(train_x, train_y)

    # Test the models accuracy on the training data
    model = rf
    # print("Accuracy : ", model.score(train_x, train_y))

    pickle.dump({
        "stemmed_words": stemmed_words,
        "pattern_id": pattern_id,
        "train_x": train_x,
        "train_y": train_y},
        open('training_data', 'wb')
    )

    # restoring all the data structures
    data = pickle.load(open("training_data", "rb"))
    stemmed_words = data['stemmed_words']
    pattern_id = data['pattern_id']
    train_x = data['train_x']
    train_y = data['train_y']

    with open('../intents.json') as json_data:
        intents = json.load(json_data)

    def clean_up_sentence(self, sentence):
        # tokenizing the pattern
        sentence_words = nltk.word_tokenize(sentence)
        # stemming each word
        sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words

    # returning bag of words array: 0 or 1 for each word in the bag that exists in the sentence
    def bow(self, sentence, words, show_details=False):
        # tokenizing the pattern
        sentence_words = self.clean_up_sentence(sentence)
        # generating bag of words
        bag = [0] * len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print("found in bag: %s" % w)

        return (np.array(bag))

    def classify(self, sentence):
        THRESHOLD = 0.3

        # generate probabilities from the model
        results = self.model.predict([self.bow(sentence, self.stemmed_words)])[0]
        # filter out predictions below a threshold
        results = [[i, r] for i, r in enumerate(results) if r > THRESHOLD]
        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append((self.pattern_id[r[0]], r[1]))
        # return tuple of intent(i.e. tag) and probability

        return return_list
