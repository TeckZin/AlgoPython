

graph: list[list[int]] = [ [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
                           ]

vistedGraph: list[list[int]]

visitedGraph = [[0 for y in range(len(x)) ] for x in graph]



def dfs(i: int, j: int, count):
    v = graph[i][j]
    count = count + 1


    visitedGraph[i][j] = count

    if j != len(graph)-1:
        if visitedGraph[i][j+1] == 0 and graph[i][j+1] == 1:
            dfs(i, j+1, count)
    if j != 0:
        if visitedGraph[i][j-1] == 0 and graph[i][j-1] == 1:
            dfs(i, j-1, count)
    if i != len(graph[0]) - 1:
        if visitedGraph[i+1][j] == 0 and graph[i+1][j] == 1:
            dfs(i+1, j, count)
    if i != 0:
        if visitedGraph[i-1][j] == 0 and graph[i-1][j] == 1:
            dfs(i-1, j, count)



if __name__ == '__main__':
    print("hello")
    # print(graph)
    # print(visitedGraph)
    for x in graph:
        print(x)

    # for x in visitedGraph:
    #     print(x)


    island: int = 0
    count = 0
    for i, x in enumerate(graph):

        for j, v in enumerate(x):
            # print(i, j, v)

            if v == 1 and visitedGraph[i][j] == 0:
                island += 1
                dfs(i, j, count)


    print(island)
    for x in visitedGraph:
        print(x)
