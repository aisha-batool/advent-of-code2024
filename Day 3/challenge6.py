with open('input3.txt') as f:
    line = f.readlines()
    lst=[]
    enabled = True
    for lines in line:
        i=0
        while True:
            if enabled and i<len(lines) and lines[i:i+4]=="mul(":
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
                        if lst[-1]==[627, 533]:
                            print(lst[-1])
                    else:
                        pass
                else:
                    pass
            elif enabled and i<len(lines) and lines[i:i+7]=="don't()":
                i+=7
                enabled = False
                while i<len(lines) and lines[i:i+4]!="do()":
                    i=i+1
                if lines[i:i+4]=="do()":
                    i+=4
                    enabled=True
            elif enabled==False:
                while i<len(lines) and lines[i:i+4]!="do()":
                    i=i+1
                if lines[i:i+4]=="do()":
                    i+=4
                    enabled=True
            else:
                i = i+1
            if i>=len(lines):
                break
    print(sum(lst))