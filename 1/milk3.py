'''
ID: krishpa2
TASK: milk3
LANG: PYTHON3
'''
import resource
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
from sys import setrecursionlimit
setrecursionlimit(10**6)

with open('milk3.in','r') as fin:
    am,bm,cm = map(int,fin.readline().split())
def mixer(a,b,bc):
    maxAmount = bc-b 
    if a > maxAmount:
        b += maxAmount
        a -= maxAmount
    else:
        b += a
        a = 0
    return [a,b]
used = set()
solutions = set()
solutions.add(cm)

def dfs(a,b,c):
    if a == 0:
        solutions.add(c)
    if (a,b,c) in used:
        return
    else:
        used.add((a,b,c))
        ab = mixer(a,b,bm)
        dfs(ab[0],ab[1],c)
        ac = mixer(a,c,cm)
        dfs(ac[0],b,ac[1])
        ba = mixer(b,a,am)
        dfs(ba[1],ba[0],c)
        bc = mixer(b,c,cm)
        dfs(a,bc[0],bc[1])
        ca = mixer(c,a,am)
        dfs(ca[1],b,ca[0])
        cb = mixer(c,b,bm)
        dfs(a,cb[1],cb[0])
dfs(0,0,cm)

solutions = sorted(solutions)
print(solutions)
with open('milk3.out','w') as fout:
    string = str()
    for i in solutions:
        string += str(i) + " "
    string = string.strip()
    string += '\n'
    fout.write(string)
