import re

with open('input3.txt') as f:
    line = f.readlines()
    lst=[]
    for lines in line:
        i=0
        while True:
            if i<len(lines) and lines[i:i+4]=="mul(":
                i = i+4
                dig1 = ""
                while i<len(lines) and lines[i]!="," and lines[i].isdigit():
                    dig1 += lines[i]
                    i+=1
                if lines[i] == ",":
                    i+=1
                    dig2 = ""
                    while i<len(lines) and lines[i]!=")" and lines[i].isdigit():
                        dig2 += lines[i]
                        i+=1
                    if lines[i]==")":
                        i+=1
                        lst.append(int(dig1) * int(dig2))
                    else:
                        i+=1
                else:
                    i+=1
            else:
                i = i+1
            if i>=len(lines):
                break
    print(sum(lst))