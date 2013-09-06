adjs = open('adjectives.txt')
output = open('adjectives-parsed.txt', 'w')

for line in adjs.readlines():
  word = line.split(' ')[0]
  if word:
    output.write(word + '\n')

adjs.close()
output.close()