'''
ID: krishpa2
TASK: milk2
LANG: PYTHON3
'''


with open('milk2.in','r') as fin:
    n = int(fin.readline())
    res = []
    for i in range(n):
        a,b = map(int,fin.readline().split())
        res.append([a,b])
mini = min([i[0] for i in res])
maxi = max([i[1] for i in res])
MAX = [0] * (maxi)
for i in res:
    a,b = i
    for j in range(a,b):
        MAX[j] = 1
MAX = MAX[mini:]
s = ''.join(map(str,MAX))
b = len(max(s.split("0"),key = len))
c = len(max(s.split("1"),key = len))
with open('milk2.out','w') as fout:
    res = str(b) + " " + str(c)
    fout.write(res)
    fout.write('\n')



