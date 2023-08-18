def adjList(inp):
    n, m = map(int, inp.readline().split())
    given = []
    for i in range(m):
        given.append(list(map(int, inp.readline().split())))

    adjlist = [[] for k in range(n + 1)]
    for j in range(len(given)):
        u, v = given[j]
        adjlist[u].append(v)
    return adjlist

def topologicalSort(adjlist):
    n = len(adjlist) - 1
    indegree = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in adjlist[u]:
            indegree[v] += 1

    queue = []
    for u in range(1, n + 1):
        if indegree[u] == 0:
            queue.append(u)

    result = []
    while queue:
        u = min(queue)
        queue.remove(u)
        result.append(u)

        for v in adjlist[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    if len(result) != n:
        return ["IMPOSSIBLE"]
    else:
        return result


with open("input2.txt") as input_file, open("output2.txt","w") as output_file:
    lst = adjList(input_file)
    choice = topologicalSort(lst)
    output_file.writelines(f"{' '.join(map(str, choice))}")