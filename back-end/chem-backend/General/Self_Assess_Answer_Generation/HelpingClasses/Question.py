from General.Self_Assess_Answer_Generation.HelpingClasses.Answer import Answer


class Question(object):
    def __init__(self, question_value):
        self.value = question_value
        self.questionType = ""
        self.answerObject = Answer()
        self.sentence = ""
        self.question_start = ""

    def convertToJson(self):
        return {
            'question': self.value,
            'correctAnswer': self.answerObject.correctAnswer,
            'answerOptions' : self.answerObject.mcqAnswer,
            'position' : self.answerObject.position
        }