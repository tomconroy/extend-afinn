import pymongo
from pymongo import MongoClient

import nltk
from nltk import *
from nltk.corpus import wordnet as wn


client = MongoClient()
db = client.mivor
words_collection = db.words


adjectives = open('common-adjectives-parsed.txt')

output = open('common-synonyms.json', 'w')
output.write('{\n')


for l in adjectives.readlines():
  word = l.strip()
  synsets = wn.synsets(word)
  
  synonyms = []
  for synset in synsets:
    synonyms = list(set(synonyms) | set(synset.lemma_names))
  
  output.write('  "%s" : %s,\n' % (word, synonyms))
  
  print word, synonyms


output.write('}')

adjectives.close()
output.close()