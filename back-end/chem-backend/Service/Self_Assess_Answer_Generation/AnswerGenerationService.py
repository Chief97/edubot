import nltk

from General.Self_Assess_Answer_Generation.AnswerExtraction import AnswerExtraction
from General.Self_Assess_Answer_Generation.QuestionTypeIdentification import QuestionTypeIdentification
from General.Self_Assess_Answer_Generation.SentenceIdentification import SentenceIdentification
from General.Self_Assess_Answer_Generation.HelpingClasses.Question import Question

class AnswerGenerationService(object):


    def autoAnswerGeneration(self,paragraph, questionList):
        NORMAL_WORD_SCORE = 1
        UNIQUE_WORD_SCORE = 2
        NO_SENTENCE_FOUND = "No sentence found"
        question_object_array = []
        initialParagraph = paragraph
        paragraph = paragraph.lower()
        sentenceArray = nltk.sent_tokenize(paragraph)

        for q in questionList:
            q = q.lower()
            print(q)
            question_object_array.append(Question(q))
        mcqQuestions = []
        for index, o in enumerate(question_object_array):
            # o.questionType = identify_question_type(str(o.value))
            questionTypeIdentification = QuestionTypeIdentification()
            o.questionType = questionTypeIdentification.identify_question_type(str(o.value))
            if o.questionType[0] != "yes-no" and o.questionType[0] != "dash":
                o.question_start = questionTypeIdentification.identify_question_start(str(o.value))

            o = questionTypeIdentification.identify_singleOrMultipleAnswer(o)
            print(o.answerObject.isSingle)
            print("Identify Type properly ")
            print(o.questionType)
            print(o.question_start)
            sentenceIdentification = SentenceIdentification()
            o, tempQuestion = sentenceIdentification.identify_sentence_regex_approach(o, sentenceArray)

            if o.sentence == NO_SENTENCE_FOUND:
                o.sentence = sentenceIdentification.compareFrequencyDistribution(paragraph, tempQuestion)

            print("-------- IN AutoAnswerGeneration ----------------------")
            print("QUESTION : ", o.value)
            print("SENTENCE : ", o.sentence)
            answerExtraction = AnswerExtraction()
            o = answerExtraction.answer_extraction_from_sentences(o, initialParagraph)
            print("-------- OUT AutoAnswerGeneration ----------------------")
            print("QUESTION : ", o.value)
            print("QUESTION-TYPE : ", o.questionType)
            mcqQuestions.append(o.convertToJson())
            # print("ANSWER-SMALL : ", o.answerObject.smallAnswer)
            # print("ANSWER-MCQ-OPTIONS : ", o.answerObject.mcqAnswer)
            # print("ANSWER-Correct-MCQ : ", o.answerObject.correctAnswer)
            # print("QUESTION_START: ", o.question_start)
        return mcqQuestions