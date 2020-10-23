"""
    Question class is used to store the questions list
    along with the sentence which the questions list was
    generated.
"""


class Question(object):

    def __init__(self):
        self.sentence = "";
        self.questions = [];

    def convertToJson(self):
        return {
            'sentence': self.sentence,
            'questions': self.questions
        }
