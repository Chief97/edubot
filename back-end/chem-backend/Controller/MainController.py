from flask import Flask, request, jsonify

from Service.Self_Assess_Question_Generation.QuestionGenerationService import QuestionGenerationService

app = Flask(__name__)

questionGenerationService = QuestionGenerationService()


@app.route('/selfEvaluate/questionGeneration/importantSentences', methods=['POST'])
def allImportantSentences():
    textInput = request.get_json()['text']
    sentences = questionGenerationService.importantSentences(textInput)
    return sentences


@app.route('/selfEvaluate/questionGeneration/allQuestions', methods=['POST'])
def allQuestions():
    textInput = request.get_json()['text']
    allQuestionsForPara = questionGenerationService.executeQuestionGeneration(textInput)
    return jsonify(allQuestionsForPara)


app.run(debug=True)