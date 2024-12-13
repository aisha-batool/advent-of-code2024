# Using dictionary improved the speed of processing the large data

import pprint
with open('input11.txt') as f:
    line = f.readlines()[0]
    lst = list(map(int, line.split()))
    dict = {}
    for i in lst:
        dict[i] = dict.get(i, 0) + 1
    print(dict)
    for i in range(75):
        newDict = {}
        for k, v in dict.items():
            if k == 0:
                newDict[1] = newDict.get(1, 0) + v
            elif len(str(k))%2==0:
                dig = str(k)
                dig1 = int(dig[:(len(dig))//2])
                dig2 = int(dig[(len(dig))//2:])
                newDict[dig1] = newDict.get(dig1, 0)+v
                newDict[dig2] = newDict.get(dig2, 0)+v
            else:
                newDict[k*2024] = newDict.get(k*2024, 0) + v
        dict = newDict
        print(dict)
    print(sum(newDict.values()))