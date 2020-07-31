class Question(object):

    def __init__(self):
        self.sentence = "";
        self.questions = [];

    def convertToJson(self):
        return {
            'sentence': self.sentence,
            'questions': self.questions
        }
