
import nltk

class QuestionTypeIdentification(object):
    def identify_question_type(self,question):
        words = question.split()
        length = len(words)
        hverbs = ["is", "have", "had", "was", "could", "would", "will", "do", "did", "should", "shall", "can", "are"]
        print(question)
        for word in words:
            if word == "what" or word == "where" or word == "who" or word == "which" or word == "why":
                return ["wh", "mcq"]
            elif word == "@dash":
                return ["blank", "mcq"]
            elif word in hverbs:
                return ["yes-no"]
            elif (nltk.word_tokenize(question)[0] == "how") and (nltk.word_tokenize(question)[1] == "many"):
                return ["howMany"]
            else:
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
        else:
            return "none"

    def identify_singleOrMultipleAnswer(self,question):
        print(question.value)
        # print(nltk.word_tokenize(question.value)[1])
        # if(nltk.word_tokenize(question.value)[1] == "are" or nltk.word_tokenize(question.value)[1] == "were"):
        #     question.answerObject.isSingle = False

        return question
