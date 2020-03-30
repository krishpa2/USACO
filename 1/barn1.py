'''
ID: krishpa2
TASK: barn1
LANG: PYTHON3
'''

with open('barn1.in','r') as fin:
    m,s,c = map(int,fin.readline().strip().split())
    res = []
    for i in range(c):
        res.append(int(fin.readline()))
    res.sort()

gaps = [res[i] - res[i-1] - 1 for i in range(1,len(res))] #using example of [3,4]. There should be no gap as the stalls are adjacent. So you must minus 1 after you subtract them.
gaps.sort()

if m > c: #prevents popping off from an empty array
    length = c
else:
    total = 0
    for i in range(m-1): #We are removing m-1 gaps to have m boarded areas. Using example 1111111, 1 represents a boarded area. If we remove 3 boarded areas at random, we might get 1010101. This leaves 4 boarded areas. So, remove m-1 gaps, to be left with m boarded areas. 
        total += gaps.pop() #largest gap is being added
    total += res[0]  -1 #we have to account for if the first cow stall does not start at 1 
    total += s-res[-1] #we have to account for if the last cow stall does not end at S (number of stalls)

    length = s - total #returns minimum boarded area as we get rid of the largest gaps. 
with open('barn1.out','w') as fout:
    fout.write(str(length) + '\n')

