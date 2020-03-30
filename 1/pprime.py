'''
ID: krishpa2
TASK: pprime
LANG: PYTHON3
'''

with open('pprime.in','r') as fin:
    a,b = map(int,fin.readline().split())

def isPrime(x):
    x = int(x)
    if x in (2,3,5,7,11,13,17):
        return True
    if x == 1:
        return False
    for i in (2,3,5,7,11,13,17):
        if x % i == 0:
            return False
    for i in range(13,int(x**.5)+1):
         if x % i == 0:  
                return False
    return True

primeList = set()
def gen(x,even):
    if even == 1:
        n = int(str(x) + str(x)[::-1])
        if a <= n <= b:
            if isPrime(n):
                primeList.add(n)
        return
    else: #odd
        for i in range(10):
            n = int(str(x) + str(i) + str(x)[::-1])
            if a<= n <= b:
                if isPrime(n):
                    primeList.add(int(n))
        return
for i in range(1,10):
    if a <= i <= b and isPrime(i):
        primeList.add(i)
for i in range(1,10000):
    gen(i,1)
    gen(i,0)
primeList = sorted(primeList)
with open('pprime.out','w+') as fout:
    for i in primeList:
        fout.write(str(i))
        fout.write('\n')


                    
