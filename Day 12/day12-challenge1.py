def bfs(matrix, graph, queue, visited, requiredN):
    if queue == []:
        return visited
    val = queue.pop(0)
    
    if val not in visited:
        visited.append(val)

    for i in graph[val]:
        if i not in visited and matrix[i[0]][i[1]]==requiredN:
            queue.append(i)
            bfs(matrix, graph, queue, visited, requiredN)
    return visited
with open("inputted.txt") as f:
    line = f.readlines()
    matrix = []
    for i in range(len(line)):
        row = []
        for j in range(len(line)):
            row.append(line[i][j])
        matrix.append(row)
    print(matrix)

    graph = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            graph[(i, j)] = []
            if i-1>=0:
                graph[(i, j)].append((i-1, j))
            if j-1>=0:
                graph[(i, j)].append((i, j-1))
            if i+1<len(matrix):
                graph[(i, j)].append((i+1, j))
            if j+1<len(matrix):
                graph[(i, j)].append((i, j+1))

    path=[]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            p = sorted(bfs(matrix, graph, [(i, j)], [(i, j)], matrix[i][j]))
            if p not in path:
                path.append(p)
    print(path)
    summed = 0
    for row in path:
        perimeter = 0
        for i, j in row:
            if i-1<0 or (i-1, j) not in row:
                perimeter+=1
            if j-1<0 or (i, j-1) not in row:
                perimeter+=1
            if i+1>=len(matrix) or (i+1, j) not in row:
                perimeter+=1
            if j+1>=len(matrix) or (i, j+1) not in row:
                perimeter+=1
        print(matrix[row[0][0]][row[0][1]], perimeter)
        summed+=len(row)*perimeter
    print(summed)