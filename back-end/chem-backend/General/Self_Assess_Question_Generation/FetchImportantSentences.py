"""
    Using Term Frequency method and entity type extracting the most important sentences
"""

import nltk;
import re;
import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")


class FetchImportantSentences(object):

    def _prettify(self, text):
        """
        words list without stopwords
        :param text: text paragraph
        :return: words list without stopwords
        """
        ##removing the stopwords and convert to lowercase
        stopwords = nltk.corpus.stopwords.words('english');
        text_in_lowercase = re.sub("[^a-zA-Z]", " ", str(text)).split(" ");
        filtered_text = []
        for word in text_in_lowercase:
            if word not in stopwords:
                filtered_text.append(word);

        return filtered_text;

    def _uniqueWords(self,words):
        # wordsList = ['matter','chemical bonds','cation','anion','ionic bonds','polarity','inter molecular bond']
        """
        unique words set
        :param words: words without stopwords
        :return: unique words set
        """
        unique_words_set = set(words);
        return list(unique_words_set);

    def _countWords(self,words):
        """
        word count for each unique word
        :param words: all the words without stopwords
        :return: a dictionary of {WORD: COUNT} where count is
                 how many times that word appears in "words".
        """

        unique_words = self._uniqueWords(words);

        dict = {};
        # for every single unique word
        for i in range(len(unique_words)):
            dict[unique_words[i]] = 0
            # see how many times this unique word appears in all words
            for x in range(len(words)):
                if unique_words[i] == words[x]:
                    dict[unique_words[i]] = dict[unique_words[i]] + 1;
        return dict;

    def _termFrequency(self,text):
        """
        Calculating term frequency for each sentence
        :param text: pre processed text para
        :return: important sentences
        """
        words_without_stopwords = self._prettify(text);
        length = len(str(text).split(" "))
        # getting the sentences from text
        blob = TextBlob(text)
        sentences = set()
        text = ''
        for sentence in blob.sentences:
            text = text + str(sentence) + " ";
        # print(text)
        sentence = str(text).split(".")
        sentences = sentence
            # sentences.append(sentence);
        TFVals = self._countWords(words_without_stopwords)
        # actually makes it TF values according to formula
        print(" ")
        for z in TFVals:
            TFVals[z] = TFVals[z] / length;
            # print("WORD : " + z, ", TF VALUE :" + str(TFVals[z]))
        # splits it up into sentences now
        TFSentences = {};
        # for every sentence
        for i in range(len(sentences)-1):
            # for every word in that sentence
            sentence_split_words = sentences[i].split(" ");
            # get the assiocated TF values of each word
            # temp.add is the "TF" value of a sentence, we need to divide it at the end
            temp_add = 0.0;
            words_no_stop_words_length = len(self._prettify(sentences[i]));
            for x in range(len(sentence_split_words)-1):
                # get the assiocated TF value and add it to temp_add
                if sentence_split_words[x].lower() in TFVals:
                    # adds all the TF values up
                    temp_add = temp_add + TFVals[sentence_split_words[x].lower()];

            # TF sentences divide by X number of items on top
            TFSentences[sentences[i]] = temp_add / len(sentence_split_words);

        return TFSentences;

    def _checkPersonEntity(self,sentence):
        words = nltk.word_tokenize(sentence);
        tagged = nltk.pos_tag(words);
        chunks = nltk.ne_chunk(tagged);
        personCount = 0;
        for chunk in chunks:
            if type(chunk) is nltk.Tree:
                for c in chunk.leaves():
                    if str(chunk.label).find('PERSON') != -1:
                        personCount = personCount + 1;

        return personCount;

    def importantSentences(self,text):
        print("")
        print("-----------------QUESTION GENERATABLE SENTENCE SELECT START")
        print("")
        print("----------TERM FREQUENCY BASED ALGORITHM START-----------")
        print("")
        print("-------INPUT PARAGRAPH START--------")
        print(text)
        print("-------INPUT PARAGRAPH END--------")
        # calculates TF
        TFVals = self._termFrequency(text);
        print("")
        print("-------CALCULATED TERM FREQUENCY VALUES START--------")
        for tfVal in TFVals:
            print(tfVal + " : " + str(TFVals[tfVal]))
        print("-------CALCULATED TERM FREQUENCY VALUES END--------")
        important_sentence_list = set();
        count=0.0
        for tf in TFVals:
            count = count + TFVals[tf]
        if len(TFVals) != 0:
            average = count / len(TFVals)
            print("")
            print("AVERAGE TF VALUE TO PARAGRAPH : " + str(average))
        # print("AVERAGE :" + str(average))
            sentences = str(text).split(".")
            optimalVal = 10
            for tf in TFVals:
                if len(sentences) < optimalVal:
                    print("")
                    print("----------SENTENCE THAT IS NOT OPTIMAL START ----------")
                    print("")
                    percentage = (optimalVal - len(sentences)) / optimalVal
                    variable = (average - (average * percentage))
                    print("UPDATED AVERAGE : " + str(average))
                    print("-----IMPORTANT SENTENCE AFTER UPDATING AVERAGE START ------")
                    # print("DECREASED AVERAGE " + str(variable))
                    if TFVals[tf] >= variable:
                        important_sentence_list.add(str(tf))
                        print(tf + " : " + str(TFVals[tf]))
                    print("-----IMPORTANT SENTENCE AFTER UPDATING AVERAGE END ------")
                    print("")
                    print("----------SENTENCE THAT IS NOT OPTIMAL END ----------")
                    print("")
                else:

                    if TFVals[tf] >= average:
                        print("")
                        print("-----IMPORTANT SENTENCE WITHOUT UPDATING AVERAGE START ------")
                        important_sentence_list.add(str(tf))
                        print(tf + " : " + str(TFVals[tf]))
                        print("-----IMPORTANT SENTENCE WITHOUT UPDATING AVERAGE END ------")
                        print("")
                count = self._checkPersonEntity(str(tf));
                if count != 0:
                    important_sentence_list.add(str(tf));
                if str(tf).find("because") != -1:
                    important_sentence_list.add(str(tf));
        else:
            for tf in TFVals:
                count = self._checkPersonEntity(str(tf));
                if count != 0:
                    important_sentence_list.add(str(tf));
                if str(tf).find("because") != -1:
                    important_sentence_list.add(str(tf));
        print("")
        print("------------IMPORTANT SENTENCES START-----------")
        print("")
        for sentence in important_sentence_list:
            print(sentence)
        print("")
        print("------------IMPORTANT SENTENCES END-----------")
        print("")
        print("----------TERM FREQUENCY BASED ALGORITHM END-----------")
        print("")
        print("-----------------QUESTION GENERATABLE SENTENCE SELECT END")
        print("")
        return important_sentence_list;

    def testImportantSentences(self,text,optimalval):
        # calculates TF
        TFVals = self._termFrequency(text);
        important_sentence_list = set();
        count=0.0
        for tf in TFVals:
            count = count + TFVals[tf]
        if len(TFVals) != 0:
            average = count / len(TFVals)
        # print("AVERAGE :" + str(average))
            sentences = str(text).split(".")
            optimalVal = optimalval
            for tf in TFVals:
                if len(sentences) < optimalVal:
                    percentage = (optimalVal - len(sentences)) / optimalVal
                    variable = (average - (average * percentage))
                    # print("DECREASED AVERAGE " + str(variable))
                    if TFVals[tf] >= variable:
                        important_sentence_list.add(str(tf))
                else:
                    if TFVals[tf] >= average:
                        important_sentence_list.add(str(tf))

                count = self._checkPersonEntity(str(tf));
                if count != 0:
                    important_sentence_list.add(str(tf));
                if str(tf).find("because") != -1:
                    important_sentence_list.add(str(tf));
        else:
            for tf in TFVals:
                count = self._checkPersonEntity(str(tf));
                if count != 0:
                    important_sentence_list.add(str(tf));
                if str(tf).find("because") != -1:
                    important_sentence_list.add(str(tf));
        return important_sentence_list;

    def extractSentences(self,text):
        blob = TextBlob(text)
        sentences = set()
        text = ''
        for sentence in blob.sentences:
            print(sentence)
            text = text + str(sentence) + " ";
        print(text)
        sentence = str(text).split(".")
        sentences = sentence
        print(len(sentences))
        return sentences;