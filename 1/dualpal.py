'''
ID: krishpa2
TASK: dualpal
LANG: PYTHON3
'''

with open('dualpal.in','r') as fin:
    n,s = map(int,fin.readline().strip().split())

def toBase(i,b):
    res = ""
    lrs = "0123456789"
    while i > 0:
        res += lrs[i%b]
        i //= b
    return res[::-1]

with open('dualpal.out','w') as fout:
    s += 1
    while s < 100000:
        if n == 0:
            break
        lc = 0
        for i in range(2,11):
            a = toBase(s,i)
            if a[0] != "0" and a == a[::-1]:
                lc += 1
            if lc == 2:
                n -= 1
                fout.write(str(s) + '\n')
                break
        s += 1
    
