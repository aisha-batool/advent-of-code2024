lst1  = []
lst2 = []
sum1 = 0
with open('input1.txt') as f:
    lines = f.readlines()

    for i in lines:
        x, y = i.split()
        lst1.append(int(x))
        lst2.append(int(y))

    while lst1!=[]:
        minLst1 = min(lst1)
        minLst2 = min(lst2)
        lst1.remove(min(lst1))
        lst2.remove(min(lst2))
        sum1 += abs(minLst1-minLst2)
    print(sum1)