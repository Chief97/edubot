import json
from collections import Counter
import numpy as np
from flask import jsonify


class SearchEngine(object):
    def search(self, searchsent, word_dictionary):
        """need to load word_dictionary"""
        print("word dictionary")
        print(word_dictionary)
        print("search sentence")
        print(searchsent)

        results1 = list()
        results1.append(searchsent)
        print('search sentence 1')
        print(results1[0])
        try:
            # split sentence into individual words
            searchsentence = searchsent.lower()
            words = searchsentence
            try:
                words = words.split(' ')
            except:
                words = list(words)
            enddic = {}
            idfdic = {}
            results1.append(words)

            print('search words')
            print(results1[1])

            # remove words if not in worddic
            realwords = []
            for word in words:
                if word in list(word_dictionary.keys()):
                    realwords.append(word)
            words = realwords
            numwords = len(words)
            print('real search words')
            print(words)

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

            # also the one above should be given a big boost if ALL found together

            print("Results")
            print("search sentence")
            print(searchsentence)
            print("search words")
            print(words)
            print("fullcount order")
            print(fullcount_order)
            print("combocount_order")
            print(combocount_order)
            print("fullidf order")
            print(fullidf_order)
            print("fdic order")
            print(fdic_order)
            results1.append(fullcount_order)
            results1.append(combocount_order)
            results1.append(fullidf_order)
            results1.append(fdic_order)

            return results1
        except:
            return "empty"
