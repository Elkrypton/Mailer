# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 23:27:17 2022

@author: Mr Robot
"""



import nltk
import nltk.sentiment.util 
import nltk.sentiment.sentiment_analyzer
from  nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentAnalyzer():
    
    def __init__(self,email_data):
        self.email_data = email_data

    def AdvancedAnalyzer(self):
        data = self.email_data
        #data = word.getTextWord(FileName).split('.')
        tokens = nltk.sent_tokenize(data)
        senti = SentimentIntensityAnalyzer()
        print("------- Built-in Sentiment Analyzer ---------")
        for msg in tokens:
            print('>> {}'.format(msg),'\n --->')
            kvp = senti.polarity_scores(msg)
            for k in kvp:
                print("[+] {} -- {}".format(k, kvp[k]),'\n')
            print()

