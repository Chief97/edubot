from flask import jsonify

from General.Self_Assess_Question_Generation.FetchImportantSentences import FetchImportantSentences
from General.Self_Assess_Question_Generation.PreProcess import PreProcess


class QuestionGenerationService(object):

    def importantSentences(self, textInput):
        preProcess = PreProcess()
        pretext = preProcess.preProcessPara(textInput)

        fetchImportantSentences = FetchImportantSentences();
        finalText = fetchImportantSentences.importantSentences(pretext);
        # Text = set(finalText);
        print(finalText)
        return jsonify(list(finalText))
