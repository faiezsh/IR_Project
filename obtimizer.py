import nltk
from nltk.stem import WordNetLemmatizer
from collections import defaultdict

 
def split(sentence):
    sentence = sentence.lower()
    words = nltk.word_tokenize(sentence)
    return words

def tage(words):
    tags = nltk.pos_tag(words) 
    return tags

def wordTags(tags):
    
    lemmatizer = WordNetLemmatizer()
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    notTags=["SYM","PRP$","CC","PRP","TO","IN","DT","EX","FW","MD","PDT","POS","RP","UH","WDT","WP","WP$","WRB","$","(",")",",","--",".",":"]
    adv=["JJR","JJS"]
    verb=["VB","VBD","VBG","VBN","VBP","VBZ"]
    adverb=["RB","RBR","RBS"]
    nouns=["NN","NNP","NNPS","NNS"]
    exact=False
    last=[]
    for word, tag in tags:
        if word in punctuation:
            word= word.replace(word, " ")
        elif tag=="``":
            if exact:
                exact=False
            else:
                exact=True
            last.append(word)
        elif exact:
            last.append(word)
        elif tag in adv:
            last.append(lemmatizer.lemmatize(word, pos="a"))
        elif tag in verb:
            last.append(lemmatizer.lemmatize(word, pos="v"))
        elif tag in adverb:
            last.append(lemmatizer.lemmatize(word, pos="r"))
        elif tag in nouns:
            last.append(lemmatizer.lemmatize(word, pos="n"))
        elif tag not in notTags:
            last.append(lemmatizer.lemmatize(word, pos="s"))
    return (last)

def without_prepositions(last):
    sentence_without_prepositions = " ".join(last)
    return (sentence_without_prepositions) 


def optmaize(word):
    words=split(word)
    tags=tage(words)
    list=wordTags(tags)
    return list