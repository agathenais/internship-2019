#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 10:24:56 2019

@author: agathenaisadiguna
"""

# Goal = count words frequency in a file

from collections import Counter
import re # regular expression operation

# define different functions


def open_a_file(filename):
    file = open(filename, "r+")   # "r+" positionnement du pointeur au début du fichier après son ouverture
    contents = file.read()
    file.close()
    return contents

def remove_unnecessary(contents):
    contents = re.sub(r'\W+', ' ', contents)
    return contents

def a_counter(words):
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    return cnt

# main function

def main(filename, topwords):
    txt = open_a_file(filename) # open the file
    txt = remove_unnecessary(txt)   # remove unnecessary characters of the file
    words = txt.split(' ')  # to obtain a list a all the words in the file
    c = a_counter(words)    # to count each word
    for w, value in c.most_common(topwords):
        print (w, value)    # to obtain words and their own counter
        
main(‘file_path’, 100) # number of words displayed