'''
ID: krishpa2
TASK: friday
LANG: PYTHON3
'''

with open('friday.in','r') as fin:
    n = int(fin.readline()[:-1])

def leapYear(n):
    if n % 100 == 0:
        return n%400 == 0
    return n%4 ==0

#starts on january 1, 1900 Monday

dayArr = ["saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
dayStats = dict()
for i in dayArr:
    dayStats[i] = 0

currYear = 1900
currDay = "monday"
beg = True #accounts for starting on monday, jan 1 1900
for i in range(n):
    #31 days January, March, May, July 
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if leapYear(currYear) == True:
        months[1] = 29
    if beg == True:
        months[0] -= 1
        num = 1
        beg = False
    else:
        num = 0
    currMonth = 0
    for i in range(sum(months)):
        #print(str(num) + " " + str(currMonth))
        if months[currMonth] == 0:
            currMonth += 1
            num = 0
        num += 1
        months[currMonth] -= 1

        if dayArr.index(currDay) != 6:
            currDay = dayArr[dayArr.index(currDay) + 1]
        else:
            currDay = "saturday"
            
        if num == 13:
            dayStats[currDay] += 1
        #print(months)
        #assert (num == 30 and currMonth == 1) == False 
        #print(months)
    currYear += 1
with open('friday.out','w') as fout:
    out = ""
    for a,b in dayStats.items():
        out += str(b) + " "
    out = out.strip()
    #print(out)
    fout.write(out)
    fout.write('\n')
