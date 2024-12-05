count = 0
with open('input2.txt') as f:
    lines = f.readlines()
    for i in lines:
        i = list(map(int, i.split()))
        if sorted(i) != i and sorted(i)[::-1]!=i:
            count += 0
        else:
            found = False
            if sorted(i) == i:
                for index in range(len(i)-1):
                    if i[index+1] not in [i[index]+1, i[index]+2, i[index]+3]:
                        found=True
            else:
                for index in range(len(i)-1):
                    if i[index+1] not in [i[index]-1, i[index]-2, i[index]-3]:
                        found=True
            if found == False:
                count+=1

    print(count)