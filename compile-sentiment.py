import nltk
from nltk import *
from nltk.corpus import wordnet as wn


adjectives = open('adjectives-parsed.txt')

# output = open('sentiments.json', 'w')
# output.write('{\n')


afinn_file = open('afinn.txt')
afinn = {} 

for l in afinn_file.readlines():
  line_list = l.split()
  key = ' '.join(line_list[0:-1])
  value = line_list[-1]
  
  afinn[key] = value


synonymValues = {}

for l in adjectives.readlines():
  word = l.strip()
  synsets = wn.synsets(word)
  
  synonyms = set()
  for synset in synsets:
    synonyms = set(synonyms) | set(synset.lemma_names)
  
  synonyms_in_afinn = set(synonyms) & set(afinn.keys())
  
  if not len(synonyms_in_afinn):
    continue
  
  avg = 0
  total = 0
  for syn in synonyms_in_afinn:
    value = int(afinn[syn])
    avg = (avg * total + value) / (total + 1)
    total += 1
  
  synonymValues[word] = avg
    
    
    # -  window.synonymValues = {}
    # -  for word of synonymList
    # -    synonyms = window.synonymList[word]
    # -    i = 0
    # -    total = 0
    # -    avg = 0
    # -    while i < synonyms.length
    # -      if val = window.afinnList[synonyms[i]]
    # -        avg = (avg * total + val) / (total + 1)
    # -        total++
    # -      i++
    # -    window.synonymValues[word] = Math.round(avg)
  
print synonymValues

# output.write('}')

adjectives.close()
afinn_file.close()
#output.close()