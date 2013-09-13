import nltk
from nltk import *
from nltk.corpus import wordnet as wn


adjectives = open('adjectives-parsed.txt')
#adjectives = open('adj-test.txt')




afinn_file = open('afinn.txt')
afinn = {} 

for l in afinn_file.readlines():
  line_list = l.split()
  key = ' '.join(line_list[0:-1])
  value = line_list[-1]
  
  afinn[key] = value


synonym_values = {}

for l in adjectives.readlines():
  word = l.strip()
  synsets = wn.synsets(word)
  
  # get first order synonyms
  synonyms = set()
  for synset in synsets:
    synonyms = set(synonyms) | set(synset.lemma_names)
  
  # add in synonyms of those synonyms
  for syn in synonyms:
    for syn_synset in wn.synsets(syn):
      synonyms = set(synonyms) | set(syn_synset.lemma_names)
  
  synonyms_in_afinn = set(synonyms) & set(afinn.keys())
  
  if not len(synonyms_in_afinn):
    continue
  
  avg = 0
  total = 0
  for syn in synonyms_in_afinn:
    value = float(afinn[syn])
    avg = (avg * total + value) / (total + 1)
    total += 1
  
  synonym_values[word] = int(avg)


all_synonyms = dict( synonym_values.items() + afinn.items() )

output = open('sentiments.json', 'w')
output.write('{\n')

for word in all_synonyms:
  output.write('  "%s" : %s,\n' % (word, all_synonyms[word]))
  
output.write('}')

adjectives.close()
afinn_file.close()
#output.close()