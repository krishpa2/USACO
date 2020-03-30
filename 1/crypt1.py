'''
ID: krishpa2
TASK: crypt1
LANG: PYTHON3
'''

with open('crypt1.in','r') as fin:
    n = int(fin.readline())
    res = list(map(int,fin.readline()[:-1].split()))

two = set()
three = set()
for i in res:
    out = str(i)
    for j in res:
        out = str(i) + str(j)
        two.add(int(out))
        for k in res:
            out = str(i) + str(j) + str(k)
            three.add(int(out))
three = sorted(three)
two = sorted(two)

sol = 0
for i in three:
    for j in two:
        a = str(i*j)
        if len(a) == 4:
            for k in a:
                if int(k) not in res:
                    break
            else:
                b = str(j)
                c = str(int(b[0]) * i)
                if len(c) == 3:
                    for l in c:
                        if int(l) not in res:
                            break
                    else:
                        c = str(int(b[1]) * i)
                        if len(c) == 3:
                            for l in c:
                                if int(l) not in res:
                                    break
                            else:
                                sol += 1
                                
with open('crypt1.out','w') as fout:
    fout.write(str(sol) + '\n')
                    






                        
