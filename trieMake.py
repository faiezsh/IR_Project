import pandas as pd
import nltk
import trie
class TrieMaker:
    def __init__(self) :
        self.myTrie =trie.PrefixTree()

    def buildTre(self,name):
        name=name+".xlsx"
        df = pd.read_excel(name)
        first=True
        ids=[]
        for index in df:
            df[index].dropna(inplace=True)
            df[index] = df[index].astype(str)
            sentence=df[index]
            if first:
                ids=sentence
                first=False
            else:
                i=0
                for s in sentence:
                    words = nltk.word_tokenize(s)
                    for word in words:
                       self.myTrie.insert(word,ids[i])
                    i+=1

    def serch_word(self,word):
        return self.myTrie.starts_with(word)