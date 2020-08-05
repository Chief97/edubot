from flask import Flask, request, jsonify

from Service.Self_Assess_Question_Generation.QuestionGenerationService import QuestionGenerationService

app = Flask(__name__)

questionGenerationService = QuestionGenerationService()

################################################# Start Doubt Detection End points ##############################################################

################################################# End Doubt Detection End points ################################################################


################################################# Start Doubt Response End points ###############################################################

################################################# End Doubt Response End points #################################################################


################################################# Start Question Generation End points ##########################################################

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

################################################# End Question Generation End points ############################################################


################################################# Start Answer Generation End points ##############################################################

################################################# End Question Generation End points ##############################################################

app.run(debug=True)