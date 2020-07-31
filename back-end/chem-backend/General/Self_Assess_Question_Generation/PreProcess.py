"""
    Pre processing the input paragraph,
    by replacing words in word dic and removing sentences
    that have a specific keyword..
"""

import nltk
import re


class PreProcess(object):

    wordDic = {
        'Therefore': '','this ': '','Those ': '','Among them, ': '',' while': '. ','protons, electrons and neutrons': 'protons electrons and neutrons',
        'However, ': '','However':'','therefore' : '','With the identification that ': ' ','Nevertheless,': '','However ': '',
        'Among ': '','Therefore,': '','Thus,': '','When ': '','This is ': '','that ': '','So, ': '','But':'', 'Hence,':'','it implies ': '',
        'As at present,': '', 'In the ': ' ','The ': '','Such ': '','For instance,': ''
    }

    def multipleReplace(self, text, wordDict):

        """
        Replacing words in the wordDict using a single scan
        through the para
        :param text: input text para
        :param wordDict: the words that must be replaced
        :return: replaced text
        """

        for key in wordDict:
            text = text.replace(key, wordDict[key])
        return text;

    def preProcessPara(self, textPara):

        """
        Removing sentences that have example etc...

        :param textPara: text input
        :return: pre processed para
        """

        # text = self.multipleReplace(textPara, self.wordDic);
        sentence_list = nltk.sent_tokenize(textPara);
        # print(sentence_list);
        removed_sentences_list = [];
        final_sentences_list = [];
        text = '';
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        for sent in sentence_list:

            if sent.find("example") != -1 or sent.find("discussed") != -1 or sent.find("earlier") != -1 or sent.find("We cannot") != -1 or sent.find("too") != -1 or (
                    regex.search(sent) is not None) or sent.find("understand") != -1 or sent.find("Study") != -1 or sent.find("let us see") != -1 or sent.find("Given below") != -1\
                    or sent.find("Studying") != -1 or sent.find("Table") != -1 or sent.find("attempt") != -1 or sent.find('Fig.') != -1 or sent.find('+') != -1 or sent.find(' * ') != -1 or sent.find('indicates') != -1:
                removed_sentences_list.append(str(sent));

            else:
                final_sentences_list.append(str(sent));
                text = text + str(sent).rstrip("\n").rstrip("\n ").rstrip(" \n").rstrip(" \n ") + " ";
        # print(removed_sentences_list)
        # print(text)
        return text;

    def tokenizedSentenceLength(self, sentence):
        """
        Returning the sentence length
        :param sentence: sentence
        :return: length of the sentence
        """
        return len(nltk.word_tokenize(sentence))


