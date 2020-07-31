from flask import Flask, request

from Service.Self_Assess_Question_Generation.QuestionGenerationService import QuestionGenerationService

app = Flask(__name__)

questionGenerationService = QuestionGenerationService()


@app.route('/iSentences', methods=['POST'])
def allImportantSentences():
    textInput = request.get_json()['text']
    sentences = questionGenerationService.importantSentences(textInput)
    return sentences


app.run(debug=True)