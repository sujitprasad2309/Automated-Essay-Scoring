# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:17:26 2017

@author: Sujit
"""

from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize
#import pandas as pd

def basic_tags(train_data):
    tokenizer = RegexpTokenizer(r'\w+')
    train_data["Sentences_count"] = [len(sent_tokenize(c)) for c in train_data["EssayText"]]
    train_data["Words_count"] = [len(tokenizer.tokenize(c)) for c in train_data["EssayText"]]
    return train_data