import os
import re
import sys
import nltk
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
files = os.listdir("/home/saurabh/TDMatrix/txtFiles")
tokens = []
stop_words = nltk.corpus.stopwords.words('english')
tdMat = defaultdict(list)
ps = PorterStemmer()
regex = re.compile('[^a-zA-Z]')
wordTokens = defaultdict(list)
vocab = []
i = 0
def unique_tokens(words_list):
	ulist = []
	[ulist.append(x) for x in words_list if x not in ulist]
	return ulist
for f in files:
	fileReader = open('/home/saurabh/TDMatrix/txtFiles/'+f,'r').read()
	cToken = word_tokenize(fileReader)
	for w in cToken:
		if w.isalpha():
			if w not in stop_words:
				wi = ps.stem(w)
				wordTokens[i].append(wi)
				vocab.append(wi)
	wordTokens[i] = unique_tokens(wordTokens[i])
	i = i + 1
vocab = unique_tokens(vocab)
print "Term Document matrix is: \n"
for term in vocab:
	for k in range(0,len(wordTokens.keys())):
		if term in wordTokens[k]:
			tdMat[term].append(1)
		else:
			tdMat[term].append(0)
for k in tdMat.keys():
	print k,
	print tdMat[k]