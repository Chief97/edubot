
import nltk

class QuestionTypeIdentification(object):
    def identify_question_type(self,question):

        # words = question.split()
        words = nltk.word_tokenize(question)

        hverbs = ["is", "have", "had", "was", "could", "would", "will", "do", "did", "should", "shall", "can", "are"]
        isWhType = False
        isDash = False
        isYesNo = False
        isHow = False
        isNone = False
        for word in words:
            if word == "what" or word == "where" or word == "who" or word == "which" or word == "why":

                isWhType = True
            elif word == "dash":
                isDash = True
            elif word in hverbs:
                if isHow == False:
                    isYesNo = True
            elif (nltk.word_tokenize(question)[0] == "how"):
                isHow = True
            else:
                isNone = True

        if isWhType :
            return ["wh", "mcq"]
        if isDash:
            return ["blank", "mcq"]
        if isYesNo:
            return ["yes-no"]
        if isHow:
            return ["how"]
        if isNone:
            return ["None"]

    def identify_question_start(self,question):
        question_words = nltk.word_tokenize(question)
        if "who" in question_words:
            return "who"
        elif "what" in question_words:
            return "what"
        elif "when" in question_words:
            return "when"
        elif "where" in question_words:
            return "where"
        elif "why" in question_words:
            return "why"
        elif "how" in question_words:
            return "how"
        else:
            return "none"

    def identify_singleOrMultipleAnswer(self,question):
        print(question.value)
        # print(nltk.word_tokenize(question.value)[1])
        # if(nltk.word_tokenize(question.value)[1] == "are" or nltk.word_tokenize(question.value)[1] == "were"):
        #     question.answerObject.isSingle = False

        return question
