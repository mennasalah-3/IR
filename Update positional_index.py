import os
import sys
import pathlib
from pathlib import Path
def tokenization(query):
    stopWords = ['the', 'a', 'an', 'in','of','that','then','is','are','was','were','out']
    tokens = query.split()
    tokensWithoutSW = [word.lower() for word in tokens if not word in stopWords]
    return  tokensWithoutSW
def positionalIndex (tokens):
    positionalindex = dict()
    for pos, term in enumerate(tokens):
        if term in positionalindex:
            positionalindex[term].append(pos + 1)
        else:
            positionalindex[term] = []
            positionalindex[term].append(pos + 1)
    return positionalindex
positions = dict()
inquery = input("Please enter your query: ")
query = tokenization(inquery)

for i in range(1, 11):
    for path in pathlib.Path("D:\CS\IR\IR").iterdir():
      if path.is_file():
        current_file = open(path, "r")
        read_string = current_file.read()
        tokens=tokenization(read_string)
        positionalindex=positionalIndex(tokens)
        for word in query:
            for pos, term in enumerate(positionalindex):
                if term == word:
                    count = len(positionalindex[word])
                    if word in positions:
                        positions[word][0] = positions[word][0] + count
                        positions[word].append([count,"Doc" + str(i), positionalindex[word]])
                    else:
                        positions[word] = []
                        positions[word].append(count)
                        positions[word].append([count,"Doc" + str(i), positionalindex[word]])
 
    
print(positions)