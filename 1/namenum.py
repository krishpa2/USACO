'''
ID: krishpa2
TASK: namenum
LANG: PYTHON3
'''
'''
          2: A,B,C     5: J,K,L    8: T,U,V
          3: D,E,F     6: M,N,O    9: W,X,Y
          4: G,H,I     7: P,R,S
'''

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
           'R','S','T','U','V','W','X','Y']
let = []
for i in range(0,24,3):
    let.append(letters[i:i+3]) #grouping letters by three 
    
dicti = dict() #assigns each number from [2,9] a group of three letters
for i in range(2,10):
    dicti[str(i)] = let[i-2]

names = set() #reading in a file of almost 4000 acceptable names
with open('dict.txt','r') as d:
    while True:
        name = d.readline().strip()
        if name != "":
            names.add(name)
        else:
            break

with open('namenum.in','r') as fin:
    num = str(fin.readline().strip()) #the number being used to determine all combinations
    
numCount = []
for i in range(len(num)):
    numCount.append(dicti[num[i]]) #creates a 2d array where each number in the initial 'num' has a group of three letters


def cartesian_iterative(pools): #returns the product of a 2d array
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    return result

pos = set() #set of possible names
if len(num) == 12: #only uses more than the allocated memory when the num is 12 digits long.
    '''
    This optimization allows the product to only calculate 2 * 3^6 values, instead of 3**12. This saves a lot of memory
    '''
    rights = cartesian_iterative(numCount[6:])
    for left in cartesian_iterative(numCount[:6]):
        for right in rights:
            a = ''.join(left+right)
            if a in names:
                pos.add(a) #adding name to set
else: #if len(num) < 12, you do not need any other optimizations and can just return normal product 
    for i in cartesian_iterative(numCount):
        a = ''.join(i)
        if a in names:
            pos.add(a)
pos = sorted(pos)
with open('namenum.out','w') as fout: #outputting all possible names
    if len(pos) > 0:
        for i in pos:
            fout.write(i)
            fout.write('\n')
    else:
        fout.write('NONE\n')
    

