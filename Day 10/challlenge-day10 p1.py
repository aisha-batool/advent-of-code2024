# Good Problem for DFS/BFS

def bfs(matrix, graph, start, queue, path, visited, requiredN):
    if queue == []:
        return visited
    val = queue.pop(0)
    
    if val not in visited:
        visited.append(val)

    if matrix[val[0]][val[1]]==9:
        path.append(visited.copy())
        # visited.pop()
        # visited.pop(0)

    for i in graph[val]:
        if i not in visited and matrix[i[0]][i[1]]==requiredN:
            queue.append(i)
            bfs(matrix, graph, i, queue, path, visited, requiredN+1)
    # return visited
import pprint
with open('input10.txt') as f:
    line = f.readlines()
    matrix = []
    count=0
    for i in range(len(line)):
        row = []
        for j in range(len(line)):
            if line[i][j].isdigit():
                row.append(int(line[i][j]))
            else:
                row.append(line[i][j])
        matrix.append(row)
    pprint.pprint(matrix)

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
    # print(graph)
    # print(bfs(graph, (0, 0)))
    path=[]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                bfs(matrix, graph, (i, j), [(i, j)], path, [(i, j)], 1)
    lastSame = {}

    print(path)

    for i in range(len(path)):
        row, col = path[i][0]
        lastSame[(row, col)] = lastSame.get((row, col), 0)+1
    print(lastSame)
    print(sum(list(lastSame.values())))
    #         if matrix[i][j] == 0:
    #             print(bfs(matrix, matrix[i][j], [[i, j]]))