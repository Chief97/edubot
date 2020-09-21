from flask import jsonify

from General.Self_Learn_Doubt_Detection.ClassifyInput import ClassifyInput


class DoubtDetectionService(object):

    def getIntent(self, inputText):
        doubtDetection = ClassifyInput()
        result = doubtDetection.classify(inputText)
        result_ = ' '.join(result)

        return jsonify(result_)
