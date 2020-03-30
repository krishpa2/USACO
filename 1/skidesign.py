'''
ID: krishpa2
TASK: skidesign
LANG: PYTHON3
'''

with open('skidesign.in','r') as fin:
    n = int(fin.readline())
    hills = [int(fin.readline()) for i in range(n)]
    
cost = 10**8

for i in range(0,84):
    tc = 0
    for j in range(n):
        if hills[j] < i:
            x = i-hills[j]
        elif hills[j] > i+17:
            x = hills[j] - (i+17)
        else:
            x = 0
        tc += x*x
    cost = min(tc,cost)

with open('skidesign.out','w') as fout:
    fout.write(str(cost) + '\n')
