from General.Self_Learn_Doubt_Response.Rank import Rank


class DoubtRespond(object):
    output_value = ""
    search_query = None

    def classify(self, input_query, word_dictionary):
        if input_query == "greeting":
            output_value = "How are you?"
            return output_value
        elif input_query == "goodbye":
            output_value = "Goodbye! Have a nice day"
            return output_value
        if input_query == "thanks":
            output_value = "Hope that was helpful!"
            return output_value
        else:
            ranking = Rank()
            self.search_query = input_query
            rank = ranking.rank(input_query, word_dictionary)
            return rank

    def scraper(self):
        
        return self.search_query
