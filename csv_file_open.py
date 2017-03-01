# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:08:13 2017

@author: Sujit
"""




import csv
#import math
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk import pos_tag
#from itertools import zip_longest
from pandas import DataFrame




tokenizer = RegexpTokenizer(r'\w+')
stop = set(stopwords.words('english'))



sentence_count = []
word_count = []
word_count_after_removing_stop_words = []
ratio_of_word_and_sentence = []
NN = []
NNP = []
NNS = []
VBZ = []
NNPS = []
IN = []
PRP = []
VB = []
JJ = []
VBP = []
VBJ = []


def main(filename = "train_rel_2.tsv"):
    f = open(filename)
    reader = csv.reader(f, delimiter = '\t')
    header = next(reader)
    for row in reader:
        essaytext = row[4]
        sentence_count.append(len(sent_tokenize(essaytext))) 
        word_count.append(len(tokenizer.tokenize(essaytext)))
        x = [i for i in row[4].lower().split() if i not in stop]
        word_count_after_removing_stop_words.append(len(x))
        ratio_of_word_and_sentence = [x / y for x, y in zip(word_count_after_removing_stop_words, sentence_count)]
        nn = 0
        nnp = 0
        nns = 0
        vbz = 0
        nnps = 0
        in_ = 0
        prp = 0
        jj = 0
        vbp = 0
        vbj = 0
        essay = word_tokenize(essaytext)
        tagged_essay = pos_tag(essay)
        for(tagged_word,tag) in tagged_essay:
            if tag == "NN":
                nn = nn + 1
            elif tag == "NNP":
                nnp = nnp + 1
            elif tag == "NNS":
                nns = nns + 1
            elif tag == "VBZ":
                vbz = vbz + 1
            elif tag == "NNPS":
                nnps = nnps + 1
            elif tag == "IN":
                in_ = in_ + 1
            elif tag == "PRP":
                prp = prp + 1
            elif tag == "JJ":
                jj = jj + 1
            elif tag == "VBP":
                vbp = vbp + 1
            elif tag == "VBJ":
                vbj = vbj + 1
        NN.append(nn)
        NNP.append(nnp)
        NNS.append(nns)
        VBZ.append(vbz)
        NNPS.append(nnps)
        IN.append(in_)
        PRP.append(prp)
        JJ.append(jj)
        VBP.append(vbp)
        VBJ.append(vbj)
                                             
    f.close()
    ratio_of_word_and_sentence = [ int(x) for x in ratio_of_word_and_sentence ]
    
    df = DataFrame({"Word_count": word_count, "Sentence_count": sentence_count, "Word_count_after_removing_stop_words": word_count_after_removing_stop_words,"Ratio_of_words_to_senteces": ratio_of_word_and_sentence,"NN": NN,"NNP": NNP,"NNS": NNS,"NNPS": NNPS,"VBZ": VBZ,"VBP": VBP,"VBJ": VBJ,"JJ": JJ,"PRP": PRP,"IN": IN})
    df.to_excel('test.xlsx', sheet_name='sheet1', index=False)

    
    
    
if __name__=="__main__":
    main()
    
