# coding=UTF-8
from __future__ import division
import nltk.data
import socket  
import random
from tf import *


class SummaryTool(object):


	def split_content_to_sentences(self, content):
		listt = []
		tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	   
		listt = tokenizer.tokenize(content)
		return listt

	# Caculate the intersection between 2 sentences
	def sentences_intersection(self, sent1, sent2, content):

		# split the sentence into words/tokens
		total_score= 0
		s1 = set(sent1.split(" "))
		s2 = set(sent2.split(" "))
		score = 0 
		# If there is not intersection, just return 0
		if (len(s1) + len(s2)) == 0:
			return 0

		common_words = s1.intersection(s2) 

		list_words= list(common_words)
		for words in list_words:
			score = idf(words,content) * tf(words,content)
			total_score += score
			#print score

		# We normalize the result by the average number of words
		return total_score


	def get_sentences_ranks(self, content):

		# Split the content into sentences
		sentences = self.split_content_to_sentences(content)

		# Calculate the intersection of every two sentences
		n = len(sentences)
	   # print n
		values = [[0 for x in xrange(n)] for x in xrange(n)]
		for i in range(0, n):
			for j in range(0, n):
				values[i][j] = self.sentences_intersection(sentences[i], sentences[j],content)
		# Build the sentences dictionary
		# The score of a sentences is the sum of all its intersection
		sentences_dic = {}
		for i in range(0, n):
			score = 0
			for j in range(0, n):
				if i == j:
					continue
				score += values[i][j]
			sentences_dic[sentences[i]] = score
		return sentences_dic


	def readFile(self,filepath):
		f= open(filepath,"r")
		return f.read()
		 

def main():


	st = SummaryTool()

	

   # print content
	complete_summary = [] 

	para_summary = [] 

	content = "Thomas A. Anderson is a man living two lives. By day he is an " + \
    "average computer programmer and by night a hacker known as " + \
    "Neo. Neo has always questioned his reality, but the truth is " + \
    "far beyond his imagination. Neo finds himself targeted by the " + \
    "police when he is contacted by Morpheus, a legendary computer " + \
    "hacker branded a terrorist by the government. Morpheus awakens " + \
    "Neo to the real world, a ravaged wasteland where most of " + \
    "humanity have been captured by a race of machines that live " + \
    "off of the humans' body heat and electrochemical energy and " + \
    "who imprison their minds within an artificial reality known as " + \
    "the Matrix. As a rebel against the machines, Neo must return to " + \
    "the Matrix and confront the agents: super-powerful computer " + \
    "programs devoted to snuffing out Neo and the entire human " + \
    "rebellion. "

	sentences_dic = st.get_sentences_ranks(content)
	dict_to_tuple = list(sentences_dic.items())
	sorted_by_second = sorted(dict_to_tuple, key=lambda tup: tup[1], reverse=True)
	print sorted_by_second[0] + "\n" + sorted_by_second[1]

if __name__ == '__main__':
	main()
