from nltk.corpus import stopwords

from General.Self_Assess_Answer_Generation.HelpingClasses.QuestionScore import QuestionScore

NORMAL_WORD_SCORE = 1
UNIQUE_WORD_SCORE = 2
NO_SENTENCE_FOUND = "No sentence found"
import nltk
import re
from nltk.stem.porter import *
class SentenceIdentification (object) :
    def identify_sentence_regex_approach(self,question, sentenceArray):
        words = question.value.split()
        length = len(words)
        if question.questionType[0] == "wh":
            if words[0] == 'what':
                words[0] = ''
        if words[length - 1] == '?':
            words[length - 1] = ''
        tempQuestion = ''
        for word in words:
            tempQuestion = tempQuestion + word + ' '
        tempQuestion = tempQuestion.strip()
        regExPattern = "." + tempQuestion + "."

        for sentence in sentenceArray:
            # print(sentence)
            if re.search(regExPattern, sentence):
                question.sentence = sentence
                break
            else:
                question.sentence = NO_SENTENCE_FOUND
        return question, tempQuestion

    def compareFrequencyDistribution(self,text, question_rem):
        print("--------START---------------")
        stemmer = PorterStemmer()

        text = text.lower()
        sentenceArray = nltk.sent_tokenize(text)
        returnSentence = ""
        weighted_score = 0
        tempQuestionTokenize = nltk.word_tokenize(question_rem)
        tempQuest_freqDist = nltk.FreqDist(tempQuestionTokenize)
        question_score_object_array = []
        for sentence in sentenceArray:
            weighted_score = 0
            sentence_unique = 0
            quest_match_unique = 0
            for word_quest in tempQuest_freqDist:
                sentence_freqDist = nltk.FreqDist(nltk.word_tokenize(sentence))
                for word_sent in sentence_freqDist:
                    if stemmer.stem(word_quest) == stemmer.stem(word_sent):
                        if word_quest in stopwords.words('english'):
                            print("Without stem : Q : ", word_quest, "S : ", word_sent, " Not unique")
                            print("Stem : Q : ", stemmer.stem(word_quest), "S : ",stemmer.stem(word_sent), " Not unique")
                            weighted_score = weighted_score + NORMAL_WORD_SCORE

                        if word_quest not in stopwords.words('english'):
                            print("Without stem :Q : ", word_quest, "S : ", word_sent, " Unique")
                            print("Stem : Q : ", stemmer.stem(word_quest), "S : ", stemmer.stem(word_sent), " Unique")
                            weighted_score = weighted_score + UNIQUE_WORD_SCORE
                            quest_match_unique = quest_match_unique + 1

            for word_sent in sentence_freqDist:
                if word_sent in stopwords.words('english'):
                    sentence_unique = sentence_unique + 1
            print("C", " : ", weighted_score)
            print("S", " : ", sentence_unique)
            print("Q", " : ", quest_match_unique)
            weighted_score = weighted_score + (weighted_score * (quest_match_unique / sentence_unique))
            if quest_match_unique == 0:
                weighted_score = 0
            score_obj = QuestionScore()
            score_obj.question = question_rem
            score_obj.sentence = sentence
            score_obj.score = weighted_score
            question_score_object_array.append(score_obj)
            print(sentence)
            print("Final Weighted Score : ", weighted_score)
            print("------------SENTENCE FINISHED ------------------------------")
        print("--------END---------------")
        print("")
        check_max_score = 0
        for question_score_object in question_score_object_array:
            if (question_score_object.score > check_max_score):
                check_max_score = question_score_object.score
                returnSentence = question_score_object.sentence
        if check_max_score == 0:
            returnSentence = NO_SENTENCE_FOUND
        return returnSentence