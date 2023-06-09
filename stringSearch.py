from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import obtimizer
from nltk.corpus import stopwords
import numpy as np


def search_data(reverse_index,cleanDf,df,Query):
    Query=obtimizer.optmaize(Query[0])
    reslist=[]
    for s in Query:
        if (s in reverse_index):
            reslist.append(list(reverse_index[s]))
    reslist = np.concatenate(reslist, axis=0)
    reslist=list(set(reslist))
    #queryId=num.QuestionAnswer(query,Query)
    train_set=[]
    docList=[]
    for i in reslist:
        train_set.append(cleanDf['Text'][i])
        docList.append (df['Text'][i])
    stopWords = stopwords.words('english')

    vectorizer = TfidfVectorizer(stop_words=stopWords)

    trainVectorizerArray = vectorizer.fit_transform(train_set)
    testVectorizerArray = vectorizer.transform([obtimizer.without_prepositions(Query)])

    cosines = cosine_similarity(testVectorizerArray, trainVectorizerArray)[0]
    enucm_cosines = list(enumerate(cosines))


    cosines = sorted(enucm_cosines, key=lambda x: x[1], reverse=True)

    dataWillReturn =cosines[:10]
    sent=[]
    for c in dataWillReturn:
        sent.append(docList[c[0]])
    return sent