class SelfAssessInput(object):

    def __init__(self):
        self.sectionName = ""
        self.paragraph = ""

    def convertToJson(self):
        return {
            'name': self.sectionName,
            'paragraph': self.paragraph
        }