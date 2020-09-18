from abc import ABC

from flask import Flask, request, jsonify
# from flask_script import Manager, Server

from flask_cors import CORS
from Other_Features.UserAccessManagement import UserAccessManagement
from Service.Self_Learn_Doubt_Detection.DoubtDetectionService import DoubtDetectionService
from Service.Self_Assess_Question_Generation.QuestionGenerationService import QuestionGenerationService
from Service.Self_Learn_Doubt_Response.DoubtResponseService import DoubtResponseService


# def prepare_data():
#     data = doubtResponseService.collect_data()
#     processing = doubtResponseService.process_data(data)
#     pass
#
#
# class CustomServer(Server):
#     def __call__(self, app, *args, **kwargs):
#         prepare_data()
#         return Server.__call__(self, app, *args, **kwargs)


app = Flask(__name__)
cors = CORS(app)


################################################# Start User access management End points #######################################################

userAccessManagement = UserAccessManagement()
userAccessManagement.initialization()


@app.route('/registerUser', methods=['POST'])
def registerUser():
    textInput = request.get_json()['data']
    response = userAccessManagement.registerUser(textInput)
    return jsonify(response)


@app.route('/validateUser', methods=['POST'])
def validateUserCredentials():
    textInput = request.get_json()['data']
    response = userAccessManagement.validateUserCredentials(textInput)
    return jsonify(response)


################################################# End User access management End points #########################################################


################################################# Start Doubt Detection End points ##############################################################
doubtDetectionService = DoubtDetectionService()
intent_id = ""


@app.route('/selfLearn/doubtDetection/getIntent', methods=['POST'])
def detectIntent_id():
    textInput = request.get_json()['text']
    intent_id = doubtDetectionService.getIntent(textInput)
    #response(intent_id)
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
    processing = doubtResponseService.process_data(data)
    return processing


@app.route('/selfLearn/doubtResponse/respond', methods=['POST'])
def response():
    text_input = request.get_json()['text']
    doubt_response = doubtResponseService.respond(text_input)
    print("respond hit")
    return doubt_response


################################################# End Doubt Response End points #################################################################


################################################# Start Question Generation End points ##########################################################

questionGenerationService = QuestionGenerationService()


@app.route('/selfEvaluate/questionGeneration/getSection', methods=['GET'])
def allSections():
    # textInput = request.get_json()['text']
    sections = questionGenerationService.retrieveSection()
    return sections


@app.route('/selfEvaluate/questionGeneration/getText', methods=['POST'])
def allText():
    section_name = request.get_json()['text']
    print("SECTION NAME : " + section_name)
    sections = questionGenerationService.retrieveText(section_name)
    return sections


@app.route('/selfEvaluate/questionGeneration/importantSentences', methods=['POST'])
def allImportantSentences():
    # textInput = request.get_json()['text']
    section_name = request.get_json()['text']
    textInput = questionGenerationService.retrieveText(section_name)
    sentences = questionGenerationService.importantSentences(textInput)
    return sentences


@app.route('/selfEvaluate/questionGeneration/allQuestions', methods=['POST'])
def allQuestions():
    # textInput = request.get_json()['text']
    section_name = request.get_json()['text']
    textInput = questionGenerationService.retrieveText(section_name)
    allQuestionsForPara = questionGenerationService.executeQuestionGeneration(textInput)
    return jsonify(allQuestionsForPara)


################################################# End Question Generation End points ############################################################


################################################# Start Answer Generation End points ##############################################################

################################################# End Question Generation End points ##############################################################

app.run(debug=True)
