from flask import Flask, request, jsonify

from Other_Features.UserAccessManagement import UserAccessManagement
from Service.Self_Assess_Question_Generation.QuestionGenerationService import QuestionGenerationService
from Service.Self_Learn_Doubt_Response.DoubtResponseService import DoubtResponseService

app = Flask(__name__)

questionGenerationService = QuestionGenerationService()
doubtResponseService = DoubtResponseService()


################################################# Start User access management End points #######################################################

userAccessManagement = UserAccessManagement()
userAccessManagement.initialization()


@app.route('/selfEvaluate/registerUser', methods=['POST'])
def registerUser():
    textInput = request.get_json()['data']
    response = userAccessManagement.registerUser(textInput)
    return jsonify(response)


@app.route('/selfEvaluate/validateUser', methods=['POST'])
def validateUserCredentials():
    textInput = request.get_json()['data']
    response = userAccessManagement.validateUserCredentials(textInput)
    return jsonify(response)

################################################# End User access management End points #########################################################


################################################# Start Doubt Detection End points ##############################################################

################################################# End Doubt Detection End points ################################################################


################################################# Start Doubt Response End points ###############################################################


@app.route('/scraper', methods=['POST'])
def webScraper():
    doubtResponseService.startScraper()




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
