from flask import Flask, request, jsonify
# from flask_script import Manager, Server

from flask_cors import CORS

from General.Self_Assess_Component.SelfAssessResponse import SelfAssessResponse
from Other_Features.UserAccessManagement import UserAccessManagement
from Service.Self_Assess_Answer_Generation.AnswerGenerationService import AnswerGenerationService
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

################################################# Start Self Assess Component ###################################################################

questionGenerationService1 = QuestionGenerationService()
answerGenerationService1 = AnswerGenerationService()

# @app.route('/selfAssess/getQuestions', methods=['POST'])
# def retrieveQuestions():
#     textInput = request.get_json()['data']
#     questionCategory = textInput["questionCategory"]
#     sectionName = textInput["sectionName"]
#     questionType = textInput["questionType"]
#
#     if questionCategory != "" and sectionName == "" and questionType == "":
#         print("get questions from firebase")
#     elif questionCategory == "" and sectionName != "" and questionType != "":
#         textParagraph = questionGenerationService.retrieveText(sectionName)
#         allQuestionsForPara = questionGenerationService.executeQuestionGeneration(textInput)
#         print("get edubot question")

@app.route('/selfAssess/getQuestions', methods=['POST'])
def getMcqQuestions():

    textInput = request.get_json()['data']
    questionCategory = textInput["questionCategory"]
    sectionName = textInput["sectionName"]
    paragraph = textInput["paragraph"]
    questionType = textInput["questionType"]

    if questionCategory == "database" and sectionName == "" and questionType == "" and paragraph == "":
        return jsonify(questionGenerationService.retrieveQuestionsFromFirebase())
    elif questionCategory == "section" and sectionName != "" and questionType != "" and paragraph != "":
        mcqQuestionsList = list()
        for i in range(2):
            response = SelfAssessResponse()
            response.question = "Who invented planetary model?"
            response.answerOptions = ["Dimitry Mendeleff, Ernest Rutherfurd, Neils Bohr, John Doily"]
            response.correctAnswer = "Ernest Rutherfurd"
            response.position = 1
            mcqQuestionsList.append(response.convertToJson())
        return jsonify(mcqQuestionsList)


@app.route('/selfAssess/getSectionPara', methods=['GET'])
def getSectionPara():
    paraForSection = questionGenerationService.retrieveParaForSection()
    return jsonify(paraForSection)

@app.route('/selfAssess/getAllQuestions', methods=['POST'])
def getAllQuestions():

    textInput = request.get_json()['data']
    questionCategory = textInput["questionCategory"]
    sectionName = textInput["sectionName"]
    paragraph = textInput["paragraph"]
    questionType = textInput["questionType"]

    if questionCategory == "database" and sectionName == "" and questionType == "" and paragraph == "":
        return jsonify(questionGenerationService.retrieveQuestionsFromFirebase())
    elif questionCategory == "section" and sectionName != "" and questionType != "" and paragraph != "":
        mcqQuestionsList = questionGenerationService1.retrieveQuestionList(paragraph)
        # answerGenerationService1.autoAnswerGeneration(paragraph,mcqQuestionsList)
        return jsonify(answerGenerationService1.autoAnswerGeneration(paragraph,mcqQuestionsList))

################################################# End Self Assess Component ###################################################################

################################################# Start Doubt Detection End points ##############################################################
doubtDetectionService = DoubtDetectionService()
intent_id = ""


@app.route('/selfLearn/doubtDetection/getIntent', methods=['POST'])
def detectIntent_id():
    textInput = request.get_json()['data']
    print(textInput)
    intent_id = doubtDetectionService.getIntent(textInput)
    print("intentID")
    print(intent_id)
    #response(intent_id)
    #return intent_id
    return response(intent_id)



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
def response(text_input):
    #text_input = request.get_json()['text']
    # print(text)
    # text_input = text['text']
    print("text_input")
    print(text_input)
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

autoAnswerGenerationService = AnswerGenerationService()
@app.route('/selfEvaluate/answerGeneration/answer', methods=['POST'])
def allAnswers():
    textInput = request.get_json()['text']
    paragraph = textInput["paragraph"]
    questionList = textInput["questionList"]
    print("Initial ", questionList)
    allAnswersForQuestions = autoAnswerGenerationService.autoAnswerGeneration(paragraph,questionList)
    return jsonify(allAnswersForQuestions)

################################################# End Question Generation End points ##############################################################

app.run(debug=True)
