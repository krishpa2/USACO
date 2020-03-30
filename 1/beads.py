'''
ID: krishpa2
TASK: beads
LANG: PYTHON3
'''

with open('beads.in','r') as fin:
    n = int(fin.readline())
    beads = fin.readline()[:-1] * 3
    #print(beads)


def canCollect(a):
    return not ('r' in a and 'b' in a)

maxi = 0

for i in range(n,n*2):
    a = i
    left = []
    while a>= 0:
        #print(a)
        if canCollect(left + [beads[a]]):
            left.append(beads[a])
            a -= 1
        else:
            break

    b = i+1
    right = []
    while b <= 3*n-1:
        #print(b)
        if canCollect(right + [beads[b]]):
            right.append(beads[b])
            b += 1
        else:
            break
    res = len(left) + len(right)
    if res >= n:
        maxi = n
        break
    else:
        maxi = max(maxi,res)
#print(maxi)       
with open('beads.out','w') as fout:
    fout.write(str(maxi))
    fout.write('\n')
