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

with open("input1.txt") as input_file, open("output1.txt","w") as output_file:
    graph = adjList(input_file)
    visited = [0 for i in range(len(graph))]
    indegree = [0 for i in range(len(graph))]
    choice = []
    for i in graph:
        for j in i:
            indegree[j] += 1

    q = []
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    while q:
        u = q.pop(0)
        if visited[u] == 0:
            visited[u] = 1
            choice.append(u)
        for i in graph[u]:
            indegree[i] -= 1
        for i in range(1, len(indegree)):
            if indegree[i] == 0 and visited[i] == 0:
                q.append(i)
    if 0 in visited[1:]:
        choice = ["IMPOSSIBLE"]

    output_file.writelines(f"{' '.join(map(str, choice))}")