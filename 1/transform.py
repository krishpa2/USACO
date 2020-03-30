'''
ID: krishpa2
TASK: transform
LANG: PYTHON3
'''

def clockwise(a):
    final = []
    for x in range(n):
        res = []
        for c in range(n):
            res.append(a[n-c-1][x])
        final.append(res)
    return final
        
def reflection(res):
    for i in range(n):
        res[i] = res[i][::-1]
    return res

with open('transform.in','r') as fin:
    n = int(fin.readline())
    orig = []
    for i in range(n):
        orig.append(list(fin.readline()[:-1]))
    new = []
    for i in range(n):
        new.append(list(fin.readline()[:-1]))

'''
types of reflections
1 90 degree clockwise
2 180 degree clockwise
3 270 degree clockwise
4 Reflection horizontally
5 Combination (horiz + 1-3)
6 No change                            done
7 Invalid
'''
a = orig[:]
b = orig[:]
c = orig[:]
num = -1
for i in range(3):
    a = clockwise(a)
    if a == new:
        num = i+1
        break
else:
    b = reflection(b)
    if b == new:
        num = 4
    else:
        for i in range(3):
            b = clockwise(b)
            if b == new:
                num = 5
                break
if num == -1:
    if c == new:
        num = 6
    else:
        num = 7

with open('transform.out','w') as fout:
    fout.write(str(num))
    fout.write('\n')











