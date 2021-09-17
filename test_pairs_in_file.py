#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 23:15:16 2019

@author: agathenaisadiguna
"""

# Goal = from a given list, create words couples, search if these couples are in the same line in a given file. Counter of every words couple

fo = open('file_list_path', 'r') # give a list
wordas = []
for line in fo:
    correction = line.replace('\\\n','')
    correction = correction.replace('\n','')
    wordas.append(correction)

wordas = wordas[1:147]
# to control quantity of words


import re

wordsplit = re.compile('\\W+').split
def matchlines(words):
    counter = 0
    w1,w2 = words
    w1 = w1.lower() # to set w1 in lowercase
    w2 = w2.lower() 
    fh = open('file_path', 'r') # give the file in which the script is going to look in 
    for line in fh:
        words = [x.lower() for x in wordsplit(line)]
        if w1 in line and w2 in line:
            counter +=1
    return counter

import itertools
for pair in itertools.combinations(wordas, 2):
    print(pair) # returns all the possible words pairs

dico = dict() # create a dictionnary
for pair in itertools.combinations(wordas, 2):
    dico[pair] = matchlines(pair)
dico.keys()

from collections import OrderedDict
d_descending = OrderedDict(sorted(dico.items(), 
                                  key = lambda kv : kv[1], reverse = True))

d_descending