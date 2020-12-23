import nltk
from nltk.corpus import stopwords
import string
from nltk.tokenize import sent_tokenize,word_tokenize
import tokenize


#Tokenizationfunction

def TokenizationDocs(doc):
    arrOfTokens=[]
    file_content = open(doc).read()
    tokens = nltk.word_tokenize(file_content)
    for token in tokens:
          arrOfTokens.append(token)

    return arrOfTokens



#remove stop Words


def RemoveStopWords(arr):
    stop_words = list(stopwords.words('english'))
    punct=list(string.punctuation)
    punct.append('’')
    StopWords=stop_words + punct
    filtered_list=[]
    lst=list(arr)
    lst = [x.lower() for x in lst] 
    for i in lst:
      if i not in StopWords:
          filtered_list.append(i)

    return filtered_list


#Tokenization
doc1=TokenizationDocs("doc1.txt")
doc2=TokenizationDocs("Doc2.txt")
doc3=TokenizationDocs("Doc3.txt")
doc4=TokenizationDocs("Doc4.txt")
doc5=TokenizationDocs("Doc5.txt")
doc6=TokenizationDocs("Doc6.txt")
doc7=TokenizationDocs("Doc7.txt")
doc8=TokenizationDocs("Doc8.txt")
doc9=TokenizationDocs("Doc9.txt")
doc10=TokenizationDocs("Doc10.txt")

#Stop Words
doc1AfterEdit=RemoveStopWords(doc1)
doc2AfterEdit=RemoveStopWords(doc2)
doc3AfterEdit=RemoveStopWords(doc3)
doc4AfterEdit=RemoveStopWords(doc4)
doc5AfterEdit=RemoveStopWords(doc5)
doc6AfterEdit=RemoveStopWords(doc6)
doc7AfterEdit=RemoveStopWords(doc7)
doc8AfterEdit=RemoveStopWords(doc8)
doc9AfterEdit=RemoveStopWords(doc9)
doc10AfterEdit=RemoveStopWords(doc10)
