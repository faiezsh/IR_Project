import pandas as pd 

def invert_dict(d):
    inverted = {}
    itr = 0
    for item in d.values:
        for word in str(item[1]).split():
            if (word not in inverted):
                inverted[word] = set()
            inverted[word].add(itr)
        itr+=1
    return inverted