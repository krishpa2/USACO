'''
ID: krishpa2
LANG: PYTHON3
TASK: gift1
'''

with open('gift1.in','r') as fin:
    np = int(fin.readline()[:-1])
    ppl = dict()
    for i in range(np):
        ppl[fin.readline()[:-1]] = 0
    for i in range(np):
        giver = fin.readline()[:-1]
        a,n = map(int,fin.readline()[:-1].split())
        if n == 0:
            value = 0
        else:
            value = a//n
        ppl[giver] -= (value) * n
        for j in range(n):
            recip = fin.readline()[:-1]
            ppl[recip] += value
with open('gift1.out','w') as fout:
    for a,b in ppl.items():
        fout.write(str(a) + " " + str(b))
        fout.write('\n')
