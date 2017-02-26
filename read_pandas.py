# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 23:52:57 2017

@author: Sujit
"""
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as pd
train_data = pd.read_table('train_rel_2_demo.tsv',encoding = "ISO-8859-1")
Score1 = train_data.Score1
Score2 = train_data.Score2
EssaySet = train_data.EssaySet
EssayText = train_data.EssayText
Id = train_data.Id
#train_data = train_data[["Id", "Score1", "Score2"]]
x = len(sent_tokenize("I am cool. How are you? I am good."))

train_data["Sentences_count"] = [len(sent_tokenize(c)) for c in train_data["EssayText"]]
train_data["Words_count"] = [len(word_tokenize(c)) for c in train_data["EssayText"]]
#EssayText = list(EssayText)
print(train_data.head())
#print(len(EssayText))
#print(EssayText[0])
#for i in len(EssayText):
    #print(EssayText)
#    train_data["Sentence_count"] = sent_tokenize(EssayText[i])
#print(len(x))

#print(x)
#print(Id.head())
#print(EssaySet.head())
#print(Score1.head())
#print(Score2.head())

##EssayText[0] = "SUjit"
#print(EssayText[0])
#train_data["SentenceCount"] = 1 
#print(train_data.SentenceCount.head())
#i = 0
#Tokenized_sentence = [[]]
#for essays in EssayText:
#    Tokenized_sentence[i] = sent_tokenize(essays)
#    i = i + 1
#    break
#print(Tokenized_sentence[2])