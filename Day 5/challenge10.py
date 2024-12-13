with open("input5.txt") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i]=lines[i].strip()
    print(lines)
    ind = lines.index('')
    print(lines[:ind])

    orderingList = lines[:ind]
    dict={}
    newDict = {}
    for line in orderingList:
        i, j = list(map(int, line.split('|')))
        dict[i] = dict.get(i, []) + [j]

    for k, v in dict.items():
        for val in v:
            newDict[val] = newDict.get(val, []) + [k]
    print(dict)
    # print(newDict)
    linesToCheck = lines[ind+1:]
    summed = 0
    toBeSummed = False
    import math
    for line in linesToCheck:
        invalid=True
        line = list(map(int, line.split(',')))
        toBeSummed=False
        while True:
            for i in range(len(line)):
                for j in range(i, len(line)):
                    if line[j] in dict and line[i] in dict[line[j]]:
                        line[i], line[j]=line[j], line[i]
                        invalid=False
                        toBeSummed=True
                        break
            if invalid==False:
                invalid=True
            elif toBeSummed==True:
                import math
                summed += line[len(line)//2]
                break
            else:
                break
    print("HERE", summed)