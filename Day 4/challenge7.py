with open('input4.txt') as f:
    line = f.readlines()
    matrix = []
    count=0
    for i in range(len(line)):
        line[i] = line[i].strip()
        row = []
        for j in range(len(line[i])):
            row.append(line[i][j])
        matrix.append(row)
    print(matrix)
    lst = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j+3<len(matrix[i]) and "".join((matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+matrix[i][j+3])) in ["XMAS", "SAMX"]:
                if sorted([[i,j],[i,j+1],[i,j+2],[i,j+3]]) not in lst:
                    lst.append(sorted([[i,j],[i,j+1],[i,j+2],[i,j+3]]))
                    count+=1
            if i+3<len(matrix) and "".join((matrix[i][j]+matrix[i+1][j]+matrix[i+2][j]+matrix[i+3][j])) in ["XMAS", "SAMX"]:
                if sorted([[i,j],[i+1,j],[i+2,j],[i+3,j]]) not in lst:
                    lst.append(sorted([[i,j],[i+1,j],[i+2,j],[i+3,j]]))
                    count+=1
            if i+3<len(matrix) and j+3<len(matrix[0]) and "".join((matrix[i][j]+matrix[i+1][j+1]+matrix[i+2][j+2]+matrix[i+3][j+3])) in ["XMAS", "SAMX"]:
                if sorted([[i,j],[i+1,j+1],[i+2,j+2],[i+3,j+3]]) not in lst:
                    lst.append(sorted([[i,j],[i+1,j+1],[i+2,j+2],[i+3,j+3]]))
                    count+=1
            if i-3>=0 and j+3<len(matrix[0]) and "".join((matrix[i][j]+matrix[i-1][j+1]+matrix[i-2][j+2]+matrix[i-3][j+3])) in ["XMAS", "SAMX"]:
                    if sorted([[i,j],[i-1,j+1],[i-2,j+2],[i-3,j+3]]) not in lst:
                        lst.append(sorted([[i,j],[i-1,j+1],[i-2,j+2],[i-3,j+3]]))
                        count+=1
    import pprint
    pprint.pprint(lst)
    print(count)