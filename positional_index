def positional (tokens):
    pos_index = dict()
    for pos, term in enumerate(tokens):
        if term in pos_index:
            pos_index[term].append(pos + 1)
        else:
            pos_index[term] = []
            pos_index[term].append(pos + 1)
    return pos_index
positions = dict()
inquery = input("Please enter a query:\n")
query = tokenize(inquery)

for term in query:
    positions[term]=list()
for i in range(1, 3):
    with open('C:\\Users\El Noubi\Documents\Python Scripts\\doc%d.txt' % i, 'r', encoding="utf-8") as doc:
        read_string = doc.read()
        tokens=tokenize(read_string)
        pos_index=positional(tokens)
        for word in query:
            for pos, term in enumerate(pos_index):
                if term == word:
                    positions[word].append([i, pos_index[word]])
print(positions)
def docID(plist):
    return plist[0]


def position(plist):
    return plist[1]


def pos_intersect(p1, p2, k):
    answer = []  # answer <- ()
    len1 = len(p1)
    len2 = len(p2)
    i = j = 0
    while i != len1 and j != len2:  # while (p1 != nil and p2 != nil)
        if docID(p1[i]) == docID(p2[j]):
            l = []  # l <- ()
            pp1 = position(p1[i])  # pp1 <- positions(p1)
            pp2 = position(p2[j])  # pp2 <- positions(p2)

            plen1 = len(pp1)
            plen2 = len(pp2)
            ii = jj = 0
            while ii != plen1:  # while (pp1 != nil)
                while jj != plen2:  # while (pp2 != nil)
                    if abs(pp1[ii] - pp2[jj]) <= k:  # if (|pos(pp1) - pos(pp2)| <= k)
                        l.append(pp2[jj])  # l.add(pos(pp2))
                    elif pp2[jj] > pp1[ii]:  # else if (pos(pp2) > pos(pp1))
                        break
                    jj += 1  # pp2 <- next(pp2)
                # l.sort()
                while l != [] and abs(l[0] - pp1[ii]) > k:  # while (l != () and |l(0) - pos(pp1)| > k)
                    l.remove(l[0])  # delete(l[0])
                for ps in l:  # for each ps in l
                    answer.append([docID(p1[i]), pp1[ii], ps])  # add answer(docID(p1), pos(pp1), ps)
                ii += 1  # pp1 <- next(pp1)
            i += 1  # p1 <- next(p1)
            j += 1  # p2 <- next(p2)
        elif docID(p1[i]) < docID(p2[j]):  # else if (docID(p1) < docID(p2))
            i += 1  # p1 <- next(p1)
        else:
            j += 1  # p2 <- next(p2)
    return answer
           i=0
           j=0
           files=list()
           finalresult = list()
            while i < len(query):
            j=i+1
              if j<len(query):
        files.append(pos_intersect(positions[query[i]], positions[query[j]], 1))
             i=j+1

         for fi in files:
            for i in fi:
        finalresult.append(i[0])

     print(set(finalresult))
