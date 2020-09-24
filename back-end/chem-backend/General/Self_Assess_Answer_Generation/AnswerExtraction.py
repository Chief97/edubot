import nltk
import random

import spacy

from General.Self_Assess_Answer_Generation.HelpingClasses.Answer import Answer
from nltk.corpus import wordnet
nlp = spacy.load("en_core_web_sm")
class AnswerExtraction(object):
    def answer_extraction_from_sentences(self,question,paragraoh):

        if(question.question_start == "what"):
            print("what")
            sent_POS = nltk.pos_tag(nltk.word_tokenize(paragraoh))
            question1 = question.value
            print("QUESTION1 :::::::::::::::::" + question1)
            if str(question1).find("what") != -1:
                question1 = str(question1).replace("what","")
                question1 = str(question1).replace("?", "")
                print("QUESTION1 ::::::::::::::::: " +question1)
                sentence = question.sentence
                print("SENTENCE ::::::::::::::::: " + sentence)
                question1 = question1.rstrip() + '.'
                print("1111111111111111111111111 " + question1)
                if str(sentence).find(question1) != -1 :
                    answer = str(sentence).replace(question1 ,"")
                    print("ANSWER &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& " + answer)
                    synonym = self.getSynonymsAndAntonyms(answer)
                    print("SYNONYM :::::::::::::::::::: " + str(synonym))
            # print(sent_POS)
            for tag in sent_POS:
                print(tag)
            sentence_NN = []
            for tag in sent_POS:
                if (tag[1] == "NN"):
                    sentence_NN.append(tag[0])
            print(sentence_NN)
            print(question.value)
            possibleAnswer = []
            for noun in sentence_NN:
                if noun not in nltk.word_tokenize(question.value):
                    possibleAnswer.append(noun)
            print(possibleAnswer)
            answer_obj = Answer
            numbersList = random.sample(range(0,len(sentence_NN)-1), 3)
            answerOptions = list()
            for i in numbersList:
                answerOptions.append(sentence_NN[i])
            answerOptions.append(answer)
            print("random           :::: ",random.shuffle(answerOptions))
            answer_obj.mcqAnswer = answerOptions
            for j,i in enumerate(answerOptions):
                if i == answer:
                    answer_obj.position = j+1

            answer_obj.correctAnswer = answer
            # answer_obj.smallAnswer = answer_obj.mcqAnswer[answer_obj.correctAnswer]
            question.answerObject = answer_obj
            print("POSSIBLE_ANSWER : ", answerOptions)
            print("CORRECT_ANSWER : ", answer)
            print(question.sentence, question.value)


            en_nlp = spacy.load('en_core_web_sm')
            doc = en_nlp(question.sentence)
            [self.to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
        elif(question.question_start == "who"):
            print("who")
            namesList = ['Ernest Rutherfurd','Neils Bohr','John Doily','Dimitri Mendeleeff','Albert Einstein','Marie Curie',
            'Isaac Newton','Charles Darwin','Nikola Tesla','Galileo Galilei','Ada Lovelace','Pythagoras']
            initialSentence = ""
            for sent_para in nltk.sent_tokenize(paragraoh):
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
                    answerOptions.append(entity[1])
                    answer = entity[1]

            numbersList = random.sample(range(0, len(namesList) - 1), 3)
            for i in numbersList:
                answerOptions.append(namesList[i])
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
            for sent_para in nltk.sent_tokenize(paragraoh):
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
            for sent_para in nltk.sent_tokenize(paragraoh):
                if sent_para.lower() == question.sentence:
                    initialSentence = sent_para
            entityList = self.getLabel(initialSentence)
            print(entityList)
            for entity in entityList:
                if entity[0] == "GPE":
                    question.answerObject.smallAnswer = entity[1]

        elif (question.questionType[0] == "howMany"):
            print("howMany")
            initialSentence = ""
            for sent_para in nltk.sent_tokenize(paragraoh):
                if sent_para.lower() == question.sentence:
                    initialSentence = sent_para
            entityList = self.getLabel(initialSentence)
            print(entityList)
            for entity in entityList:
                if entity[0] == "CARDINAL":
                    question.answerObject.smallAnswer = entity[1]

        elif question.question_start != "what" and question.question_start != "who" and question.question_start != "when" and question.question_start != "where" and question.question_start != "howMany":
            print("YES NO")
            answer_obj = Answer
            answer_obj.mcqAnswer = ['Yes','No']
            # answer_obj.mcqAnswer = answerOptions
            answer_obj.position = 1
            answer_obj.correctAnswer = 'Yes'
            question.answerObject = answer_obj
        question.value = question.value.capitalize()
        return question

    def to_nltk_tree(self,node):
        if node.n_lefts + node.n_rights > 0:
            return nltk.Tree(self.tok_format(node), [self.to_nltk_tree(child) for child in node.children])
        else:
            return self.tok_format(node)

    def tok_format(self,tok):
        return "_".join([tok.orth_, tok.tag_])

    def getLabel(self,sentence):
        doc = nlp(sentence)
        entityList = []


        for e in doc.ents:
            entityList.append([e.label_,e.text])

        return entityList

    def getSynonymsAndAntonyms(self,word):
        synonyms = []
        antonyms = []

        for synonym in wordnet.synsets(word):
            for l in synonym.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())

        return  synonyms,antonyms