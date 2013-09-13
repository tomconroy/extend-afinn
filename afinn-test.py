afinn = open('afinn.txt')
afinn_list = []

for l in afinn.readlines():
  afinn_list.append(l.strip().split()[0])

print afinn_list