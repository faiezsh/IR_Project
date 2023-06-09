# IR_Project
the constracter of the project:


antique_docs.xlsx : antique/test docs
antique_qrels.xlsx : antique/test qrels
antique_que.xlsx : antique/test query
newDoc.xlsx : clean antique/test docs
newqury.xlsx : clean antique/test query


antique_train_docs.xlsx : antique/train docs
antique_train_qrels.xlsx : antique/train qrels
antique_train_que.xlsx : antique/train query
newTrainDoc.xlsx : clean antique/train docs
newTrainqury.xlsx : clean antique/train query

py files:

1- compare_sentences: python module tht have two functions:
	1) compare_sentences: take two string arrays arguments return if they have same value or not
	2) compare: take two string arguments return if they have same value or not after split them

2- evaluation: python module tht have four functions:
	1) TP_FN: return 1X2 array that contain number of true positive and false negative
	2) evaluation: return 2X2 array that is confusion matrix
	3) PR_RE_FM: return 1X3 array that is the precison and recall and F1 value
	4) search_data: return the accuracy of each query resault

3- inverted_Index: python module tht have one function:
	1) invert_dict: return inverted index of the document

4- number: python module tht have three functions:
	1) Numberofanswerssent: return doc_ids of correct answers
	2) Numberofcorrectanswers: return number of correct answer after search
	3) QuestionAnswer: return query id of the string we search for or 0 if its not found

5- obtimizer: python module tht have six functions:
	1) split: return array of words to a sentence
	2) tage: return tuble array of word and its tags
	3) wordTags: lemmatizer the words
	4) without_prepositions: return one string from string array
	5) inverted_index: return inverted index for a document
	6) optmaize: return a clean string of the string you want to clean it

6- stringSearch: python module tht have one function:
	1) search_data: return array of strings that is the values of query search

7- trie: data structure that containe all words in document we use it to suggest the rest of inputed words

8- trieMaker: helper class that take the ducument to make the trie data structure

ipynb files:

1- apiRequest: its use is to send requests and show the resualt

2- apis: its the flask server that recieve apis

3- database: download the dataset and save it in excel file

4- dataCleaner: clean data and restore them in another excel file

5- search: calculate the accuracy of train dataset

6- testSearch: calculate the accuracy of test dataset

