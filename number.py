import compare_sentences as compare
def Numberofanswerssent(sent,df):
    docId=[]
    for index in df.index:
        f=str(df["Text"][index])
        if f in sent:
            docId.append(df["doc_id"][index])
    return docId

def Numberofcorrectanswers(quaryId,qrels):
    docIdPosetev=[]
    for index in qrels.index:
        if (qrels["query_id"][index]==quaryId):
            docIdPosetev.append(qrels["doc_id"][index])
    return docIdPosetev

def QuestionAnswer (query,Query):
    queryId=0
    Query=Query.split(" ")
    for index in query.index:
        word=query["Text"][index]
        word=word.split(" ")
        if (compare.compare_sentences(word,Query)==True):
            queryId=query["id"][index]
            break 
    return queryId