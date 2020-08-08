from flask import jsonify

from General.Self_Assess_Question_Generation.FetchImportantSentences import FetchImportantSentences
from General.Self_Assess_Question_Generation.PreProcess import PreProcess
from General.Self_Assess_Question_Generation.Question import Question
from General.Self_Assess_Question_Generation.QuestionFormation import QuestionFormation


class QuestionGenerationService(object):

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
            if how_question is not None and how_question != "":
                questionList.append(how_question)
            if fill_in_blanks_question != '':
                questionList.append(fill_in_blanks_question)
            if why_question != '':
                questionList.append(why_question)
            if yes_question != '':
                questionList.append(yes_question)
            if no_question != '':
                # newly added
                if yes_question != no_question:
                    questionList.append(no_question)
            if wh_question != '':
                questionList.append(wh_question)
            questions.questions = questionList
            allQuestionsForPara.append(questions.convertToJson())
        return allQuestionsForPara