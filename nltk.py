#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:14:40 2019

@author: agathenaisadiguna
"""

# Goal = clean a file => remove words without meaning, remove special characters, lemmatizing, stemming

import pandas as pd
import string

# for machine learning - classification
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

# for visualisation
import seaborn as sns
import matplotlib.pyplot as plt

# for NLP
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords

filename = '/Users/agathenaisadiguna/Downloads/gensim_documents_shape.txt'
file = open(filename, 'r')
text = file.read()
file.close()


# split into words
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)

# convert to lower case
tokens = [w.lower() for w in tokens]


# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]

# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]

lemma = WordNetLemmatizer()
text = word_tokenize(text)
[lemma.lemmatize(word) for word in text]
[lemma.lemmatize(lemma.lemmatize(lemma.lemmatize(word, pos='a'), pos='v'),pos='n') for word in text]

# filter out stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]

from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in words]

print(stemmed[:1000000])
