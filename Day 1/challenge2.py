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
        popN = lst1[0]
        countPopped = lst1.count(popN)
        for i in range(countPopped):
            lst1.remove(popN)
        countPopped = lst2.count(popN)
        sum1 += popN * countPopped
    print(sum1)