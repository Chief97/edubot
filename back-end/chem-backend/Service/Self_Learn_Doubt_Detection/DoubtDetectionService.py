from flask import jsonify

from General.Self_Learn_Doubt_Detection.DoubtDetection import DoubtDetection


class DoubtDetectionService(object):

    def getIntent(self, inputText):
        doubtDetection = DoubtDetection()
        result = doubtDetection.classify(inputText)

        print(result)
        return jsonify(list(result))
