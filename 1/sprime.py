'''
ID: krishpa2
TASK: sprime
LANG: PYTHON3
'''

with open('sprime.in','r') as fin:
    n = int(fin.readline())
def isPrime(x):
    x = abs(int(x))
    if x == 2:
        return True
    if x == 1:
        return False
    if x in (3,5,7):
        return True
    if x % 2 == 0 or x%3 == 0 or x % 5 == 0 or x%7 ==0:
        return False
    for i in range(2,int(x**.5)+1):
         if x % i == 0:  
                return False
    return True
fout = open('sprime.out','w+') 
def dfs(start,depth):
    if depth == n:  
        fout.write(str(start))
        fout.write('\n')
        return 
    for i in range(1,10,2):
        p = start * 10 + i
        if isPrime(p):
            dfs(p,depth+1)
for i in [2,3,5,7]:
    dfs(i,1)
