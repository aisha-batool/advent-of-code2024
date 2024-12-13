def getdigit(ans):
    for i in range(len(ans) - 1, -1, -1):
        if ans[i].isdigit():
            return i, ans[i]

def all_dots_at_end(s, dotF):
    firstInd = s.find('.', dotF)
    return s[firstInd:].count('.') == len(s) - firstInd

with open('input9.txt') as f:
    line = f.readlines()[0]
    ans = []
    id = 0
    for i in range(0, len(line)):
        if i % 2 == 0:
            ans.extend([str(id)] * int(line[i]))
            id += 1
        else:
            ans.extend(['.'] * int(line[i]))

    left = 0
    right = len(ans) - 1
    dotF = 0

    while all_dots_at_end("".join(ans), dotF)==False:
        dotF = ans.index('.', dotF)
        digitF, val = getdigit(ans)
        ans[digitF], ans[dotF] = '.', val

    checkSum = 0
    for i in range(len(ans)):
        if ans[i].isdigit():
            checkSum += i * int(ans[i])
        else:
            break
    
    print(checkSum)