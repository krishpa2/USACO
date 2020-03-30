'''
ID: krishpa2
TASK: palsquare
LANG: PYTHON3
'''


with open('palsquare.in','r') as fin:
    base = int(fin.readline())

def toBase(i,b):
    lst = "0123456789ABCDEFGHIJ"
    res = ""
    while i > 0:
        res += lst[int(i%b)]
        i //= b
    return res[::-1]

with open("palsquare.out",'w') as fout:
    for i in range(1,301):
        r = str(toBase(i,base))
        ra = str(toBase(i**2,base))
        if ra == ra[::-1]:
            fout.write(r + " " + ra + '\n')
        

