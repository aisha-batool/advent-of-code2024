def func(i):
    found = False
    if sorted(i) == i:
        for index in range(len(i)-1):
            if i[index+1] not in [i[index]+1, i[index]+2, i[index]+3]:
                found=True
    else:
        for index in range(len(i)-1):
            if i[index+1] not in [i[index]-1, i[index]-2, i[index]-3]:
                found=True
    return found

count = 0
with open('input2.txt') as f:
    lines = f.readlines()
    for i in lines:
        done = False
        i = list(map(int, i.split()))
        if sorted(i) == i or sorted(i)[::-1]==i: 
            found = func(i)
            if found == False:
                count+=1
                done = True
        if done == False:
            for j in range(len(i)):
                newLst = i[:j] + i[j+1:]
                if sorted(newLst) == newLst or sorted(newLst)[::-1]==newLst: 
                    found = func(newLst)
                    if found ==False:
                        count+=1
                        break
                

    print(count)