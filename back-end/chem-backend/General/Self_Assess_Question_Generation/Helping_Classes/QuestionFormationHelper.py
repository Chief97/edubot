"""
    Helper methods used to generate questions (WH,Fill-in-the-blanks,Binary questions),
"""

import nltk
import spacy
import inflect
import random

from nltk.corpus import wordnet
from nltk import sent_tokenize, RegexpParser, pos_tag

inflect = inflect.engine()
nlp = spacy.load("en_core_web_sm")


class QuestionFormationHelper(object):

    def getSubject(self, sentence):
        """
       Extracting the subject from the sentence
       :param sentence: selected sentence
       :return: the subject of the sentence
       """
        doc = nlp(sentence.lstrip());  # document representation of the sentence
        root = [token for token in doc if token.head == token][0]
        sub = ""  # subject
        if str(list(root.lefts)) == '[]':
            sub = "SUBJECT CANNOT BE DEFINED";
        else:
            subject = list(root.lefts)[0]
            for descendant in subject.subtree:
                assert subject is descendant or subject.is_ancestor(descendant);
                sub = sub + str(descendant.text) + " ";
        # print("subject :" + sub)
        return sub;

    def _getNounPhrasesWithSubject(self, sentence):
        """
              Extracting all the nouns in the sentence(including the subject)
              :param sentence: selected sentence
              :return: list of nouns in the sentence
              """
        # pattern for noun phrases
        pattern = r"""
                     NP:{<DT>?<JJ>*<NN>}
                        {<NNP>+}
                        {<NN>+}
                        {<NNP><NN>}
                     """
        noun_list = [];  # nouns list
        for sent in sent_tokenize(sentence):
            # subject = self._getSubject(sent);
            sentence = sent.split();
            PChunker = RegexpParser(pattern);
            output = PChunker.parse(pos_tag(sentence));
            for subtree in output.subtrees(filter=lambda t: t.label() == 'NP'):
                for x in subtree:
                    # if subject.find(x[0]) == -1:
                    noun_list.append(x[0]);
        # print(noun_list);
        return noun_list;

    def getNounPhrases(self, sentence):
        """
        Extracting all the nouns in the sentence(the subject is excluded)
        :param sentence: selected sentence
        :return: list of nouns in the sentence
        """
        stopwords = nltk.corpus.stopwords.words('english');  # retrieving the stopwords
        ## defining the pattern for noun
        pattern = r"""
               NP:{<DT>?<JJ>*<NN>}
                  {<NNP>+}
                  {<NNS>+}
                  {<NN>+}
                  {<NNP><NN>}
               """
        noun_list = [];  # nouns list
        for sent in sent_tokenize(sentence):
            subject = self.getSubject(sent);  # subject of the sentence
            sentence = sent.split();
            PChunker = RegexpParser(pattern);
            output = PChunker.parse(pos_tag(sentence));
            for subtree in output.subtrees(filter=lambda t: t.label() == 'NP'):
                for x in subtree:
                    if subject.find(x[0]) == -1 and x[0] not in stopwords:
                        noun_list.append(x[0]);
        # print(noun_list);
        return noun_list;

    def getLabelArray(self, subject):
        """
        generating the entity label for the subject
        :param subject: subject phrase of a sentence
        :return: a string including the entity label
                of the subject
        """
        words = nltk.word_tokenize(subject);  # word tokenized sentence
        tagged = nltk.pos_tag(words);  # tag array of word array
        chunks = nltk.ne_chunk(tagged);  # chunks of the tagged words
        label = '';  # named entity label
        labels = [];  # named entity label list
        for chunk in chunks:
            if type(chunk) is nltk.Tree:
                for c in chunk.leaves():
                    # checking for person label
                    if str(chunk.label).find('PERSON') != -1:
                        label = 'PERSON'
                    # checking for organization label
                    elif str(chunk.label).find('ORGANIZATION') != -1:
                        label = 'ORGANIZATION'
                    # checking for location label
                    elif str(chunk.label).find('LOCATION') != -1:
                        label = 'LOCATION'
            labels.append(label);

        label = str(labels);
        if label.find("PERSON") != -1 and label.find("ORGANIZATION") != -1:
            label = "PERSON"
        elif label.find("PERSON") != -1 and label.find("ORGANIZATION") == -1:
            label = "ORGANIZATION"
        elif label.find("PERSON") == -1 and label.find("LOCATION") != -1:
            label = 'LOCATION'
        elif label.find("PERSON") == -1 and label.find("ORGANIZATION") == -1:
            label = ''

        return str(label);

    def slicer(self, my_str, sub):
        """
        Slicing a sentence using the subject
        input sentence = I went to kandy, slicing word = to
        output sentence = I went
        :param my_str: sentence
        :param sub: subject
        :return: sub string(excluding the subject)
        """
        length = len(sub)
        index = my_str.find(sub)
        index = index + len(sub)
        if index != -1:
            # print("WORD :::::" , my_str[index])
            return my_str[:index - length]
        else:
            raise Exception('Sub string not found!')

    def getLabel(self, word):
        """
        Extracting the entity type of the subject
        :param word: input word
        :return: named entity for the input word
        """
        doc = nlp(word);  # document representation of the sentence
        label = "";  # named entity label
        for ent in doc.ents:
            label = ent.label_
            if label == '':
                label = "";
        return label;

    def checkPersonEntity(self, sentence):
        """
        Identifying the person entity counts
        :param sentence: input sentence
        :return: number of person entities in the sentence
        """
        doc = nlp(sentence)  # document representation of the sentence
        personCount = 0  # initial person count in a given sentence
        for e in doc.ents:
            # identifying the entity is person
            if e.label_ == "PERSON":
                # print(e.text)
                personCount = personCount + 1
        return personCount
        # words = nltk.word_tokenize(sentence);
        # tagged = nltk.pos_tag(words);
        # chunks = nltk.ne_chunk(tagged);
        # personCount = 0;
        # for chunk in chunks:
        #     if type(chunk) is nltk.Tree:
        #         for c in chunk.leaves():
        #             if str(chunk.label).find('PERSON') != -1:
        #                 personCount = personCount + 1;
        #
        # return personCount;

    def removingFirstDt(self, sentence):
        """
        Removing the first determiner if its present in a sentence
        :param sentence: input sentence
        :return: sentence after the first determiner is removed
        """
        words = nltk.word_tokenize(sentence);  # word tokenized sentence
        tagged = nltk.pos_tag(words);  # tagged sentence
        # print(tagged)
        if tagged[0][1] == "DT":
            # print(tagged[0])
            word = tagged[0][0]
            # print("Replaced word : " +word)
            sentence = sentence.replace(word, " ", 1)
            # print("REPLACED SENTENCE : " +sentence)
        return sentence;

    def getMainVerb(self, sentence):

        doc = nlp(sentence)  # document representation of the sentence
        verb = ''  # main verb
        for i in doc:
            if i.pos_ == 'VERB':
                verb = i

        return verb

    def _getVerb(self, sentence):
        """
        identifying the verbs for a given sentence
        :param sentence: input sentence
        :return: verbs list in the sentence
        """
        words = nltk.word_tokenize(sentence)  # word tokenized sentence
        verb = []  # verbs list
        for i in words:
            # all possible states of a verb
            if i[1] == 'VB' or i[1] == 'VBG' or i[1] == 'VBD' or i[1] == 'VBN' or i[1] == 'VBP' or i[1] == 'VBZ':
                verb.append(i[0])
        return verb

    def getAntonym(self, word, sentence):
        """
        Identifying the antonym for a given sentence
        :param word: input word
        :param sentence:
        :return: identifying the antonym for the input word
        """
        antonyms = []
        for syn in wordnet.synsets(word):
            for lm in syn.lemmas():
                if lm.antonyms():
                    antonyms.append(lm.antonyms()[0].name())  # adding into antonyms
        # print(set(antonyms))

        if len(list(set(antonyms))) != 0:
            if word == "physical":
                return "non-physical"
            elif word == "single":
                return "double"
            elif word == "light":
                return "heavy"
            elif word == "native":
                return "non-native"
            elif word == "poor":
                return "rich"
            else:
                return random.choice(list(set(antonyms)))
        else:
            return ''

    def getSynonym(self, word):
        """
        Identifying the synonym for a given word
        :param word: input word
        :return: synonym to the input word
        """
        # Creating a list
        synonyms = []  # synonyms array
        for syn in wordnet.synsets(word):
            for lm in syn.lemmas():
                synonyms.append(lm.name())  # adding into synonyms
        # print(set(synonyms))
        if len(random.choice(list(set(synonyms)))) != 0:
            return random.choice(list(set(synonyms)))
        else:
            return ''

    def determineTenseInput(self, sentence):
        """
        Identifying the tense of a sentence
        sentence = I went to kandy - past tense
                   I will goto kandy - future tense
                   I goto kandy - present tense
        :param sentence: input sentence
        :return: the tense of the sentence
        """
        text = nltk.word_tokenize(sentence)  # word tokenized sentence
        tagged = pos_tag(text)  # tagged sentence

        fc = len([word for word in tagged if word[1] == "MD"])  # rule for future tense
        prec = len([word for word in tagged if word[1] in ["VBP", "VBZ", "VBG"]])  # rule for present tense
        pc = len([word for word in tagged if word[1] in ["VBD", "VBN"]])  # rule for past tense
        if fc > prec and fc > pc:
            return "future";
        elif prec > fc and prec > pc:
            return "present"
        else:
            return "past"

    def getLabelsForFillInBlanks(self, sentence):
        """
        Identifying the named entities in a sentence
        :param sentence: input sentence
        :return: the words array that is a named entity
        """
        doc = nlp(sentence)
        # doc=nlp("Harry Potter was born in london")
        # document level
        entityArray = []  # named entity array
        for e in doc.ents:
            entityArray.append(e.text)
        return entityArray

    def slicer1(self, my_str, sub):
        """
        Slicing the sentence using a word
        input sentence = I went to kandy, slicing word = to
        output sentence = kandy
        :param my_str:
        :param sub:
        :return:
        """
        length = len(sub)
        index = my_str.find(sub)
        index = index + len(sub)
        if index != -1:
            # print("WORD :::::" , my_str[index])
            return my_str[index:]
        else:
            raise Exception('Sub string not found!')
