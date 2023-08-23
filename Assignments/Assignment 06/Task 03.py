def adjList(inp):
    n, m = inp.readline().split()
    n, m = int(n), int(m)
    given = []
    for i in range(m):
        given.append([int(i) for i in inp.readline().split()])

    adjlist = [[] for k in range(n + 1)]
    for j in range(len(given)):
        u, v= given[j]
        adjlist[u].append(v)
    return adjlist


def DFS(lst, s):
    n = len(lst)
    visited = [0 for i in range(n)]
    for i in range(1, n):
        if visited[i] == 0:
            dfs_visit(lst, visited, i, s)
    return s

def dfs_visit(lst, visited, start, s):
    visited[start] = 1
    for i in lst[start]:
        if visited[i] == 0:
            dfs_visit(lst, visited, i, s)
    s.append(start)


def dfs_transposed(graph, v, visited, scc):
    visited[v] = True
    scc.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs_transposed(graph, i, visited, scc)


def transposeGraph(graph):
    n = len(graph)
    new = [[] for i in range(n)]
    for i in range(n):
        for j in graph[i]:
            new[j].append(i)
    return new


with open("input3.txt") as input_file, open("output3.txt", "w") as output_file:
    lst = adjList(input_file)
    stack = []
    stack = DFS(lst, stack)
    print(stack)
    tg = transposeGraph(lst)
    visited = [0 for i in range(len(tg))]
    strongly_connected_components = []

    while stack:
        u = stack.pop()
        if visited[u] == 0:
            tmp = []
            dfs_transposed(tg, u, visited, tmp)
            strongly_connected_components.append(tmp)
    for j in strongly_connected_components:
        output_file.writelines(" ".join(map(str, j)))
        output_file.writelines("\n")