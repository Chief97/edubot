import pandas as pd
import numpy as np
import bs4 as bs
import string
import random
import math

import nltk
from nltk.corpus import brown
from nltk.corpus import reuters

from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer


# currently loading random documents to show
def load_data():
    data_frame = pd.read_csv("D:\SLIIT\Y4S1\CDAP\Develop\2020-100\back-end\chem-backend\General"
                             "\Self_Learn_Doubt_Response\webScraper\webScraper\spiders\data.csv")
    return data_frame


# removing html
def remove_html(text):
    soup = bs.BeautifulSoup(text, 'lxml')
    html_free = soup.get_text()
    return html_free


# removing punctuations
def remove_punctuation(text):
    exclude = set(string.punctuation)
    no_punct = "".join(c for c in text if c not in exclude)
    return no_punct


def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    s_words = [w for w in text if w not in stop_words]
    return s_words


def word_stemmer(text):
    stemmer = PorterStemmer()
    stemmed_txt = " ".join([stemmer.stem(i) for i in text])
    return stemmed_txt


def preprocessing():
    df = load_data()

    # remove html
    df['activity'] = df['activity'].apply(lambda txt: remove_html(txt))
    df['notes'] = df['notes'].apply(lambda txt: remove_html(txt))
    df['reaction'] = df['reaction'].apply(lambda txt: remove_html(txt))

    # remove punctuation
    df['images'] = df['images'].apply(lambda txt: remove_punctuation(txt))
    df['definition'] = df['definition'].apply(lambda txt: remove_punctuation(txt))
    df['activity'] = df['activity'].apply(lambda txt: remove_punctuation(txt))
    df['notes'] = df['notes'].apply(lambda txt: remove_punctuation(txt))
    df['reaction'] = df['reaction'].apply(lambda txt: remove_punctuation(txt))

    # tokenizing the words
    tokenizer = RegexpTokenizer(r'\w+')
    df['definition'] = df['definition'].apply(lambda txt: tokenizer.tokenize(txt.lower()))
    df['activity'] = df['activity'].apply(lambda txt: tokenizer.tokenize(txt.lower()))
    df['notes'] = df['notes'].apply(lambda txt: tokenizer.tokenize(txt.lower()))
    df['reaction'] = df['reaction'].apply(lambda txt: tokenizer.tokenize(txt.lower()))

    # removing the stopwords
    df['images'] = df['images'].apply(lambda txt: remove_stopwords(txt))
    df['definition'] = df['definition'].apply(lambda txt: remove_stopwords(txt))
    df['activity'] = df['activity'].apply(lambda txt: remove_stopwords(txt))
    df['notes'] = df['notes'].apply(lambda txt: remove_stopwords(txt))
    df['reaction'] = df['reaction'].apply(lambda txt: remove_stopwords(txt))

    # stem words
    df['images'] = df['images'].apply(lambda txt: word_stemmer(txt))
    df['definition'] = df['definition'].apply(lambda txt: word_stemmer(txt))
    df['activity'] = df['activity'].apply(lambda txt: word_stemmer(txt))
    df['notes'] = df['notes'].apply(lambda txt: word_stemmer(txt))
    df['reaction'] = df['reaction'].apply(lambda txt: word_stemmer(txt))


# CREATING AN INVERSE-INDEX
# Create inverse index which gives document number for each document and where word appears

# creating a list of all words
l = plot_data[0]
flatten = [item for sublist in l for item in sublist]
words = flatten
wordsunique = set(words)
wordsunique = list(wordsunique)

# create functions for TD-IDF

from textblob import TextBlob as tb


def tf(word, doc):
    return doc.count(word) / len(doc)


def n_containing(word, doclist):
    return sum(1 for doc in doclist if word in doc)


def idf(word, doclist):
    return math.log(len(doclist) / (0.01 + n_containing(word, doclist)))


def tfidf(word, doc, doclist):
    return (tf(word, doc) * idf(word, doclist))


# Create dictonary of words
import re
import numpy as np

plottest = plot_data[0][0:1000]

worddic = {}

for doc in plottest:
    for word in wordsunique:
        if word in doc:
            word = str(word)
            index = plottest.index(doc)
            positions = list(np.where(np.array(plottest[index]) == word)[0])
            idfs = tfidf(word, doc, plottest)
            try:
                worddic[word].append([index, positions, idfs])
            except:
                worddic[word] = []
                worddic[word].append([index, positions, idfs])

worddic['china']

# pickel (save) the dictonary to avoid re-calculating
np.save('worddic_1000.npy', worddic)
