import nltk
import math
from nltk import *
from nltk.corpus import wordnet as wn

def abs_ceil(val):
  if val > 0:
    return math.ceil(val)
  elif val < 0:
    return math.floor(val)
  return 0


afinn_file = open('afinn.txt')

synonym_values = {} 

for l in afinn_file.readlines():
  line_list = l.split()
  if len(line_list) > 1:
    key = ' '.join(line_list[0:-1])
    value = line_list[-1]
    synonym_values[key] = value


def parse_file(f):
  for l in f.readlines():    
    word = l.strip()
    synsets = wn.synsets(word)
    
    if word in synonym_values:
      continue
    
    # get first order synonyms
    synonyms = set()
    for synset in synsets:
      synonyms = set(synonyms) | set(synset.lemma_names)
  
    # add in synonyms of those synonyms
    for syn in synonyms:
      for syn_synset in wn.synsets(syn):
        synonyms = set(synonyms) | set(syn_synset.lemma_names)
    
    synonyms_with_values = set(synonyms) & set(synonym_values.keys())
    
    if not len(synonyms_with_values):
      continue
    
    avg = 0
    total = 0
    for syn in synonyms_with_values:
      value = synonym_values[syn]
      avg = (avg * total + float(value)) / (total + 1)
      total += 1
    
    # print "Adding", word, avg
    synonym_values[word] = int(abs_ceil(avg))
  
  f.close()

parse_file(open('adjectives-parsed.txt'))
parse_file(open('adjectives-parsed.txt'))
parse_file(open('extra-words.txt'))

output = open('sentiments.json', 'w')
output.write('{\n')

for word in synonym_values:
  output.write('  "%s" : %s,\n' % (word, synonym_values[word]))
  
output.write('}')

afinn_file.close()
output.close()