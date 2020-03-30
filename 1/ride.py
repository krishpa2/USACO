'''
ID: krishpa2
TASK: ride
LANG: PYTHON3
'''

with open('ride.in','r') as fin:
  comet = fin.readline()[:-1]
  group = fin.readline()[:-1]

word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 1
count2 = 1

for words in comet:
  count *= word.index(words)+1
for words in group:
  count2 *= word.index(words)+1

with open('ride.out','w') as fout:
    if (count % 47) == (count2 % 47):
      fout.write('GO\n')
    else:
      fout.write('STAY\n')
