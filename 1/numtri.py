'''
ID: krishpa2
TASK: numtri
LANG: PYTHON3
'''

with open('numtri.in','r') as fin:
    n = int(fin.readline())
    rows = []
    for i in range(n):
        out = list(map(int,fin.readline().split()))
        rows.append(out)
        if i == n-1:
            res = out
print(rows)
for i in reversed(range(1,n)):
    for j in range(i): 
        res[j] = rows[i-1][j] + max(res[j+1],res[j])
ans = str(max(res)) + '\n'
print(ans)
with open('numtri.out','w+') as fout:
    fout.write(ans)










