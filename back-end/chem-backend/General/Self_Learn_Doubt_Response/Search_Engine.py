from collections import Counter


def search(searchsentence, word_dictionary):
    try:
        # split sentence into individual words
        searchsentence = searchsentence.lower()
        words = searchsentence
        try:
            words = words.split(' ')
        except:
            words = list(words)
        enddic = {}
        idfdic = {}
        closedic = {}

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
        alloptions = {k: word_dictionary.get(k, None) for k in (words)}
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

        # could make another metric for if they are not next to each other but still close

        return searchsentence, words, fullcount_order, combocount_order, fullidf_order, fdic_order

    except:
        return ""
