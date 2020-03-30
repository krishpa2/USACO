"""
ID: krishpa2
TASK: wormhole
LANG: PYTHON3
"""
with open('wormhole.in','r') as fin:
    N = int(fin.readline())
    holes = []
    for i in range(N):
        x,y = map(int,fin.readline().strip().split())
        holes.append([x,y])

partner = [-1] * (N+1)
next_on_right = [-1] * (N+1)
for i in range(N):
    for j in range(N):
        if (holes[j][0] > holes[i][0] and holes[i][1] == holes[j][1]): #holes[j] has same y value and is greater than hole[i]
            if (next_on_right[i]==-1 or holes[next_on_right[i]][0] > holes[j][0]): #not assigned a point or it isn't the closest point on the right
                next_on_right[i]=j
def cycle_exists():
    for i in range(N):
        s=i
        for j in range(N):
            s=next_on_right[partner[s]]
        if(s!=-1):
            return 1
    return 0
def pair():
    t=0
    for i in range(N):
        if partner[i]==-1: #unpaired so we need to pair it
            break
    if partner[i]!=-1:
        if cycle_exists(): #everything is paired so we test for cycle
            return 1
        return 0
    
    for j in range(i+1,N): #try to pair points after i 
        if partner[j]==-1:
            partner[i]=j #pair the wormholes
            partner[j]=i
            t += pair()
            partner[i]=-1 #set pairs back to -1 to pair again 
            partner[j]=-1
    return t
t=pair()
with open('wormhole.out','w') as fout:
    fout.write(str(t))
    fout.write('\n')
