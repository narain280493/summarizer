# coding=UTF-8
from __future__ import division
import re
import math
from operator import itemgetter

## Code adapted from http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/ 

def sentenceCount(content):
  return content.split('.')

def idf(word, content):
	sentences = sentenceCount(content)
	number_of_sentences = len(sentences)
	count=0
	for sentence in sentences:
		if sentence.count(word) > 0:
		  count += 1
	
	return math.log(number_of_sentences/(1+count))

def wordCount(content):
  return len(content.split(None))

def freq(word, content):
  return content.count(word)

def tf(word, content):
  return (freq(word,content) / float(wordCount(content)))

