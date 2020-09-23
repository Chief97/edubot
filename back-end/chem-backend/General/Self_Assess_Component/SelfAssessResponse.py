class SelfAssessResponse(object):
    def __init__(self):
        self.question = ""
        self.answerOptions = []
        self.correctAnswer = ""
        self.position = 0

    def convertToJson(self):
        return {
            'question': self.question,
            'answerOptions': self.answerOptions,
            'correctAnswer': self.correctAnswer,
            'position': self.position
        }