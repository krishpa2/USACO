'''
ID: krishpa2
TASK: ariprog
LANG: PYTHON3
'''

#import time
#start_time = time.time()

with open('ariprog.in','r') as fin:
    n = int(fin.readline())
    m = int(fin.readline())

bisq = set()
for i in range(m+1):
    for j in range(m+1):
        bisq.add(i**2 + j**2)
bisq = set(bisq)
ibisq = sorted(bisq)
solutions = set()

for i in range(len(ibisq)-1,n-2,-1): #find starting seed
    man = ibisq[i]
    chg = 1
    wife = ibisq[i-chg]
    step = man - wife
    maxStep = man // (n-1)
    while step <= maxStep:
        flag = True
        for j in range(n-2):
            wife -= step
            if wife not in bisq:
                flag = False
                break
        if flag:
            solutions.add((wife,step))
        chg += 1
        wife = ibisq[i-chg]
        step = man-wife

solutions = list(solutions)
solutions.sort(key = lambda x: [x[1],x[0]])
with open('ariprog.out','w+') as fout:
    if len(solutions):
        for i in solutions:
            fout.write(str(i[0]) + " "  + str(i[1]))
            fout.write('\n')
    else:
        fout.write('NONE\n')

