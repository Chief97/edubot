"""
    Forming questions using a sentence
"""
import difflib
import nltk
import spacy
import inflect
import random

from General.Self_Assess_Question_Generation.PreProcess import PreProcess

from nltk.corpus import wordnet
from nltk import sent_tokenize, RegexpParser, pos_tag
from nltk.stem.wordnet import WordNetLemmatizer

inflect = inflect.engine()
nlp = spacy.load("en_core_web_sm")


class QuestionFormation(object):

    def _getSubject(self, sentence):
        """
       Extracting the subject from the sentence
       :param sentence: selected sentence
       :return: the subject of the sentence
       """

        if sent_tokenize(sentence)[0].find("Therefore") != -1 or sent_tokenize(sentence)[0].find("Therefore,") != -1 or sent_tokenize(sentence)[0].find("The") != -1:
            wordDic={'Therefore':'','Therefore,':''}
            p = PreProcess()
            sentence = p.multipleReplace(sentence,wordDic)
            # print("TRUE")
        # print(sentence)
        doc = nlp(sentence);
        root = [token for token in doc if token.head == token][0]
        sub = ""
        if str(list(root.lefts)) == '[]':
            return "SUBJECT CANNOT BE DEFINED";
        else:
            subject = list(root.lefts)[0]
            for descendant in subject.subtree:
                assert subject is descendant or subject.is_ancestor(descendant);
                sub = sub + str(descendant.text) + " ";
            p = PreProcess()
            if p.tokenizedSentenceLength(sub) <= 1:
                stopwords = nltk.corpus.stopwords.words('english');
                verifyVal = sub.lower()
                if verifyVal in stopwords:
                    return "SUBJECT CANNOT BE DEFINED";
                else:
                    return verifyVal;
            else:
                return sub;
        # print("subject :" + sub)


    def _getLabelArray(self, subject):
        """
        generating the entity label for the subject
        :param subject: subject phrase of a sentence
        :return: a string including the entity label
                of the subject
        """
        words = nltk.word_tokenize(subject);
        tagged = nltk.pos_tag(words);
        chunks = nltk.ne_chunk(tagged);
        label = '';
        labels = [];
        for chunk in chunks:
            if type(chunk) is nltk.Tree:
                for c in chunk.leaves():
                    if str(chunk.label).find('PERSON') != -1:
                        label = 'PERSON'

                    elif str(chunk.label).find('ORGANIZATION') != -1:
                        label = 'ORGANIZATION'

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

    def yesNoQuestions(self, sentence):
        hverbs = ["is", "have", "had", "was", "could", "would", "will", "do", "did", "should", "shall", "can", "are"]
        words = sentence.split(" ");
        zen_sim = (0, "", "");
        question = '';
        for hverb in hverbs:
            for word in words:
                similarity = difflib.SequenceMatcher(None, word, hverb).ratio() * 100
                if similarity > zen_sim[0]:
                    zen_sim = (similarity, hverb, word)
        if zen_sim[0] < 30:
            raise ValueError("unable to create question.")
        else:
            words.remove(zen_sim[2])
            words = " ".join(words)[0].lower() + " ".join(words)[1:-1]
            question = "{0} {1}?".format(zen_sim[1].capitalize(), words);
        return question;

    def generateWhyQuestion(self, sentence):
        # print(nltk.word_tokenize(sentence)[0])
        ##newly added
        if nltk.word_tokenize(sentence)[0].find("Because") != -1 or nltk.word_tokenize(sentence)[0].find(
                "Hence") != -1 or nltk.word_tokenize(sentence)[0].find("Therefore") != -1 or \
                nltk.word_tokenize(sentence)[0].find("But") != -1:
            wordDic = {'Because of': '', 'Because': '', 'Therefore,': '', 'Therefore': '', 'Hence,': '', 'But if': '', "But": '', 'Hence': ''}
            preProcess = PreProcess()
            sentence = preProcess.multipleReplace(sentence, wordDic)
            if str(sentence).count(',') > 0:
                doc = nlp(sentence)
                pos=''
                for chunk in doc.noun_chunks:
                    if chunk.root.dep_ == 'nsubjpass' or chunk.root.dep_ == 'nsubj':
                        pos = nltk.pos_tag(nltk.word_tokenize(chunk.text))
                        # print(pos)
                    if str(pos).find('PRP') == -1:
                        break;
                question = '';
                return question
            else:
                return 'Why is ' + sentence + '?'
        elif str(sentence).find('because') != -1 or str(sentence).find('therefore') != -1 or str(sentence).find(
                'although') != -1 or str(sentence).find('since') != -1:
            doc = nlp(sentence)
            headword = []
            for chunk in doc.noun_chunks:
                if chunk.root.dep_ == 'nsubjpass' or chunk.root.dep_ == 'nsubj':
                    pos = nltk.pos_tag(nltk.word_tokenize(chunk.text))
                    # print(pos)
                if str(pos).find('PRP') == -1:
                    headword.append(chunk.text)
            headword = headword[0];
            sentencePart = self._slicer(sentence, 'because');
            # print("hii1 " + sentencePart)
            if len(sent_tokenize(sentencePart)) <= 2:
                return ''
            else:
                if str(sentencePart).count(',') > 0:
                    sentencePart = self.slicer1(sentencePart, ',');
                # print("hii " + sentencePart)
                s = ''
                for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentencePart))):
                    if (pos == 'PRP'):
                        # print(word)
                        word = headword
                        # print(word)
                    # print(word)
                    s = s + word + " "
                    # s = ''.join(word)
                # print(s)
                question = 'Why ' + s + '?';
                return question
        else:
            return ''

    def generateWHQuestion(self, sentence):
        sentence = sentence.lower()
        question = '';
        WHVerbs = ['Who', 'What', 'Where'];
        # p = PreProcess()
        # wordDic = {'But':'','Similarly':'','Thus':'','Therefore,':''}
        wordDic = {'Thus, ': '', 'Hence, ': '', 'Hence ': '','Therefore,': '', 'But,': '','But': '', 'Similarly': '', 'Therefore':''}
        p = PreProcess()
        sentence = p.multipleReplace(sentence, wordDic)
        # if nltk.word_tokenize(sentence)[0].find("But") != -1 or nltk.word_tokenize(sentence)[0].find("Therefore") != -1 or nltk.word_tokenize(sentence)[0].find("Similarly") != -1 or nltk.word_tokenize(sentence)[0].find("Thus") != -1:
        #     sentence = p.multipleReplace(sentence,wordDic)
        print("SENTENCE ___________________________ " + sentence)
        subject = self._getSubject(sentence);
        print("SUBJECT ************ " ,str(subject))
        if subject == 'SUBJECT CANNOT BE DEFINED' or subject == '':
            question = '';
        else:
            label = self._getLabelArray(subject);
            # print("LABLE : " + label)
            if label == '':
                # wordDict = {'%subject%': 'What '}
                # p = PreProcess()
                # question = p.multipleReplace(sentence,wordDict)
                # print("SUBJECT : " + subject.lstrip())
                question = str(sentence).replace(subject.lstrip(), "What ");
                question = question + '?'
                # question = question.replace(".", "?");
                # print(question)
            elif label == 'PERSON':
                question = sentence.replace(subject, "Who ");
                question = question + '?'
            elif label == 'LOCATION':
                question = sentence.replace(subject, "Where ");
                question = question + '?'
            # print("QUESTION : " + question)

        if question is '':
            # question = "CANNOT GENERATE MEANINGFUL WH TYPE QUESTION";
            return '';
        elif nltk.word_tokenize(question)[0] not in WHVerbs:
            # question = "CANNOT GENERATE MEANINGFUL WH TYPE QUESTION";
            return '';
        else:
            return question

    def _getNounPhrases(self, sentence):
        """
        Extracting all the nouns in the sentence
        :param sentence: selected sentence
        :return: list of nouns in the sentence
        """
        stopwords = nltk.corpus.stopwords.words('english');

        pattern = r"""
            NP:{<DT>?<JJ>*<NN>}
               {<NNP>+}
               {<NNS>+}
               {<NN>+}
               {<NNP><NN>}
            """
        noun_list = [];
        for sent in sent_tokenize(sentence):
            subject = self._getSubject(sent);
            sentence = sent.split();
            PChunker = RegexpParser(pattern);
            output = PChunker.parse(pos_tag(sentence));
            for subtree in output.subtrees(filter=lambda t: t.label() == 'NP'):
                for x in subtree:
                    if subject.find(x[0]) == -1 and x[0] not in stopwords:
                        noun_list.append(x[0]);
        # print(noun_list);
        return noun_list;

    def _slicer(self, my_str, sub):
        length = len(sub)
        index = my_str.find(sub)
        index = index + len(sub)
        if index != -1:
            # print("WORD :::::" , my_str[index])
            return my_str[:index - length]
        else:
            raise Exception('Sub string not found!')

    def generateFillInTheBlanksQuestion(self, sentence):

        """
        generating filling the blanks questions
        :param sentence: selected sentence
        :return: filling the blank question
        """

        noun_list = self._getNounPhrases(sentence);
        # stopwords = nltk.corpus.stopwords.words('english');
        #
        # for noun in noun_list:
        #     if noun in stopwords:
        #         noun_list.remove(noun);
        # if noun == 'the' or noun == 'of' or noun == 'an' or noun == 'it' or noun == 'a':
        #     noun_list.remove(noun);

        for key in noun_list:
            # if key == 'the' or key == 'of' or key == 'an' or 'it':
            #     continue
            # print(key)
            sentence = sentence.replace(key, "__________")

        if str(sentence).find("__________") != -1:
            return sentence;
        else:
            sentence = "CANNOT GENERATE MEANINGFUL FILL IN THE BLANKS QUESTION";
            return sentence;

    # def _getLabel(self, word):
    #     """
    #     Extracting the entity type of the subject
    #     :param word:
    #     :return: entity type
    #     """
    #     doc = nlp(word);
    #     label = "";
    #     for ent in doc.ents:
    #         label = ent.label_
    #         if label == '':
    #             label = "";
    #     return label;

    def slicer1(self, my_str, sub):
        length = len(sub)
        index = my_str.find(sub)
        index = index + len(sub)
        if index != -1:
            # print("WORD :::::" , my_str[index])
            return my_str[index:]
        else:
            raise Exception('Sub string not found!')

    def generateHowQuestion(self, sentence):
        # qf = QuestionFormation()
        c = str(sentence).count(',')

        # print(c)
        if c == 1:
            sentence = self.slicer1(sentence, ",")
        # print(sent)
        words = nltk.word_tokenize(sentence);
        tagged = nltk.pos_tag(words);
        subject = self._getSubject(sentence)
        dict = {}
        l1 = ['MD', 'NN', 'VB', 'VBN']
        l2 = ['MD', 'NN', 'NNS', 'VB', 'VBN']
        noun = []
        q = "How "
        for pos in enumerate(tagged):
            if pos[1][1] == 'NN':
                noun.append(pos[1][0])
            dict[pos[1][1]] = pos[1][0]
        # print(str(dict))

        # if all(i in dict for i in l1):
        #     question = 'How' + ' ' + dict['MD'] + ' ' + noun[0] + ' ' + dict['VB'] + ' ' + dict['VBN'] + '?'
        #     return question
        #     # print(question)
        question = ''
        if subject != '':
            if str(sentence).find('Therefore') != -1 or str(sentence).find('it') != -1:
                return question
            elif all(i in dict for i in l1):
                question = 'How' + ' ' + dict['MD'] + ' ' + subject.lower() + ' ' + dict['VB'] + ' ' + dict['VBN'] + '?'
                return question
                # print(question)
        else:
            return question
            # print(word)

    def createYesUsingHVerbPhrase(self, sentence):

        if str(sentence).find("This") != -1 or str(sentence).find("this") != -1 or str(sentence).find(
                "them") != -1 or str(sentence).find("them,") != -1:
            question = ''
            return question
        else:
            ##newly added
            wordDic = {'Thus, ': '', 'Hence, ': '', 'Therefore,': '', 'But': '', 'Similarly': ''}
            p = PreProcess()
            sentence = p.multipleReplace(sentence, wordDic)
            words = nltk.word_tokenize(sentence);
            tagged = nltk.pos_tag(words);
            verb = []
            adjectives = []
            synonym = ''
            hverb = ['is', 'are', 'can', 'was', 'were']
            for x, y in enumerate(tagged):
                if y[1] == 'MD' or y[1] == 'VBZ' or y[1] == 'VBP':
                    verb.append(y[0])

            # noun = self._getNounPhrasesWithSubject(sentence)
            # removable = ['The','the']
            # for i in noun:
            #     if i in removable:
            #         noun.remove(i)

            # print(noun)
            if len(verb) == 0:
                return ''
            else:
                if verb[0] in hverb:
                    # print("VERB " + verb[0])
                    sentence = sentence.replace(verb[0], '')
                    question = verb[0].capitalize() + ' ' + sentence.lower() + "?"
                    return question;
                else:
                    v = ''
                    for h in hverb:
                        if str(sentence).find(h) != -1:
                            v = h
                            break;
                    # print(inflect.singular_noun(v))
                    if v != '':
                        if inflect.singular_noun(nltk.word_tokenize(sentence)[0]) is False and inflect.singular_noun(
                                v) is False:
                            return v.capitalize() + ' ' + sentence.lower() + "?"
                        elif inflect.singular_noun(nltk.word_tokenize(sentence)[0]) is True and inflect.singular_noun(
                                v) is True:
                            return v.capitalize() + ' ' + sentence.lower() + "?"
                        else:
                            if self._determineTenseInput(sentence) == "past":
                                words = nltk.word_tokenize(sentence);
                                tagged = nltk.pos_tag(words);
                                vb = []
                                for i in tagged:
                                    if i[1] == 'VBD':
                                        vb.append(i[0])
                                        break;
                                if len(vb) != 0:
                                    sentence = sentence.replace(vb[0], WordNetLemmatizer().lemmatize(vb[0], 'v'))
                                    question = 'Did' + ' ' + sentence.lower() + "?"
                                    return question;
                                else:
                                    return ''
                            else:
                                words = nltk.word_tokenize(sentence);
                                if inflect.singular_noun(words[0]) is False:
                                    # print(noun[0])
                                    question = 'Does' + ' ' + sentence.lower() + "?"
                                    return question;
                                else:
                                    question = 'Do' + ' ' + sentence.lower() + "?"
                                    return question;
                    else:
                        if self._determineTenseInput(sentence) == "past":
                            words = nltk.word_tokenize(sentence);
                            tagged = nltk.pos_tag(words);
                            vb = []
                            for i in tagged:
                                if i[1] == 'VBD':
                                    vb.append(i[0])
                                    break;
                            if len(vb) != 0:
                                sentence = sentence.replace(vb[0], WordNetLemmatizer().lemmatize(vb[0], 'v'))
                                question = 'Did' + ' ' + sentence.lower() + "?"
                                return question;
                            else:
                                return ''
                        else:
                            words = nltk.word_tokenize(sentence);
                            if inflect.singular_noun(words[0]) is False:
                                # print(noun[0])
                                question = 'Does' + ' ' + sentence.lower() + "?"
                                return question;
                            else:
                                question = 'Do' + ' ' + sentence.lower() + "?"
                                return question;

    def createNoUsingHVerbPhrase(self, sentence):
        if str(sentence).find("This") != -1 or str(sentence).find("this") != -1 or str(sentence).find(
                "them") != -1 or str(sentence).find("them,") != -1:
            question = ''
            return question
        else:
            ##newly added
            wordDic = {'Thus, ': '', 'Hence, ': '', 'Therefore,': '', 'But': '', 'Similarly': ''}
            p = PreProcess()
            sentence = p.multipleReplace(sentence, wordDic)
            words = nltk.word_tokenize(sentence);
            tagged = nltk.pos_tag(words);
            verb = []
            adjectives = []
            synonym = ''
            hverb = ['is', 'are', 'can', 'was', 'were']
            for x, y in enumerate(tagged):
                if y[1] == 'MD' or y[1] == 'VBZ' or y[1] == 'VBP':
                    verb.append(y[0])
                if y[1] == 'JJ' or y[1] == 'JJS' or y[1] == 'JJR':
                    adjectives.append(y[0])
            # print("ADJECTIVE : " ,adjectives)
            # noun = self._getNounPhrasesWithSubject(sentence)
            # print(noun)
            if len(adjectives) != 0:
                adjective = random.choice(adjectives)
                # print("ADJECTIVE " + adjective);
                # print("SYNONYM " + str(self._getSynonym(adjective)))
                antonym = str(self._getAntonym(adjective, sentence));
                # print("ADJECTIVE " + adjective)
                # print("ANTONONYM " + antonym)
                if antonym != '':
                    if str(sentence).find(antonym) == -1:
                        sentence = sentence.replace(str(adjective), antonym)

                if len(verb) == 0:
                    return ''
                else:
                    if verb[0] in hverb:
                        # print("VERB " + verb[0])
                        sentence = sentence.replace(verb[0], '')
                        question = verb[0].capitalize() + ' ' + sentence.lower() + "?"
                        return question;
                    else:
                        v = ''
                        for h in hverb:
                            if str(sentence).find(h) != -1:
                                v = h
                                break;
                        # print(v)
                        if v != '':
                            if inflect.singular_noun(
                                    nltk.word_tokenize(sentence)[0]) is False and inflect.singular_noun(
                                v) is False:
                                return v.capitalize() + ' ' + sentence.lower() + "?"
                            elif inflect.singular_noun(
                                    nltk.word_tokenize(sentence)[0]) is True and inflect.singular_noun(
                                v) is True:
                                return v.capitalize() + ' ' + sentence.lower() + "?"
                            else:
                                if self._determineTenseInput(sentence) == "past":
                                    words = nltk.word_tokenize(sentence);
                                    tagged = nltk.pos_tag(words);
                                    vb = []
                                    for i in tagged:
                                        if i[1] == 'VBD':
                                            vb.append(i[0])
                                            break;
                                    if len(vb) != 0:
                                        sentence = sentence.replace(vb[0], WordNetLemmatizer().lemmatize(vb[0], 'v'))
                                        question = 'Did' + ' ' + sentence.lower() + "?"
                                        return question;
                                    else:
                                        return ''
                                else:
                                    words = nltk.word_tokenize(sentence);
                                    if inflect.singular_noun(words[0]) is False:
                                        question = 'Does' + ' ' + sentence.lower() + "?"
                                        return question;
                                    else:
                                        question = 'Do' + ' ' + sentence.lower() + "?"
                                        return question;
                        else:
                            if self._determineTenseInput(sentence) == "past":
                                words = nltk.word_tokenize(sentence);
                                tagged = nltk.pos_tag(words);
                                vb = []
                                for i in tagged:
                                    if i[1] == 'VBD':
                                        vb.append(i[0])
                                        break;
                                if len(vb) != 0:
                                    sentence = sentence.replace(vb[0], WordNetLemmatizer().lemmatize(vb[0], 'v'))
                                    question = 'Did' + ' ' + sentence.lower() + "?"
                                    return question;
                                else:
                                    return ''
                            else:
                                words = nltk.word_tokenize(sentence);
                                if inflect.singular_noun(words[0]) is False:
                                    question = 'Does' + ' ' + sentence.lower() + "?"
                                    return question;
                                else:
                                    question = 'Do' + ' ' + sentence.lower() + "?"
                                    return question;
            else:
                return ''

    def _getNounPhrasesWithSubject(self, sentence):
        """
              Extracting all the nouns in the sentence
              :param sentence: selected sentence
              :return: list of nouns in the sentence
              """

        pattern = r"""
                  NP:{<DT>?<JJ>*<NN>}
                     {<NNP>+}
                     {<NN>+}
                     {<NNP><NN>}
                  """
        noun_list = [];
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

    def _determineTenseInput(self, sentence):
        text = nltk.word_tokenize(sentence)
        tagged = pos_tag(text)

        fc = len([word for word in tagged if word[1] == "MD"])
        prec = len([word for word in tagged if word[1] in ["VBP", "VBZ", "VBG"]])
        pc = len([word for word in tagged if word[1] in ["VBD", "VBN"]])
        if fc > prec and fc > pc:
            return "future";
        elif prec > fc and prec > pc:
            return "present"
        else:
            return "past"

    def _getSynonym(self, word):
        # Creating a list
        synonyms = []
        for syn in wordnet.synsets(word):
            for lm in syn.lemmas():
                synonyms.append(lm.name())  # adding into synonyms
        # print(set(synonyms))
        if len(random.choice(list(set(synonyms)))) != 0:
            return random.choice(list(set(synonyms)))
        else:
            return ''

    def _getAntonym(self, word, sentence):
        antonyms = []
        for syn in wordnet.synsets(word):
            for lm in syn.lemmas():
                if lm.antonyms():
                    antonyms.append(lm.antonyms()[0].name())  # adding into antonyms
        # print(set(antonyms))

        if len(list(set(antonyms))) != 0:
            return random.choice(list(set(antonyms)))
        else:
            return ''

    def _getLabelsForFillInBlanks(self, sentence):
        doc = nlp(sentence)
        # doc=nlp("Ada lovlace was born in london")
        # document level
        entityArray = []
        for e in doc.ents:
            entityArray.append(e.text)
        return entityArray

    def fillInBlanks(self, sentence):
        entityArray = self._getLabelsForFillInBlanks(sentence)
        nouns = []
        # print(entityArray)
        if len(entityArray) != 0:
            for i in entityArray:
                nouns.append(i)
            noun = random.choice(nouns)
            sentence = sentence.replace(noun, ' @dash ')
            return sentence
        else:
            nouns = self._getNounPhrases(sentence)
            if len(nouns) != 0:
                noun = random.choice(nouns)
                sentence = sentence.replace(noun, ' @dash ')
                return sentence
            else:
                return ''

    def _getVerb(self, sentence):
        words = nltk.word_tokenize(sentence)
        verb = []
        for i in words:
            if i[1] == 'VB' or i[1] == 'VBG' or i[1] == 'VBD' or i[1] == 'VBN' or i[1] == 'VBP' or i[1] == 'VBZ':
                verb.append(i[0])
        return verb
