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
for term in vocab:
	for k in range(0,len(wordTokens.keys())):
		if term in wordTokens[k]:
			tdMat[term].append(1)
		else:
			tdMat[term].append(0)
print "Enter your query"
query = raw_input()
query_token = word_tokenize(query.lower())
print query_token
aon_list = []
terms_list = []
for q in query_token:
	if q == 'and':
		aon_list.append(q)
	elif q == 'or':
		aon_list.append(q)
	elif q == 'not':
		aon_list.append(q)
	else:
		terms_list.append(q)
print terms_list
print aon_list
final = 0
j = len(terms_list)
print j
while len(aon_list) != 0:
	operator = aon_list.pop()
	if len(terms_list) == j:
		if terms_list[len(terms_list)-1] in vocab:
			final = convertToInt(tdMat[terms_list.pop()])
			if operator == 'not':
				final = ~final
		else:
			if aon_list[len(aon_list)-1] == 
	if operator == 'and':
		num1 = int(''.join(str(t) for t in tdMat[ps.stem(terms_list.pop())]),2)
		if aon_list[len(aon_list)-1] == 'not':
			final = final & ~num1
			aon_list.pop()
		else:
			final = final & num1
	if operator == 'or':
		num1 = int(''.join(str(t) for t in tdMat[ps.stem(terms_list.pop())]),2)
		if aon_list[len(aon_list)-1] == 'not':
			final = final | ~num1
			aon_list.pop()
		else:
			final = final | num1
retrievedFiles = []
binaryList = []
l = 4
while l > 0:
	binaryList.append(final%2)
	final = final/2
	l = l-1
binaryList = binaryList.reverse()
print binaryList
k = 0
for b in binaryList:
	if b == 1:
		retrievedFiles.append('file'+str(k))
		k = k + 1
	else:
		k = k + 1
print retrievedFiles
def convertToInt(listOfBinary):
	return int(''.join(str(t) for t in listOfBinary),2)