import json
from collections import Counter

from flask import jsonify

from General.Self_Learn_Doubt_Response.DataLoading import DataLoading
from General.Self_Learn_Doubt_Response.Search_Engine import SearchEngine


class read_data(object):
    def __init__(self, jdata):
        self.__dict__ = json.loads(jdata)


class Rank(object):

    def rank(self, term, word_dictionary):
        search_engine1 = SearchEngine()
        print("term")
        print(term)
        results = search_engine1.search(term, word_dictionary)
        print(results)

        # get metrics
        num_score = results[2]
        per_score = results[3]
        tfscore = results[4]
        order_score = results[5]

        final_candidates = []

        try:
            # rule1: if high word order score & 100% percentage terms then put at top position
            try:
                first_candidates = []

                for candidates in order_score:
                    if candidates[1] > 1:
                        first_candidates.append(candidates[0])

                print("first candidates")
                print(first_candidates[0])
                second_candidates = []

                for match_candidates in per_score:
                    if match_candidates[1] == 1:
                        second_candidates.append(match_candidates[0])
                    if match_candidates[1] == 1 and match_candidates[0] in first_candidates:
                        final_candidates.append(match_candidates[0])

                print("second candidates")
                print(second_candidates[0])
                print("final candidates 1")
                print(final_candidates[0])
                # rule2: next add other word order score which are greater than 1

                t3_order = first_candidates[0:3]
                for each in t3_order:
                    if each not in final_candidates:
                        final_candidates.insert(len(final_candidates), each)

                # rule3: next add top td-idf results
                final_candidates.insert(len(final_candidates), tfscore[0][0])
                final_candidates.insert(len(final_candidates), tfscore[1][0])

                print("final candidates 2")
                print(final_candidates[0])

                # rule4: next add other high percentage score
                t3_per = second_candidates[0:3]
                for each in t3_per:
                    if each not in final_candidates:
                        final_candidates.insert(len(final_candidates), each)

                print("final candidates 3")
                print(final_candidates[0])
                # rule5: next add any other top results for metrics
                othertops = [num_score[0][0], per_score[0][0], tfscore[0][0], order_score[0][0]]
                for top in othertops:
                    if top not in final_candidates:
                        final_candidates.insert(len(final_candidates), top)

                print("final candidates 4")
                print(final_candidates[0])

            # unless single term searched, in which case just return
            except:
                othertops = [num_score[0][0], per_score[0][0], tfscore[0][0]]
                for top in othertops:
                    if top not in final_candidates:
                        final_candidates.insert(len(final_candidates), top)

                print("final candidates 5")
                print(final_candidates[0])

                # return the most appropriate document
                load_data = DataLoading()
                data = load_data.load_file()
                final_results = {
                    "type": "textContent",
                    "name": data.iloc[final_candidates[0]]['name'],
                    "html_text": data.iloc[final_candidates[0]]['html_text']
                }
                print("final candidates 6")
                print(final_candidates[0])
                print(final_results)
                return jsonify(final_results)
        except:
            print("error")
            results3 = {
                "type": "error",
                "output_value": "not available"
            }
            return jsonify(results3)
