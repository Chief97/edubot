import unittest

from General.Self_Assess_Question_Generation.QuestionFormation import QuestionFormation


class TestQuestionGeneration(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_yes_questions(self):
        questionGeneration = QuestionFormation()
        # Expected Value
        expectedResult = "Can the things in our environment  be classified into two categories as matter and energy?"

        # Actual Value
        actualResult = questionGeneration.createYesUsingHVerbPhrase(
            'The things in our environment can be classified into two categories as matter and energy')

        # Assert
        self.assertEqual(actualResult, expectedResult)

    def test_negative_yes_questions(self):
        questionGeneration = QuestionFormation()
        # Expected Value
        expectedResult = ""

        # Actual Value
        actualResult = questionGeneration.createYesUsingHVerbPhrase(
            'Manganese dioxide has increased the rate of this reaction')

        # Assert
        self.assertEqual(actualResult, expectedResult)

    def test_WH_questions(self):
        questionGeneration = QuestionFormation()
        # Expected Value
        expectedResult = "What are called matter?"

        # Actual Value
        actualResult = questionGeneration.generateWHQuestion(
            'Things that occupy space and have mass are called matter')

        # Assert
        self.assertEqual(actualResult, expectedResult)

    def test_negative_WH_questions(self):
        questionGeneration = QuestionFormation()
        # Expected Value
        expectedResult = ""

        # Actual Value
        actualResult = questionGeneration.generateWHQuestion(
            'According to the chemical composition, the matter can be divided as Pure substances and mixtures')

        # Assert
        self.assertEqual(actualResult, expectedResult)

    def test_fill_in_blanks_questions(self):
        questionGeneration = QuestionFormation()
        # Expected Value
        expectedResult = "Things that occupy space and have mass are called  @dash "

        # Actual Value
        actualResult = questionGeneration.fillInBlanks(
            'Things that occupy space and have mass are called matter')

        # Assert
        self.assertEqual(actualResult, expectedResult)

    def test_how_questions(self):
        questionGeneration = QuestionFormation()
        # Expected Value
        expectedResult = "How can pure substances  be divided?"

        # Actual Value
        actualResult = questionGeneration.generateHowQuestion(
            'Pure substances can be divided as elements and compounds')

        # Assert
        self.assertEqual(actualResult, expectedResult)

    def test_negative_how_questions(self):
        questionGeneration = QuestionFormation()
        # Expected Value
        expectedResult = None

        # Actual Value
        actualResult = questionGeneration.generateHowQuestion(
            'Things that occupy space and have mass are called matter')

        # Assert
        self.assertEqual(actualResult, expectedResult)


if __name__ == '__main__':
    unittest.main()
