def find_dots_seq(s, countReq, until):
    for i in range(0, until):
        if s[i:i+countReq] == "."*countReq:
            print(s[i:i+countReq])
            return i
    return -1

with open('input9.txt') as f:
    line = f.readlines()[0]
    ans = []
    id = 0
    for i in range(0, len(line)):
        if i % 2 == 0:
            ans.extend([str(id)] * int(line[i]))
            if int(line[i])==0:
                print(str(id))
            id += 1
        else:
            ans.extend(['.'] * int(line[i]))
    left = 0
    right = len(ans) - 1
    dotF = 0
    for j in range(id-1, -1, -1):
        print(j)
        countID = ans.count(str(j))
        until = ans.index(str(j))
        dotF = -1
        for i in range(0, until):
            if ans[i:i+countID] == ["."]*countID:
                dotF = i
                while str(j) in ans:
                    ans[ans.index(str(j))]='.'
                if ans[dotF:dotF+countID] == ["."]*countID:
                    ans[dotF:dotF+countID] = [str(j)]*countID
                break
    checkSum = 0
    for i in range(len(ans)):
        if ans[i].isdigit():
            checkSum += i * int(ans[i])
    
    print(checkSum)
