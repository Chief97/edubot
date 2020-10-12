import language_tool_python
import firebase_admin
import random
import re
from flask import jsonify
from firebase_admin import credentials
from firebase_admin import firestore

from General.Self_Assess_Component.SelfAssessInput import SelfAssessInput
from General.Self_Assess_Component.SelfAssessResponse import SelfAssessResponse
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

    def retrieveText(self, section_name):
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
                para = "para" + str(i)
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

    ## Component related
    def retrieveParaForSection(self):
        db = firestore.client()
        doc_ref = db.collection(u'section_content').stream()
        sectionParaList = list()
        for x in doc_ref:
            response = SelfAssessInput()
            section_name = str(x.id)
            response.sectionName = section_name
            response.paragraph = self.retrieveText(section_name)
            sectionParaList.append(response.convertToJson())

        return sectionParaList

    def retrieveQuestionsFromFirebase(self):

        db = firestore.client()
        doc_ref1 = db.collection('question').stream()
        types = list()
        for x in doc_ref1:
            type_name = str(x.id)
            types.append(type_name)
        questions = list()
        for i in types:
            doc_ref2 = db.collection('question').document(i)
            doc = doc_ref2.get()
            if doc.exists:
                data_dic = doc.to_dict()
                question = data_dic['type']
                questions.append(question)

        doc_ref3 = db.collection(u'element').stream()
        elements = list()
        mcqQuestionsList = list()
        for x in doc_ref3:
            element_name = str(x.id)
            elements.append(element_name)
        numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        for l in range(len(questions)):
            response = SelfAssessResponse()
            if questions[l].find('@element.name') != -1:
                element = random.choice(elements)
                question = questions[l].replace('@element.name', element)
                response.question = question
                type1 = types[l]
                print("T " + type1)
                doc_ref4 = db.collection(u'element').document(element)
                doc = doc_ref4.get()
                data_dic = doc.to_dict()
                answer = data_dic[type1]
                print("A " + answer)
                response.correctAnswer = answer

                if type1 != 'symbol':
                    answerOptions = []
                    numbersList = random.sample(range(0, 20), 3)
                    numbersList1 = ['21','22','23','24','25']
                    for i in numbersList:
                        if answer == i:
                            answerOptions.append(str(random.choice(numbersList1)))
                        answerOptions.append(str(i))
                    answerOptions.append(answer)
                    print("random           :::: ", random.shuffle(answerOptions))
                    for j, i in enumerate(answerOptions):
                        if i == answer:
                            response.position = j + 1
                    response.answerOptions = answerOptions
                else:
                    answerOptions = []
                    numbersList = random.sample(range(0, 19), 3)
                    numbersList1 = ['21', '22', '23', '24', '25']
                    symbols = ['H', 'He', 'li', 'Be', 'B', 'N', 'C', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S',
                               'Cl', 'Ar', 'K', 'Ca', 'Kr', 'Se', 'Ti', 'Co', 'Mn' ,'Cr']
                    # symbols_copy = symbols
                    for i in numbersList:
                        if answer == symbols[i]:
                            answerOptions.append(symbols[(random.choice(numbersList1))])
                        answerOptions.append(symbols[i])
                    answerOptions.append(answer)
                    print("random           :::: ", random.shuffle(answerOptions))
                    for j, i in enumerate(answerOptions):
                        if i == answer:
                            response.position = j + 1
                    response.answerOptions = answerOptions
                mcqQuestionsList.append(response.convertToJson())
            # if questions[l].find('@element.symbol') != -1:
            #     symbols = ['H','He','li','Be','B','N','C','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca']
            #     symbol = random.choice(symbols)
            #     question = questions[l].replace('@element.symbol', symbol)
            #     response.question = question
            #     type1 = types[l]
            #     print("T " + type1)
            #     doc_ref4 = db.collection(u'element').document(element)
            #     doc = doc_ref4.get()
            #     data_dic = doc.to_dict()
            #     answer = data_dic[type1]
            #     print("A " + answer)
            #     response.correctAnswer = answer
            #     mcqQuestionsList.append(response.convertToJson())


            # print("TABLE NAME :::::::::::::::::::: " + str(table_name))
            # print("Attribute name :::::::::::::::::: " + str(attribute_name))

        return mcqQuestionsList
        #     table_name_regex = '^@+.$'
        #     table_name = re.match(table_name_regex,questionCategory)
        #     doc_ref2 = db.collection(u'element').stream()
        #     elements = list()
        #     mcqQuestionsList = list()
        #     # print("LENGTH : " + str(len(doc_ref)))
        #     for x in doc_ref2:
        #         element_name = str(x.id)
        #         elements.append(element_name)
        #     for i in range(len(elements)):
        #         response = SelfAssessResponse()
        #
        #         response.question = question_type.replace()

    def retrieveQuestionList(self, textPara):
        preProcess = PreProcess()
        pretext = preProcess.preProcessPara(textPara)
        tool = language_tool_python.LanguageToolPublicAPI('en-US')
        fetchImportantSentences = FetchImportantSentences();
        finalText = fetchImportantSentences.importantSentences(pretext);
        text = set(finalText);
        allQuestionsForPara = []
        for i, y in enumerate(text):
            # questions = Question()
            sentence = y.lstrip().replace("\n", "")
            # questions.sentence = sentence
            # print(questions.sentence)
            questionList = []
            question = QuestionFormation()
            # how_question = question.generateHowQuestion(sentence);
            why_question = question.generateWhyQuestion(sentence);
            yes_question = question.createYesUsingHVerbPhrase(sentence);
            wh_question = question.generateWHQuestion(sentence)
            who_question = question.generateWhoTypeQuestion(sentence)
            # if how_question is not None and how_question != "":
            #     how_question = tool.correct(str(how_question))
            #     questionList.append(how_question)
            if why_question != '':
                why_question = tool.correct(str(why_question))
                questionList.append(why_question)
            if yes_question != '':
                yes_question = tool.correct(str(yes_question))
                questionList.append(yes_question)
            if wh_question != '':
                wh_question = tool.correct(str(wh_question))
                questionList.append(wh_question)
            if who_question is not None and who_question != '':
                who_question = tool.correct(str(who_question))
                questionList.append(who_question)
            if len(questionList) != 0:
                finalQuestion = random.choice(questionList)
                allQuestionsForPara.append(finalQuestion)

        return allQuestionsForPara


