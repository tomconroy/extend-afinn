import pymongo
from pymongo import MongoClient

import nltk
from nltk import *
from nltk.corpus import wordnet as wn


client = MongoClient()
db = client.mivor
words_collection = db.words


adjectives = open('adjectives-parsed.txt')

output = open('synonyms.json', 'w')
output.write('{\n')


afinn = open('afinn.txt')
afinn_list = []

for l in afinn.readlines():
  afinn_list.append(l.split()[0])

for l in adjectives.readlines():
  word = l.strip()
  synsets = wn.synsets(word)
  
  synonyms = []
  for synset in synsets:
    synonyms = list(set(synonyms) | set(synset.lemma_names))
  
  # synonyms_in_afinn = [word for word in synonyms if word in afinn_list]
  synonyms_in_afinn = list( set(synonyms) & set(afinn_list) )
  
  if len(synonyms_in_afinn):
    output.write('  "%s" : %s,\n' % (word, synonyms_in_afinn))
  
    print word, synonyms_in_afinn


output.write('}')

adjectives.close()
output.close()