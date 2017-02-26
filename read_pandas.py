# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 23:52:57 2017

@author: Sujit
"""
from nltk.tokenize import RegexpTokenizer
import tags
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as pd
train_data = pd.read_table('train_rel_2_demo.tsv',encoding = "ISO-8859-1")
#Score1 = train_data.Score1
#Score2 = train_data.Score2
#EssaySet = train_data.EssaySet
#EssayText = train_data.EssayText
#Id = train_data.Id
train_data = tags.basic_tags(train_data)
print(train_data.head())
#train_data = train_data[["Id", "Score1", "Score2"]]

#train_data = 

#x = len(sent_tokenize("I am cool. How are you? I am good."))


#train_data["Sentences_count"] = [len(sent_tokenize(c)) for c in train_data["EssayText"]]
#train_data["Words_count"] = [len(word_tokenize(c)) for c in train_data["EssayText"]]
#EssayText = list(EssayText)
#print(train_data.tail())
#print(len(word_tokenize("I don't know what is going on!")))
#tokenizer = RegexpTokenizer(r'\w+')
#print(len(tokenizer.tokenize("I don't know what is going on!")))
