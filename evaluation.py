from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import obtimizer
from nltk.corpus import stopwords
import number as num
import numpy as np
def TP_FN (docIdPosetev,docId):
    i=[0,0]
    for id in docIdPosetev:
        if (id in docId):
            i[0]=i[0]+1
        else:
            i[1]=i[1]+1
    return i

def evaluation(docIdPosetev,docId,df):
    confusion_matrix=[[0,0],[0,0]]
    confusion_matrix[0]=TP_FN(docIdPosetev,docId)
    confusion_matrix[1][0] = confusion_matrix[0][1]
    confusion_matrix[1][1] = len(df)-(confusion_matrix[0][0]+confusion_matrix[0][1]+confusion_matrix[1][0]) 
    return confusion_matrix

def PR_RE_FM(confusion_matrix):
    Tp, Fp = confusion_matrix[0][0], confusion_matrix[0][1]
    Fn, Tn = confusion_matrix[1][0], confusion_matrix[1][1]
    pr = round(Tp / (Tp + Fp),3)
    re = round(Tp / (Tp + Fn),3)
    if re==0:
        fm=0
    else:
        fm = round(2 * pr * re / (pr + re),3)
    return [pr,re,fm]

def search_data(reverse_index,query,cleanDf,df,qrel):
    for index in query.index:
        Query=[query["Text"][index]]
        queryId=query['id'][index]
        Query=obtimizer.optmaize(Query[0])
        reslist=[]
        for s in Query:
            if (s in reverse_index):
                reslist.append(list(reverse_index[s]))
        reslist = np.concatenate(reslist, axis=0)
        reslist=list(set(reslist))
        #queryId=num.QuestionAnswer(query,Query)
        docIdPosetev=num.Numberofcorrectanswers(queryId,qrel)
        lendocPosetev=len(docIdPosetev)
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

        dataWillReturn =cosines[:min(lendocPosetev,len(cosines)-1)]
        sent=[]
        for c in dataWillReturn:
            sent.append(docList[c[0]])
        docId=num.Numberofanswerssent(sent,df)
        confusion_matrix=evaluation(docIdPosetev,docId,df)
        matrix=[]
        matrix.append(PR_RE_FM(confusion_matrix))
        i=1
        j=1
        a=0.0
        for d in docId :
            for d2 in  docIdPosetev:
                if d==d2:
                    a=j/i
                j+=1
            i+=1
        ap=a/len(docIdPosetev)
        i=0
        a=0.0
        for d in docId :
            if d in docIdPosetev:
                a+=1/(i+1)
                break
            i+=1
        rr=a
        matrix[len(matrix)-1].append(ap)
        matrix[len(matrix)-1].append(rr)
    return matrix