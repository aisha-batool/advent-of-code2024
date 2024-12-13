import pprint
with open('input11.txt') as f:
    line = f.readlines()[0]
    lst = list(map(int, line.split()))
    print(lst)
    for i in range(75):
        print(i)
        newL = []
        for val in lst:
            if val==0:
                newL.append(1)
            elif len(str(val))%2==0:
                digitInString = str(val)
                dig1 = int(digitInString[:len(str(val))//2])
                dig2 = int(digitInString[len(str(val))//2:])
                newL.append(dig1)
                newL.append(dig2)
            else:
                newL.append(val*2024)
        lst = newL
    print(len(lst))