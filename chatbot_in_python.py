# -*- coding: utf-8 -*-
"""Chatbot in Python

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12dKlekdDtmYNNBt3_-kxJytA1lCzLkqT
"""

import numpy as np
import nltk
import string
import random

f=open('chatbot.txt','r',errors = 'ignore')
raw_doc=f.read()
raw_doc=raw_doc.lower()# convert text to lower case
nltk.download('punkt') # using the Punkt tokenizer
nltk.download('wordnet')# using wordnet dictionary
sent_tokens = nltk.sent_tokenize(raw_doc) # convert doc to list of sentences
word_tokens = nltk.word_tokenize(raw_doc) #convert doc to list of words

sent_tokens[:2]

word_tokens[:2]

lemmer =nltk.stem.WordNetLemmatizer
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

Greet_input=("hello","hi","greetings","sup","what's up","hey")
Greet_responses=['hi','hey','hi there','hello','I am glad! You are talking to me']
def greet(sentence):
    for word in sentence.split():
        if word.lower() in Greet_input:
            return random.choice(Greet_responses)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def respose(user_response):
  robo1_response=''
  TfidfVec=TfidfVectorizer(tokenizer=LemNormalize,stop_words='english')
  tfidf=TfidfVec.fit_transform(sent_tokens)
  vals=cosine_similarity(tfidf[-1],tfidf)
  idx=vals.argsort()[0][-2]
  float=vals.flatten()
  float.sort()
  req_tfidf=float[-2]
  if(req_tfidf==0):
    robo1_response=robo1_response+"I am sorry! I don't understand you"
    return robo1_response
  else:
    robo1_response=robo1_response+sent_tokens[idx]
    return robo1_response

import nltk
from nltk.stem import WordNetLemmatizer

lemmer =nltk.stem. WordNetLemmatizer # Instantiate the lemmatizer

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    # Tokenize the text before lemmatizing
    tokens = nltk.word_tokenize(text.lower().translate(remove_punct_dict))
    return LemTokens(tokens)

flag=True
print('BOT: My name is Zain. Lets have a conversation , also if you wanna exit just type Bye Bye')
while flag==True:
  user_response=input()
  user_response=user_response.lower()
  if(user_response!='bye'):
    if(user_response=='thanks' or user_response=='thank you'):
      flag=False
      print('BOT: You are welcome')
    else:
      if(greet(user_response)!=None):
        print('BOT: '+greet(user_response))
      else:
        sent_tokens.append(user_response)
        word_tokens=word_tokens+nltk.word_tokenize(user_response)
        final_words=list(set(word_tokens))
        print('BOT: ',end='')
        print(respose(user_response))
        sent_tokens.remove(user_response)
  else:
    flag=False
    print('BOT: Goodbye! Take care <3')