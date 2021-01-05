import nltk
import random
import re;
import spacy

from General.Self_Assess_Answer_Generation.HelpingClasses.Answer import Answer
from nltk.corpus import wordnet

from General.Self_Assess_Question_Generation.Helping_Classes.QuestionFormationHelper import QuestionFormationHelper
from General.Self_Assess_Question_Generation.PreProcess import PreProcess
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")


class AnswerExtraction(object):
    def answer_extraction_from_sentences(self, question, paragraph):

        helper = QuestionFormationHelper()
        print(
            "IN answer Extraction ------------------------------------------------------------------------------------------------------------------")

        if question.questionType[0] != "yes-no" and question.questionType[0] != "blank":

            if (question.question_start == "what"):
                print("what")
                answer = ""
                sent_POS = nltk.pos_tag(nltk.word_tokenize(paragraph))
                question1 = question.value
                print("QUESTION1 :::::::::::::::::" + question1)
                if str(question1).find("what") != -1:
                    question1 = str(question1).replace("what", "")
                    question1 = str(question1).replace("?", "")
                    print("QUESTION1 ::::::::::::::::: " + question1)
                    sentence = question.sentence
                    print("SENTENCE ::::::::::::::::: " + sentence)
                    question1 = question1.rstrip()
                    print("1111111111111111111111111 " + question1)
                    answer = self.extracting(sentence, question1)
                    dotRemovedAnswer = "";
                    for l in answer:
                        if l == ".":
                            dotRemovedAnswer = dotRemovedAnswer + " "
                        else:
                            dotRemovedAnswer = dotRemovedAnswer + l
                    answer = dotRemovedAnswer
                    print("ANSWER &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& " + answer)
                    # synonym = self.getSynonymsAndAntonyms(answer)
                    # print("SYNONYM :::::::::::::::::::: " + str(synonym))
                    # if str(sentence).find(question1) != -1 :
                    #     print("worked")
                    #     answer = str(sentence).replace(question1 ,"")
                    #     print("ANSWER &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& " + answer)
                    #     synonym = self.getSynonymsAndAntonyms(answer)
                    #     print("SYNONYM :::::::::::::::::::: " + str(synonym))
                # print(sent_POS)
                if answer == "":
                    sent_pos1 = nltk.pos_tag(nltk.word_tokenize(sentence))
                    for tag in sent_pos1:
                        if (tag[1] == "NN"):
                            answer = (tag[0])
                            break;
                    if answer == "":
                        answer = "Not Found"
                # for tag in sent_POS:
                # print(tag)
                sentence_NN = []
                for tag in sent_POS:
                    if (tag[1] == "NN"):
                        sentence_NN.append(tag[0])
                print(sentence_NN)
                print(question.value)
                possibleAnswer = []
                # for noun in sentence_NN:
                #     if noun not in nltk.word_tokenize(question.value):
                #         possibleAnswer.append(noun)
                # print(possibleAnswer)
                answer_obj = Answer
                # numbersList = random.sample(range(0, len(sentence_NN) - 1), 3)
                answer_obj.correctAnswer = answer
                answerOptions = list()
                answerOptions.append(answer)
                answerOptions = self.generateOptionsForWhatTypeQuestion(answer,question,paragraph,answerOptions)
                random.shuffle(answerOptions)
                answer_obj.mcqAnswer = answerOptions
                for j, i in enumerate(answerOptions):
                    if i == answer:
                        answer_obj.position = j + 1
                question.answerObject = answer_obj

                # for i in numbersList:
                #     answerOptions.append(sentence_NN[i])
                # answer = self.removeStopWords(answer)

                # print("random           :::: ", random.shuffle(answerOptions))
                # answer_obj.mcqAnswer = answerOptions
                # for j, i in enumerate(answerOptions):
                #     if i == answer:
                #         answer_obj.position = j + 1
                #
                # answer_obj.correctAnswer = answer
                # answer_obj.smallAnswer = answer_obj.mcqAnswer[answer_obj.correctAnswer]
                # question.answerObject = answer_obj
                print("POSSIBLE_ANSWER : ", answerOptions)
                print("CORRECT_ANSWER : ", answer)
                print(question.sentence, question.value)

                en_nlp = spacy.load('en_core_web_sm')
                doc = en_nlp(question.sentence)
                [self.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]

            elif (question.question_start == "who"):
                print("who")
                namesList = ['Ernest Rutherfurd', 'Neils Bohr', 'John Doily', 'Dimitri Mendeleeff', 'Albert Einstein',
                             'Marie Curie',
                             'Isaac Newton', 'Charles Darwin', 'Nikola Tesla', 'Galileo Galilei', 'Ada Lovelace',
                             'Pythagoras']
                initialSentence = ""
                for sent_para in nltk.sent_tokenize(paragraph):
                    if sent_para.lower() == question.sentence:
                        initialSentence = sent_para
                entityList = self.getLabel(initialSentence)
                print(entityList)
                answerOptions = list()
                answer = ''
                answer_obj = Answer
                for entity in entityList:
                    if entity[0] == "PERSON":
                        answer_obj.correctAnswer = entity[1]
                        # answerOptions.append(entity[1])
                        answer = entity[1]
                print(answer)
                numbersList = random.sample(range(0, len(namesList) - 1), 3)
                for i in numbersList:
                    answerOptions.append(namesList[i])
                answerOptions.append(answer)
                print("random           :::: ", random.shuffle(answerOptions))
                answer_obj.mcqAnswer = answerOptions
                answer_obj.correctAnswer = answer
                for j, i in enumerate(answerOptions):
                    if i == answer:
                        answer_obj.position = j + 1
                question.answerObject = answer_obj

            elif (question.question_start == "when"):
                print("when")
                initialSentence = ""
                for sent_para in nltk.sent_tokenize(paragraph):
                    if sent_para.lower() == question.sentence:
                        initialSentence = sent_para
                entityList = self.getLabel(initialSentence)
                print(entityList)
                for entity in entityList:
                    if entity[0] == "DATE":
                        question.answerObject.smallAnswer = entity[1]

            elif (question.question_start == "where"):
                print("where")
                initialSentence = ""
                for sent_para in nltk.sent_tokenize(paragraph):
                    if sent_para.lower() == question.sentence:
                        initialSentence = sent_para
                entityList = self.getLabel(initialSentence)
                print(entityList)
                for entity in entityList:
                    if entity[0] == "GPE":
                        question.answerObject.smallAnswer = entity[1]
            elif (question.question_start == "why"):
                print("why")
                conjunctionList = ["Because", "Hence", "Therefore", "But", "Because,", "Hence,", "Therefore,", "But,"]
                print(nltk.word_tokenize(question.sentence))
                questionSentenceTransformed = ""
                for i, word in enumerate(nltk.word_tokenize(question.sentence)):
                    if word in [",", "."]:
                        questionSentenceTransformed = questionSentenceTransformed + word
                    else:
                        if i == 0:
                            questionSentenceTransformed = questionSentenceTransformed + " " + word.capitalize()
                        else:
                            questionSentenceTransformed = questionSentenceTransformed + " " + word
                print("Transformed", questionSentenceTransformed)

                if nltk.word_tokenize(questionSentenceTransformed)[0] in conjunctionList:
                    print(paragraph)
                    for i, sentenceInPara in enumerate(nltk.sent_tokenize(paragraph)):
                        if sentenceInPara.strip() == questionSentenceTransformed.strip():
                            print("hit the sentence")
                            indexOfAnswerSentence = i - 1
                            answer = nltk.sent_tokenize(paragraph)[indexOfAnswerSentence]
                            answer_obj = Answer
                            answer_obj.correctAnswer = answer
                            answerOptions = list()
                            answerOptions.append(answer)
                            answerOptions = self.generateOptionsForWhyTypeQuestion(answer, question, paragraph,answerOptions)

                            random.shuffle(answerOptions)
                            answer_obj.mcqAnswer = answerOptions
                            for j, i in enumerate(answerOptions):
                                if i == answer:
                                    answer_obj.position = j + 1
                            question.answerObject = answer_obj
                    print("initial sentence")
                else:
                    print(paragraph)
                    for i, sentenceInPara in enumerate(nltk.sent_tokenize(paragraph)):

                        if sentenceInPara.strip() == questionSentenceTransformed.strip():
                            print("hit the sentence")
                            answer = self.helperForWhyQuestions(nltk.sent_tokenize(paragraph)[i])
                            answer_obj = Answer
                            answer_obj.correctAnswer = answer
                            answerOptions = list()
                            answerOptions.append(answer)
                            answerOptions = self.generateOptionsForWhyTypeQuestion(answer, question, paragraph,
                                                                                   answerOptions)

                            random.shuffle(answerOptions)
                            answer_obj.mcqAnswer = answerOptions
                            for j, i in enumerate(answerOptions):
                                if i == answer:
                                    answer_obj.position = j + 1
                            question.answerObject = answer_obj
                    print("middle of sentence")





            elif (question.questionType[0] == "how"):
                print("howMany")
                # print(question.value)
                # print(question.sentence)
                # answersList = list()
                # questionTokenized = nltk.word_tokenize(question.value)
                # sentenceTokenized = nltk.word_tokenize(question.sentence)
                #
                # for word in sentenceTokenized:
                #     if word not in questionTokenized:
                #         answersList.append(word)
                #
                # for word,i in enumerate(answersList):
                #     if word in nltk.corpus.stopwords.words('english'):
                #         answersList.pop(i);
                # answer = str(answersList)
                # answer_obj = Answer
                # answer_obj.correctAnswer = answer
                # answerOptions = list()
                # answerOptions.append("a")
                # answerOptions.append("b")
                # answerOptions.append("c")
                # answerOptions.append(answer)
                # random.shuffle(answerOptions)
                # answer_obj.mcqAnswer = answerOptions
                # for j, i in enumerate(answerOptions):
                #     if i == answer:
                #         answer_obj.position = j + 1
                # question.answerObject = answer_obj

        else:
            if question.questionType[0] == "yes-no":
                isYes = True;
                isNo = False;
                print("Yes NO")
                print(question.value)
                print(question.sentence)
                questionTokenized = nltk.word_tokenize(question.value)
                sentenceTokenized = nltk.word_tokenize(question.sentence)

                questionTokenized.pop(len(questionTokenized) - 1)
                sentenceTokenized.pop(len(sentenceTokenized) - 1)

                for word in questionTokenized:
                    if word not in sentenceTokenized:
                        isYes = False
                        isNo = True
                answer_obj = Answer
                answer_obj.mcqAnswer = ['Yes', 'No']
                if isNo:
                    answer_obj.position = 2
                    answer_obj.correctAnswer = 'No'
                if isYes:
                    answer_obj.position = 1
                    answer_obj.correctAnswer = 'Yes'
                print("tokenized question ", questionTokenized)
                print("tokenized sentence ", sentenceTokenized)
                question.answerObject = answer_obj
            if question.questionType[0] == "blank":
                print("dash")
                answer = ""
                sentence = question.sentence
                wordDic = {'Thus, ': '',
                           'Hence, ': '',
                           'Hence ': '',
                           'Therefore,': '',
                           'But,': '',
                           'But': '',
                           'Similarly': '',
                           'Therefore': '',
                           'thus, ': '',
                           'hence, ': '',
                           'hence ': '',
                           'therefore,': '',
                           'but,': '',
                           'but': '',
                           'similarly': '',
                           'therefore': ''
                           }  # word dictionary
                p = PreProcess()
                sentence = p.multipleReplace(sentence, wordDic)
                print("pre processed: ", sentence)
                questionTokenized = nltk.word_tokenize(question.value)
                sentenceTokenized = nltk.word_tokenize(sentence)
                for i, word in enumerate(questionTokenized):
                    if word == "dash":
                        index = i
                        answer = sentenceTokenized[index]
                        break
                print(answer)
                answer_obj = Answer
                answer_obj.correctAnswer = answer
                answerOptions = list()
                answerOptions.append(answer)
                answerOptions = self.generateOptionsForFillInTheBlank(answer,question,paragraph,answerOptions)
                random.shuffle(answerOptions)
                answer_obj.mcqAnswer = answerOptions
                for j, i in enumerate(answerOptions):
                    if i == answer:
                        answer_obj.position = j + 1
                question.answerObject = answer_obj
                questionGenerated = question.value
                question.value = questionGenerated.replace("dash", "_______")

                print("QUESTION ::::::::::::: " + questionGenerated)
        question.value = question.value.capitalize()
        print(
            "OUT answer Extraction ------------------------------------------------------------------------------------------------------------------")
        return question

    def to_nltk_tree(self, node):
        if node.n_lefts + node.n_rights > 0:
            return nltk.Tree(self.tok_format(node), [self.to_nltk_tree(child) for child in node.children])
        else:
            return self.tok_format(node)

    def tok_format(self, tok):
        return "_".join([tok.orth_, tok.tag_])

    def getLabel(self, sentence):
        doc = nlp(sentence)
        entityList = []

        for e in doc.ents:
            entityList.append([e.label_, e.text])

        return entityList

    def getSynonymsAndAntonyms(self, word):
        synonyms = []
        antonyms = []

        for synonym in wordnet.synsets(word):
            for l in synonym.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())

        return synonyms, antonyms

    def extracting(self, sentence, question):
        answer = ""
        print("SENTENCE IN EXTRACTION :::::::::  ", sentence)
        print("QUESTION IN EXTRACTION :::::::::  ", question)
        # if sentence.find(question) != -1:
        #     answer = sentence.replace(question,"",1)
        #     print("ANSWER important : " + answer)
        # if question in sentence:
        #     answer = sentence.replace(question, "", 1)
        #     print("ANSWER important : " + answer)
        wordDic = {'Thus, ': '', 'Hence, ': '', 'Hence ': '', 'Therefore,': '', 'But,': '', 'But': '', 'Similarly': '',
                   'Therefore': '', 'thus, ': '', 'hence, ': '', 'hence ': '', 'therefore,': ' ', 'but,': '', 'but': '',
                   'similarly': '',
                   'therefore': ''}
        p = PreProcess()
        sentence = p.multipleReplace(sentence, wordDic)
        print("replaced question :::: " + sentence)
        question = question.lstrip()
        if sentence.find(question) != -1:
            answer = sentence.replace(question, " ", 1)
        # words = question.lstrip().split(" ")
        # print(words)
        # for w in words:
        #     if sentence.find(w) != -1:
        #         print("INSIDE IF ")
        #         answer = sentence.replace(w,"")
        # answer = re.sub(question," ")
        print("ANSWER VERY IMPORTANT : " + answer)
        if answer == "":
            tokens = question.split(" ")
            print("TOKENS :::::::::::::::: " + str(tokens))
            for t in tokens:
                sentence = sentence.replace(t, "", 1)
                answer = sentence
                print("ANSWER??????? " + answer)
        return answer

    def generateOptions(self, answer,type):
        optionList = list()
        optionList.append("a")
        optionList.append("b")
        optionList.append("c")
        optionList.append(answer)

        return optionList

    def generateOptionsForFillInTheBlank(self, answer, question,paragraph,optionList):

        sentence_NN = []


        if any(char.isdigit() for char in answer) :
            numbersList = random.sample(range(0, 25), 3)
            for i in numbersList:
                if i not in optionList:
                    optionList.append(i)
        else :
            sent_POS = nltk.pos_tag(nltk.word_tokenize(paragraph))

            for tag in sent_POS:
                if (tag[1] == "NN") and tag [0] not in sentence_NN:
                    sentence_NN.append(tag[0])
            print(sentence_NN)
            numbersList = random.sample(range(0, len(sentence_NN) - 1), 3)
            for i in numbersList:
                if sentence_NN[i] not in optionList:
                    optionList.append(sentence_NN[i])


        return optionList

    def generateOptionsForWhatTypeQuestion(self, answer, question,paragraph,optionList):

        sentence_NN = []

        if any(char.isdigit() for char in answer):
            numbersList = random.sample(range(0, 25), 3)
            for i in numbersList:
                if i not in optionList:
                    optionList.append(i)
        else:
            sent_POS = nltk.pos_tag(nltk.word_tokenize(paragraph))
            helper = QuestionFormationHelper()
            subject = helper.getSubject(answer)
            option = ""
            for tag in sent_POS:
                if (tag[1] == "NN") and tag[0] not in sentence_NN:
                    op = tag[0]
                    op = op + " "
                    option = answer.replace(subject,op,1)
                    if option not in sentence_NN :
                        sentence_NN.append(option)
            print("The length of options ",len(sentence_NN))
            print(" options ",sentence_NN)
            lengthCurrent = len(sentence_NN)
            if lengthCurrent >= 3 :
                numbersList = random.sample(range(0, len(sentence_NN) - 1), 3)
                for i in numbersList:
                    if sentence_NN[i] not in optionList:
                        optionList.append(sentence_NN[i])
            else :
                missingOption = 3 - lengthCurrent
                for tag in sent_POS:
                    if (tag[1] == "NN") and tag[0] not in sentence_NN:
                        sentence_NN.append(tag[0])
                print(sentence_NN)
                numbersList = random.sample(range(0, len(sentence_NN) - 1), missingOption)
                for i in numbersList:
                    if sentence_NN[i] not in optionList:
                        optionList.append(sentence_NN[i])

        return optionList

    def generateOptionsForWhyTypeQuestion(self, answer, question,paragraph,optionList):

        sentence_NN = []

        if any(char.isdigit() for char in answer):
            numbersList = random.sample(range(0, 25), 3)
            for i in numbersList:
                if i not in optionList:
                    optionList.append(i)
        else:
            sent_POS = nltk.pos_tag(nltk.word_tokenize(paragraph))
            helper = QuestionFormationHelper()
            subject = helper.getSubject(answer)
            option = ""
            for tag in sent_POS:
                if (tag[1] == "NN") and tag[0] not in sentence_NN:
                    op = tag[0]
                    op = op + " "
                    option = answer.replace(subject,op,1)
                    if option not in sentence_NN :
                        sentence_NN.append(option)
            print("The length of options ",len(sentence_NN))
            print(" options ",sentence_NN)
            lengthCurrent = len(sentence_NN)
            if lengthCurrent >= 3 :
                numbersList = random.sample(range(0, len(sentence_NN) - 1), 3)
                for i in numbersList:
                    if sentence_NN[i] not in optionList:
                        optionList.append(sentence_NN[i])
            else :
                missingOption = 3 - lengthCurrent
                for tag in sent_POS:
                    if (tag[1] == "NN") and tag[0] not in sentence_NN:
                        sentence_NN.append(tag[0])
                print(sentence_NN)
                numbersList = random.sample(range(0, len(sentence_NN) - 1), missingOption)
                for i in numbersList:
                    if sentence_NN[i] not in optionList:
                        optionList.append(sentence_NN[i])

        return optionList


    def helperForWhyQuestions(self, sentence):
        sentencePart = ""
        helper = QuestionFormationHelper()
        if str(sentence).find('because') != -1:
            sentencePart = helper.slicer1(sentence, 'because');
        elif str(sentence).find('therefore') != -1:
            sentencePart = helper.slicer1(sentence, 'therefore');
        elif str(sentence).find('therefore,') != -1:
            sentencePart = helper.slicer1(sentence, 'therefore,');
        elif str(sentence).find('therefore,') != -1:
            sentencePart = helper.slicer1(sentence, 'because,');

        return sentencePart

    def removeStopWords (self,answer) :
        print("Before :",answer)
        answer = answer.strip()
        print("After :", answer)
        stopwords = nltk.corpus.stopwords.words('english');
        text_in_lowercase = re.sub("[^a-zA-Z]", " ", str(answer)).split(" ");
        filtered_text = []
        for word in text_in_lowercase:
            if word not in stopwords:
                filtered_text.append(word);
        answer = " ".join(str(x) for x in filtered_text)
        print("After  removal:", answer)
        return answer