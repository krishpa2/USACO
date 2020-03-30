'''
ID: krishpa2
TASK: milk
LANG: PYTHON3
'''

with open('milk.in','r') as fin:
    n,m = map(int,fin.readline().strip().split())
    unOrderedPrices = dict()
    for i in range(m):
        a,b = map(int,fin.readline().strip().split())
        try:
            unOrderedPrices[a] += b
        except:
            unOrderedPrices[a] = b

    keys = sorted(unOrderedPrices.keys())
    prices = dict()
    for i in keys:
        prices[i] = unOrderedPrices[i]
    total = 0
    for a,b in prices.items():
        if n == 0:
            break
        if b < n:
            n -= b
            total += a * b
        else:
            total += n * a
            n -= n

with open('milk.out','w') as fout:
    fout.write(str(total) + '\n')
    
