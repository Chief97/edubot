from flask import Flask, request

from Service.Self_Assess_Question_Generation.QuestionGenerationService import QuestionGenerationService
from Service.Self_Learn_Doubt_Response.DoubtResponseService import GenerateResponse

app = Flask(__name__)

questionGenerationService = QuestionGenerationService()
generateResponse = GenerateResponse()


@app.route('/iSentences', methods=['POST'])
def allImportantSentences():
    textInput = request.get_json()['text']
    sentences = questionGenerationService.importantSentences(textInput)
    return sentences

@app.route('/scraping' , methods=[''])
def webScraper():
    textInput = request.get_json()['text']
    webScrape = generateResponse.webScraper(textInput)

@app.route('/searchKeywords', methods=['GET'])
def searchKeywords ():



app.run(debug=True)