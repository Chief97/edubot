from flask import Flask, request, jsonify

from Other_Features.UserAccessManagement import UserAccessManagement
from Service.Self_Learn_Doubt_Detection.DoubtDetectionService import DoubtDetectionService
from Service.Self_Assess_Question_Generation.QuestionGenerationService import QuestionGenerationService
from Service.Self_Learn_Doubt_Response.DoubtResponseService import DoubtResponseService

app = Flask(__name__)

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
doubtDetectionService = DoubtDetectionService()


@app.route('/selfLearn/doubtDetection/getIntent', methods=['POST'])
def detectIntent_id():
    textInput = request.get_json()['text']
    intent_id = doubtDetectionService.getIntent(textInput)
    return intent_id


################################################# End Doubt Detection End points ################################################################


################################################# Start Doubt Response End points ###############################################################
doubtResponseService = DoubtResponseService()


@app.route('/scraper', methods=['POST'])
def webScraper():
    doubtResponseService.startScraper()


@app.route('/selfLearn/doubtResponse/prepareData', methods=['POST'])
def prepare_data():
    # text = request.get_json()['text']
    data = doubtResponseService.collect_data()
    return jsonify(data)


################################################# End Doubt Response End points #################################################################


################################################# Start Question Generation End points ##########################################################

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


################################################# End Question Generation End points ############################################################


################################################# Start Answer Generation End points ##############################################################

################################################# End Question Generation End points ##############################################################

app.run(debug=True)
