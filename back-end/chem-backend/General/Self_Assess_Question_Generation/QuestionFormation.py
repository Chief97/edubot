"""
    Forming questions using a sentence
"""
import difflib
import nltk
import spacy
import inflect
import random

from General.Self_Assess_Question_Generation.Helping_Classes.QuestionFormationHelper import QuestionFormationHelper
from General.Self_Assess_Question_Generation.PreProcess import PreProcess

from nltk import sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

inflect = inflect.engine()
nlp = spacy.load("en_core_web_sm")


class QuestionFormation(object):

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
        """
        generation of why type of questions. initially will be checking for conjunctions in the sentence.
        If a conjunction is present genrating ehy type question
        :param sentence: input sentence
        :return: question
        """

        # identification for conjunctions at the beginning of the sentence
        if nltk.word_tokenize(sentence)[0].find("Because") != -1 or nltk.word_tokenize(sentence)[0].find(
                "Hence") != -1 or nltk.word_tokenize(sentence)[0].find("Therefore") != -1 or \
                nltk.word_tokenize(sentence)[0].find("But") != -1:
            wordDic = {'Because of': '', 'Because': '', 'Therefore,': '', 'Therefore': '', 'Hence,': '', 'But if': '',
                       "But": '', 'Hence': ''}
            preProcess = PreProcess()
            sentence = preProcess.multipleReplace(sentence,
                                                  wordDic)  # replacing the conjunction according to the worddic
            if str(sentence).count(',') > 0:
                doc = nlp(sentence)  # document representation of the sentence
                pos = ''  # post tag
                for chunk in doc.noun_chunks:
                    if chunk.root.dep_ == 'nsubjpass' or chunk.root.dep_ == 'nsubj':
                        pos = nltk.pos_tag(nltk.word_tokenize(chunk.text))

                    if str(pos).find('PRP') == -1:
                        break;
                question = '';
                return question
            else:
                ## cheching for hverb
                hverb = ['is', 'are', 'can', 'was', 'were']
                words = nltk.word_tokenize(sentence);  # word tokenizing
                tagged = nltk.pos_tag(words);  # words tagging
                verb = []
                for x, y in enumerate(tagged):
                    if y[1] == 'MD' or y[1] == 'VBZ' or y[1] == 'VBP':  # identifying helping verbs using rule base approach
                        verb.append(y[0])
                if verb[0] in hverb:  # identifying whether the verb list contains a hverb defined above

                    sentence = sentence.replace(verb[0], '')
                #     return "Why " + sentence + " ?"
                # else:
                    return 'Why is ' + sentence + ' ?'  # question

        # identifying a conjunction is present in the middle of sentence
        elif str(sentence).find('because') != -1 or str(sentence).find('therefore') != -1 or str(sentence).find(
                'although') != -1 or str(sentence).find('since') != -1:

            doc = nlp(sentence)  # document representation of the sentence
            headword = []  # the head word of the pronoun
            pos = ''  # pos tag
            for chunk in doc.noun_chunks:
                if chunk.root.dep_ == 'nsubjpass' or chunk.root.dep_ == 'nsubj':
                    pos = nltk.pos_tag(nltk.word_tokenize(chunk.text))

                if str(pos).find('PRP') == -1:
                    headword.append(chunk.text)
            headword = headword[0];  # replacing the pronoun with the headword
            helper = QuestionFormationHelper()
            sentencePart = helper.helperForWhyQuestions(sentence);

            if len(sent_tokenize(sentencePart)) <= 2:
                return 'Why ' + sentencePart + " ?"
            else:
                if str(sentencePart).count(',') > 0:
                    sentencePart = helper.slicer1(sentencePart, ',');

                s = ''
                for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentencePart))):
                    if (pos == 'PRP'):
                        word = headword

                    s = s + word + " "
                    # s = ''.join(word)

                question = 'Why ' + s + ' ?';
                return question
        else:
            return ''

    def generateWHQuestion(self, sentence):
        """
        Generating wh type questions( mainly who, what)
        :param sentence: inpurt sentence
        :return: wh question
        """
        # sentence = sentence.lower()
        question = '';  # question
        WHVerbs = ['Who', 'What', 'Where'];  # wh verb list
        # p = PreProcess()
        # wordDic = {'But':'','Similarly':'','Thus':'','Therefore,':''}
        wordDic = {'Thus, ': '', 'Hence, ': '', 'Hence ': '', 'Therefore,': '', 'But,': '', 'But': '', 'Similarly': '',
                   'Therefore': ''}  # word dictionary of conjunctions
        p = PreProcess()
        sentence = p.multipleReplace(sentence,
                                     wordDic)  # replacing conjunctions in word dictionary if found in sentence
        helper = QuestionFormationHelper()
        # if nltk.word_tokenize(sentence)[0].find("But") != -1 or nltk.word_tokenize(sentence)[0].find("Therefore") != -1 or nltk.word_tokenize(sentence)[0].find("Similarly") != -1 or nltk.word_tokenize(sentence)[0].find("Thus") != -1:
        #     sentence = p.multipleReplace(sentence,wordDic)
        sentence = helper.removingFirstDt(sentence)  # removing the first determiner
        subject = helper.getSubject(sentence);  # identifying the subject of the sentence

        if subject == 'SUBJECT CANNOT BE DEFINED' or subject == 'none':
            question = '';
        else:
            label = helper.getLabelArray(subject);  # identifying the named entity label for the subject

            if label == '':
                # wordDict = {'%subject%': 'What '}
                # p = PreProcess()
                # question = p.multipleReplace(sentence,wordDict)
                # print("SUBJECT : " + subject.lstrip())
                # when there is no particular label the question will be what type
                # print("SUBJECT::::::::::: " + subject.lstrip())
                question = str(sentence).replace(subject.lstrip(), "What ", 1);
                question = question + ' ?'
                # print(question)
                # question = question.replace(".", "?");
                # print(question)
            # when the named entity label is person the question will be who type
            elif label == 'PERSON':
                question = sentence.replace(subject, "Who ", 1);
                question = question + ' ?'
            # when the named entity label is location the question will be where type
            elif label == 'LOCATION':
                question = sentence.replace(subject, "Where ", 1);
                question = question + ' ?'


        if question is '':
            # question = "CANNOT GENERATE MEANINGFUL WH TYPE QUESTION";
            return '';
        elif nltk.word_tokenize(question)[0] not in WHVerbs:
            # question = "CANNOT GENERATE MEANINGFUL WH TYPE QUESTION";
            return '';
        else:
            return question

    def generateFillInTheBlanksQuestion(self, sentence):

        """
        generating filling the blanks questions
        :param sentence: selected sentence
        :return: filling the blank question
        """

        helper = QuestionFormationHelper();
        noun_list = helper.getNounPhrases(sentence);  # identifying the noun list for the sentence
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
            sentence = sentence.replace(key, "__________")  # replacing the noun with a dash

        if str(sentence).find("__________") != -1:
            return sentence;
        else:
            sentence = "CANNOT GENERATE MEANINGFUL FILL IN THE BLANKS QUESTION";
            return sentence;

    def generateHowQuestion(self, sentence):
        """
        generation of how type questions
        :param sentence: input sentence
        :return: question
        """
        # qf = QuestionFormation()
        c = str(sentence).count(',')  # count of commas present in the sentence
        helper = QuestionFormationHelper()
        # print(c)
        if c == 1:
            sentence = helper.slicer1(sentence, ",")  # slicing the sentence
        # print(sent)
        words = nltk.word_tokenize(sentence);  # identifying the words in the sentence
        tagged = nltk.pos_tag(words);  # tagging the words
        subject = helper.getSubject(sentence)  # identification of  the subject for the sentence
        dict = {}  # dictionary
        l1 = ['MD', 'NN', 'VB', 'VBN']  # rule defined to identify how question type
        l2 = ['MD', 'NN', 'NNS', 'VB', 'VBN']
        noun = []
        q = "How "
        for pos in enumerate(tagged):
            if pos[1][1] == 'NN':
                noun.append(pos[1][0])
            dict[pos[1][1]] = pos[1][0]


        # if all(i in dict for i in l1):
        #     question = 'How' + ' ' + dict['MD'] + ' ' + noun[0] + ' ' + dict['VB'] + ' ' + dict['VBN'] + '?'
        #     return question

        question = ''  # question
        if subject != '':  # verifying the subject is not null
            if str(sentence).find('Therefore') != -1 or str(sentence).find('it') != -1:
                return question
            elif all(i in dict for i in l1):
                question = 'How' + ' ' + dict['MD'] + ' ' + subject.lower() + ' ' + dict['VB'] + ' ' + dict[
                    'VBN'] + ' ?'
                return question

        else:
            return question


    def createYesUsingHVerbPhrase(self, sentence):
        """
        generating yes type questions
        :param sentence: input sentence
        :return: yes type question
        """
        helper = QuestionFormationHelper()
        if str(sentence).find("This") != -1 or str(sentence).find("this") != -1 or str(sentence).find(
                "them") != -1 or str(sentence).find("them,") != -1:
            question = ''
            return question
        else:
            # word dictionary
            wordDic = {'Thus, ': '', 'Hence, ': '', 'Therefore,': '', 'But': '', 'Similarly': '', 'Therefore':''}
            p = PreProcess()
            sentence = p.multipleReplace(sentence, wordDic)
            words = nltk.word_tokenize(sentence);  # word tokenizing
            tagged = nltk.pos_tag(words);  # words tagging
            verb = []  # verb list
            adjectives = []
            synonym = ''
            hverb = ['is', 'are', 'can', 'was', 'were']  # helping verb list
            for x, y in enumerate(tagged):
                if y[1] == 'MD' or y[1] == 'VBZ' or y[1] == 'VBP':  # identifying helping verbs using rule base approach
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
                if verb[0] in hverb:  # identifying whether the verb list contains a hverb defined above
                    sentence = sentence.replace(verb[0], '')
                    question = verb[0].capitalize() + ' ' + sentence.lower() + " ?"
                    return question;
                else:
                    v = ''
                    for h in hverb:  # finding whether the sentence contains a hverb defined above
                        if str(sentence).find(h) != -1:
                            v = h
                            break;
                    # print(inflect.singular_noun(v))
                    if v != '':
                        # when the hverb is plural and not in past tense
                        if inflect.singular_noun(nltk.word_tokenize(sentence)[0]) is False and inflect.singular_noun(
                                v) is False:
                            return v.capitalize() + ' ' + sentence.lower() + " ?"
                        # when the hverb is singular and not in past tense
                        elif inflect.singular_noun(nltk.word_tokenize(sentence)[0]) is True and inflect.singular_noun(
                                v) is True:
                            return v.capitalize() + ' ' + sentence.lower() + " ?"
                        else:
                            if helper.determineTenseInput(sentence) == "past":
                                words = nltk.word_tokenize(sentence);
                                tagged = nltk.pos_tag(words);
                                vb = []
                                # identification of the main verb that is past in tense
                                for i in tagged:
                                    if i[1] == 'VBD':
                                        vb.append(i[0])
                                        break;
                                if len(vb) != 0:
                                    # getting the lemma of the main verb
                                    sentence = sentence.replace(vb[0], WordNetLemmatizer().lemmatize(vb[0], 'v'))
                                    question = 'Did' + ' ' + sentence.lower() + " ?"
                                    return question;
                                else:
                                    return ''
                            else:
                                words = nltk.word_tokenize(sentence);
                                if inflect.singular_noun(words[0]) is False:
                                    # print(noun[0])
                                    question = 'Does' + ' ' + sentence.lower() + " ?"
                                    return question;
                                else:
                                    question = 'Do' + ' ' + sentence.lower() + " ?"
                                    return question;
                    else:
                        # when the hverb is in past tense
                        if helper.determineTenseInput(sentence) == "past":
                            words = nltk.word_tokenize(sentence);
                            tagged = nltk.pos_tag(words);
                            vb = []
                            for i in tagged:
                                # identification of the main verb that is past in tense
                                if i[1] == 'VBD':
                                    vb.append(i[0])
                                    break;
                            if len(vb) != 0:
                                # getting the lemma of the main verb. and replacing the verb in past tense with the lemma
                                sentence = sentence.replace(vb[0], WordNetLemmatizer().lemmatize(vb[0], 'v'))
                                question = 'Did' + ' ' + sentence.lower() + " ?"
                                return question;
                            else:
                                return ''
                        else:
                            words = nltk.word_tokenize(sentence);
                            # when the main noun is singular
                            if inflect.singular_noun(words[0]) is False:
                                # print(noun[0])
                                question = 'Does' + ' ' + sentence.lower() + " ?"
                                return question;
                            else:
                                # when the main noun is plural
                                question = 'Do' + ' ' + sentence.lower() + " ?"
                                return question;

    def createNoUsingHVerbPhrase(self, sentence):
        """
        generating no questions
        :param sentence: input sentence
        :return: no type question
        """
        helper = QuestionFormationHelper()
        if str(sentence).find("This") != -1 or str(sentence).find("this") != -1 or str(sentence).find(
                "them") != -1 or str(sentence).find("them,") != -1:
            question = ''
            return question
        else:
            ##newly added
            wordDic = {'Thus, ': '', 'Hence, ': '', 'Therefore,': '', 'But': '', 'Similarly': '','Therefore':''}
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

            # noun = self._getNounPhrasesWithSubject(sentence)
            # print(noun)
            if len(adjectives) != 0:
                adjective = random.choice(adjectives)
                antonym = str(helper.getAntonym(adjective, sentence));
                if antonym != '':
                    if str(sentence).find(antonym) == -1:
                        sentence = sentence.replace(str(adjective), antonym, 1)

                if len(verb) == 0:
                    return ''
                else:
                    if verb[0] in hverb:
                        # print("VERB " + verb[0])
                        sentence = sentence.replace(verb[0], '')
                        question = verb[0].capitalize() + ' ' + sentence.lower() + " ?"
                        return question;
                    else:
                        v = ''
                        for h in hverb:
                            if str(sentence).find(h) != -1:
                                v = h
                                break;
                        # print(v)
                        if v != '':
                            # when the hverb is plural and not in past tense
                            if inflect.singular_noun(
                                    nltk.word_tokenize(sentence)[0]) is False and inflect.singular_noun(
                                v) is False:
                                return v.capitalize() + ' ' + sentence.lower() + " ?"
                            # when the hverb is singular and not in past tense
                            elif inflect.singular_noun(
                                    nltk.word_tokenize(sentence)[0]) is True and inflect.singular_noun(
                                v) is True:
                                return v.capitalize() + ' ' + sentence.lower() + " ?"
                            else:
                                # when the sentence is past in tense
                                if helper.determineTenseInput(sentence) == "past":
                                    words = nltk.word_tokenize(sentence);
                                    tagged = nltk.pos_tag(words);
                                    vb = []
                                    # identifying the main verb in past in tense
                                    for i in tagged:
                                        if i[1] == 'VBD':
                                            vb.append(i[0])
                                            break;
                                    if len(vb) != 0:
                                        # identifying the lemma of the past tensed verb and replacing the original
                                        sentence = sentence.replace(vb[0], WordNetLemmatizer().lemmatize(vb[0], 'v'))
                                        question = 'Did' + ' ' + sentence.lower() + " ?"
                                        return question;
                                    else:
                                        return ''
                                else:
                                    words = nltk.word_tokenize(sentence);
                                    if inflect.singular_noun(words[0]) is False:
                                        # main noun is singular
                                        question = 'Does' + ' ' + sentence.lower() + " ?"
                                        return question;
                                    else:
                                        # main noun is plural
                                        question = 'Do' + ' ' + sentence.lower() + " ?"
                                        return question;
                        else:
                            # when the sentence is past in tense
                            if helper.determineTenseInput(sentence) == "past":
                                words = nltk.word_tokenize(sentence);
                                tagged = nltk.pos_tag(words);
                                vb = []
                                # identifying the main verb in past in tense
                                for i in tagged:
                                    if i[1] == 'VBD':
                                        vb.append(i[0])
                                        break;
                                if len(vb) != 0:
                                    # identifying the lemma of the past tensed verb and replacing the original
                                    sentence = sentence.replace(vb[0], WordNetLemmatizer().lemmatize(vb[0], 'v'))
                                    question = 'Did' + ' ' + sentence.lower() + " ?"
                                    return question;
                                else:
                                    return ''
                            else:
                                words = nltk.word_tokenize(sentence);
                                # main noun is singular
                                if inflect.singular_noun(words[0]) is False:
                                    question = 'Does' + ' ' + sentence.lower() + " ?"
                                    return question;
                                # main noun is plural
                                else:
                                    question = 'Do' + ' ' + sentence.lower() + " ?"
                                    return question;
            else:
                return ''

    def fillInBlanks(self, sentence):

        """
        generating filling the blanks questions
        :param sentence: input sentence
        :return: filling the blank question
        """
        helper = QuestionFormationHelper()
        entityArray = helper.getLabelsForFillInBlanks(sentence)  # identifying words that is a special names entity
        nouns = []  # nouns list

        wordDic = {'Thus, ': '', 'Hence, ': '', 'Hence ': '', 'Therefore,': '', 'But,': '', 'But': '', 'Similarly': '',
                   'Therefore': ''}  # word dictionary
        p = PreProcess()
        sentence = p.multipleReplace(sentence, wordDic)  # replacing the conjunctions according to word dic
        sentence = sentence.lstrip()  # removing left space/s if contains in the sentence
        if len(entityArray) != 0:
            for i in entityArray:
                nouns.append(i)
            noun = random.choice(nouns)
            sentence = sentence.replace(noun, ' @dash ',
                                        1)  # replacing a random word that is a special named entity using @dash sign
            return sentence
        else:
            nouns = helper.getNounPhrases(sentence)
            if len(nouns) != 0:
                noun = random.choice(nouns)
                sentence = sentence.replace(noun, ' @dash ', 1)  # replacing a random noun using @dash sign
                return sentence
            else:
                return ''

    def generateWhoTypeQuestion(self, sentence):
        """
        Generating who type questions
        :param sentence: input sentence
        :return:  question
        """

        helper = QuestionFormationHelper()
        personCount = helper.checkPersonEntity(sentence)  # identifying  the person count
        question = ''  # question
        # verifying the person count is not 0
        if personCount != 0:
            verb = str(helper.getMainVerb(sentence))  # identifying the main verb
            subject = helper.getSubject(sentence)  # identifying the subject
            label = helper.getLabel(subject)  # identifying the named entity label
            
            # question generation according to the person named entity
            if label == "PERSON" or label == "ORG":
                question = sentence.replace(subject, "Who ");
                question = question + ' ?'
                # print("WHO1 ************************************************************ " + question)
                return question
            else:
                question = question + "Who " + verb + " " + subject + " ?"
                # print("WHO2 **************************************************************** " + question)
                return question
        else:
            return question
