import math
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas

def TF (numofwords ,bagofwords):
    TFDict = {}
    Length = len(bagofwords)
    for key , value in numofwords.items():
        TFDict[key] = value/Length
    return TFDict

def IDF (documents):
    import math
    no_of_documents = len(documents)
    IDFDict = dict.fromkeys(documents[1].keys(),0)
    for document in documents:
        for key , value in document.items():
            if value > 0:
                IDFDict[key] +=1
    for key , value in IDFDict.items():
        IDFDict[key] = math.log10(no_of_documents/value)
    return IDFDict
IDF1 =IDF([numofwordsofdoc1 , numofwordsofdoc2])

def TF_IDF (TFDict , IDFDict):
    TF_IDFDict = {}
    for key , value in IDFDict.items():
        TF_IDFDict[key] = TFDict[key] * value
    return TF_IDFDict

def Normalize (TF_IDFDict):
    Length = 0
    NormalizeDict = {}
    for key  in TF_IDFDict:
        Length += math.pow(TF_IDFDict[key],2)
    Length =math.sqrt(Length)
    for key in TF_IDFDict:
        NormalizeDict[key] = TF_IDFDict[key]/Length
    return NormalizeDict
def Similarity (NormalizeQuery , NormalizeDoc):
    similarity = NormalizeQuery + NormalizeDoc
    return similarity

#TFQuery = TF(QueryDict , QueryList)
#TFQueryDoc = TF(QueryDocDict , QueryDocList)

#IDFQuery = IDF(QueryDict)
#IDFQueryDoc = IDF(QueryDocDict)

#TF_IDFQuery = TF_IDF(TFQuery , IDFQuery)
#TF_IDFQueryDoc = TF_IDF(TFQueryDoc , IDFQueryDoc)

#NormalizeQuery = Normalize ( TF_IDFQuery)

#NormalizeQueryDoc = Normalize ( TF_IDFQueryDoc)

#Similarity(NormalizeQuery , NormalizeQueryDoc)
