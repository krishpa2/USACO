with open('namenumdict.txt','r') as d:
    count = 0
    while True:
        name = d.readline().strip()
        if name != "":
            if len(name) == 12:
                print(name)
                count += 1
        else:
            break

print(count)
