import language_tool_python
import firebase_admin
import random

from flask import jsonify
from firebase_admin import credentials
from firebase_admin import firestore
from General.Self_Assess_Question_Generation.FetchImportantSentences import FetchImportantSentences
from General.Self_Assess_Question_Generation.PreProcess import PreProcess
from General.Self_Assess_Question_Generation.Question import Question
from General.Self_Assess_Question_Generation.QuestionFormation import QuestionFormation


class QuestionGenerationService(object):

    def retrieveSection(self):
        # section_name = section_name.lower()
        # section_name = section_name.replace(" ","_")
        # section_name = "matter_" + section_name
        db = firestore.client()
        doc_ref = db.collection(u'section_content').stream()
        # doc = doc_ref.getAll()
        sections = list()
        # print("LENGTH : " + str(len(doc_ref)))
        for x in doc_ref:
            # print(x.id)
            # section_name = str(x.id).replace("matter_", "")
            # section_name = section_name.replace("_", " ")
            # section_name = section_name.lstrip().capitalize()
            section_name = str(x.id)
            sections.append(section_name)
        for i in sections:
            print(i)
        return jsonify(sections)
        # return doc
        # if doc != 0:
        #     data_dic = doc.to_dict()
        #     print(data_dic)
        #     return data_dic
        # else:
        #     print("This section does not exists")
        #     return "This section does not exists"

    def retrieveText(self,section_name):
        db = firestore.client()
        doc_ref = db.collection(u'section_content').document(section_name)
        doc = doc_ref.get()
        data_dic = doc.to_dict()
        print(len(data_dic))
        listLength = len(data_dic) - 1
        paragraph = ""
        paragraphList = list()
        if listLength == 1:
            paragraph = data_dic["para1"]
        else:
            for i in range(1, len(data_dic)):
                para = "para"+str(i)
                paraval = data_dic[para]
                if paraval != "":
                    paragraphList.append(data_dic[para])
                else:
                    break
            paragraph = random.choice(paragraphList)

        # for i in range(1,10):
        #     para = "para"+str(i)
        #     paraval = data_dic[para]
        #     if paraval != "":
        #         paragraphList.append(data_dic[para])
        #     else:
        #         break
        # para1 = data_dic["para1"]
        # print("PARA1 " + para1)
        # para2 = data_dic["para2"]
        # print("PARA2 " + para2)
        # paragraphList.append(para1)

        # paragraph = random.choice(paragraphList)
        # print(paragraph)
        return paragraph

    def importantSentences(self, textInput):
        preProcess = PreProcess()
        pretext = preProcess.preProcessPara(textInput)

        fetchImportantSentences = FetchImportantSentences();
        finalText = fetchImportantSentences.importantSentences(pretext);
        # Text = set(finalText);
        print(finalText)
        return jsonify(list(finalText))

    def executeQuestionGeneration(self, textInput):
        preProcess = PreProcess()
        pretext = preProcess.preProcessPara(textInput)
        tool = language_tool_python.LanguageToolPublicAPI('en-US')
        fetchImportantSentences = FetchImportantSentences();
        finalText = fetchImportantSentences.importantSentences(pretext);
        Text = set(finalText);

        allQuestionsForPara = []
        for i, y in enumerate(Text):
            questions = Question()
            sentence = y.lstrip().replace("\n", "")
            questions.sentence = sentence
            print(questions.sentence)
            questionList = []
            question = QuestionFormation()
            how_question = question.generateHowQuestion(sentence);
            fill_in_blanks_question = question.fillInBlanks(sentence);
            why_question = question.generateWhyQuestion(sentence);
            yes_question = question.createYesUsingHVerbPhrase(sentence);
            no_question = question.createNoUsingHVerbPhrase(sentence);
            wh_question = question.generateWHQuestion(sentence)
            print(" wh QUESTION *************************************** " + wh_question)
            who_question = question.generateWhoTypeQuestion(sentence)
            if how_question is not None and how_question != "":
                how_question = tool.correct(str(how_question))
                questionList.append(how_question)
            if fill_in_blanks_question != '':
                questionList.append(fill_in_blanks_question)
            if why_question != '':
                why_question = tool.correct(str(why_question))
                questionList.append(why_question)
            if yes_question != '':
                yes_question = tool.correct(str(yes_question))
                questionList.append(yes_question)
            if no_question != '':
                # newly added
                if yes_question != no_question:
                    no_question = tool.correct(str(no_question))
                    questionList.append(no_question)
            if wh_question != '':
                wh_question = tool.correct(str(wh_question))
                questionList.append(wh_question)
            if who_question is not None and who_question != '':
                who_question = tool.correct(str(who_question))
                questionList.append(who_question)
            questions.questions = list(set(questionList))
            allQuestionsForPara.append(questions.convertToJson())
        return allQuestionsForPara
