'''
ID: krishpa2
TASK: combo
LANG: PYTHON3
'''

with open('combo.in','r') as fin:
    N = int(fin.readline())
    f = list(map(int,fin.readline()[:-1].split()))
    m = list(map(int,fin.readline()[:-1].split()))

def close(i,c,N):
    if abs(c-i) <= 2:
        return True
    if abs(i-c) >= N-2:
        return True
    return False

def closeEnough(i,j,k,m1,m2,m3):
    if close(i,m1,N) and close(j,m2,N) and close(k,m3,N):
        return True
out = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if closeEnough(i,j,k,f[0],f[1],f[2]) or closeEnough(i,j,k,m[0],m[1],m[2]):
                out += 1

with open('combo.out','w') as fout:
    fout.write(str(out) + '\n')
