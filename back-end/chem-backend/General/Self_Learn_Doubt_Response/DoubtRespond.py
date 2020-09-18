from General.Self_Learn_Doubt_Response.Rank import Rank


class DoubtRespond(object):
    output_value = ""

    def classify(self, input_query, word_dictionary):
        if input_query == "greeting":
            output_value = "How are you?"
            return output_value
        elif input_query == "goodbye":
            output_value = "Goodbye! Have a nice day"
            return output_value
        if input_query == "thanks":
            output_value = "Hope that was helpful!"
            return
        else:
            ranking = Rank()
            rank = ranking.rank(input_query, word_dictionary)
            return rank
