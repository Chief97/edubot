from flask import jsonify

from General.Self_Learn_Doubt_Response.Rank import Rank


class DoubtRespond(object):
    output_value = ""
    search_query = None

    def classify(self, input_query, word_dictionary):
        if input_query == "greeting":
            final_results = {
                "type": "ConversationReply",
                "output_value": "How are you?"
            }
            return jsonify(final_results)
        elif input_query == "How are you?":
            final_results = {
                "type": "ConversationReply",
                "output_value": "I am doing well as always!"
            }
            return jsonify(final_results)
        elif input_query == "goodbye":
            final_results = {
                "type": "ConversationReply",
                "output_value": "Goodbye! Have a nice day"
            }
            return jsonify(final_results)
        elif input_query == "negative greeting response":
            final_results = {
                "type": "ConversationReply",
                "output_value": "Do not worry, everything will be fine. How may I help you today?"
            }
            return jsonify(final_results)
        elif input_query == "thanks":
            final_results = {
                "type": "ConversationReply",
                "output_value": "Hope that was helpful!"
            }
            return jsonify(final_results)
        elif input_query == "positive greeting response":
            final_results = {
                "type": "ConversationReply",
                "output_value": "What can I help you with today?"
            }
            return jsonify(final_results)
        elif input_query == "":
            final_results = {
                "type": "ConversationReply",
                "output_value": "Sorry! that is not in the O/L chemistry Syllabus"
            }
            return jsonify(final_results)
        else:
            ranking = Rank()
            self.search_query = input_query
            rank1 = ranking.rank(input_query, word_dictionary)
            return jsonify(rank1)

    def scraper(self):
        
        return self.search_query
