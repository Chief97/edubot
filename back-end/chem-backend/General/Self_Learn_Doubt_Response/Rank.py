import json
from collections import Counter

from flask import jsonify

from General.Self_Learn_Doubt_Response.DataLoading import DataLoading


class read_data(object):
    def __init__(self, jdata):
        self.__dict__ = json.loads(jdata)


class Rank(object):

    def rank(self, term, word_dictionary):
        # search_engine = SearchEngine()
        # results = search_engine.search(term, word_dictionary)

        # calculate the relevant metrics
        try:
            # split sentence into individual words
            searchsentence = term.lower()
            words = searchsentence
            try:
                words = words.split(' ')
            except:
                words = list(words)
            enddic = {}
            idfdic = {}

            # remove words if not in worddic
            realwords = []
            for word in words:
                if word in list(word_dictionary.keys()):
                    realwords.append(word)
            words = realwords
            numwords = len(words)

            # make metric of number of occurances of all words in each doc & largest total IDF
            for word in words:
                for indpos in word_dictionary[word]:
                    index = indpos[0]
                    amount = len(indpos[1])
                    idfscore = indpos[2]
                    enddic[index] = amount
                    idfdic[index] = idfscore
                    fullcount_order = sorted(enddic.items(), key=lambda x: x[1], reverse=True)
                    fullidf_order = sorted(idfdic.items(), key=lambda x: x[1], reverse=True)


            # make metric of what percentage of words appear in each doc
            combo = []
            alloptions = {k: word_dictionary.get(k, None) for k in words}
            for worddex in list(alloptions.values()):
                for indexpos in worddex:
                    for indexz in indexpos:
                        combo.append(indexz)
            comboindex = combo[::3]
            combocount = Counter(comboindex)
            for key in combocount:
                combocount[key] = combocount[key] / numwords
            combocount_order = sorted(combocount.items(), key=lambda x: x[1], reverse=True)


            # make metric for if words appear in same order as in search
            if len(words) > 1:
                x = []
                y = []
                for record in [word_dictionary[z] for z in words]:
                    for index in record:
                        x.append(index[0])
                for i in x:
                    if x.count(i) > 1:
                        y.append(i)
                y = list(set(y))

                closedic = {}
                for wordbig in [word_dictionary[x] for x in words]:
                    for record in wordbig:
                        if record[0] in y:
                            index = record[0]
                            positions = record[1]
                            try:
                                closedic[index].append(positions)
                            except:
                                closedic[index] = []
                                closedic[index].append(positions)

                x = 0
                fdic = {}
                for index in y:
                    csum = []
                    for seqlist in closedic[index]:
                        while x > 0:
                            secondlist = seqlist
                            x = 0
                            sol = [1 for i in firstlist if i + 1 in secondlist]
                            csum.append(sol)
                            fsum = [item for sublist in csum for item in sublist]
                            fsum = sum(fsum)
                            fdic[index] = fsum
                            fdic_order = sorted(fdic.items(), key=lambda x: x[1], reverse=True)
                        while x == 0:
                            firstlist = seqlist
                            x = x + 1
            else:
                fdic_order = 0

            # get metrics1
            num_score = fullcount_order
            per_score = combocount_order
            tfscore = fullidf_order
            order_score = fdic_order

            final_candidates = []

            # rule1: if high word order score & 100% percentage terms then put at top position
            try:
                first_candidates = []

                for candidates in order_score:
                    if candidates[1] > 1:
                        first_candidates.append(candidates[0])

                second_candidates = []

                for match_candidates in per_score:
                    if match_candidates[1] == 1:
                        second_candidates.append(match_candidates[0])
                    if match_candidates[1] == 1 and match_candidates[0] in first_candidates:
                        final_candidates.append(match_candidates[0])

                # rule2: next add other word order score which are greater than 1

                t3_order = first_candidates[0:3]
                for each in t3_order:
                    if each not in final_candidates:
                        final_candidates.insert(len(final_candidates), each)

                # rule3: next add top td-idf results
                final_candidates.insert(len(final_candidates), tfscore[0][0])
                final_candidates.insert(len(final_candidates), tfscore[1][0])

                # rule4: next add other high percentage score
                t3_per = second_candidates[0:3]
                for each in t3_per:
                    if each not in final_candidates:
                        final_candidates.insert(len(final_candidates), each)

                # rule5: next add any other top results for metrics
                othertops = [num_score[0][0], per_score[0][0], tfscore[0][0], order_score[0][0]]
                for top in othertops:
                    if top not in final_candidates:
                        final_candidates.insert(len(final_candidates), top)

            # unless single term searched, in which case just return
            except:
                othertops = [num_score[0][0], per_score[0][0], tfscore[0][0]]
                for top in othertops:
                    if top not in final_candidates:
                        final_candidates.insert(len(final_candidates), top)

            # return the most appropriate document
            load_data = DataLoading()
            data = load_data.load_file()
            final_results = {
                "name": data.iloc[final_candidates[0]]['name'],
                "html_text": data.iloc[final_candidates[0]]['html_text']
            }

            return jsonify(final_results)

        except:
            error_msg = "error"
            return error_msg

