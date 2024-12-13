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
    import math
    for line in linesToCheck:
        invalid=True
        line = list(map(int, line.split(',')))
        for i in range(len(line)):
            for j in range(i, len(line)):
                if line[i] in dict and line[j] in dict[line[i]]:
                    pass
                elif line[j] not in dict:
                    pass
                elif line[j] in dict and line[i] in dict[line[j]]:
                    invalid=False
                    break
        if invalid:
            import math
            summed += line[len(line)//2]
    print("HERE", summed)