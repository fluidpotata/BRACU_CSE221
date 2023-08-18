def adjList(inp):
    n, m, target = inp.readline().split()
    n, m, target = int(n), int(m), int(target)
    given = []
    for i in range(m):
        given.append([int(i) for i in inp.readline().split()])

    adjlist = [[] for k in range(n + 1)]
    for j in range(len(given)):
        u, v= given[j]
        adjlist[u].append(v)
        adjlist[v].append(u)
    return adjlist, target


def shortest_path(graph, start, target):
    visited = [0] * len(graph)
    q = []
    q.append((start, [start]))
    visited[start] = True

    while q:
        u, path = q.pop(0)
        if u == target:
            return len(path)-1, path

        for v in graph[u]:
            if visited[v]==0:
                q.append((v, path + [v]))
                visited[v] = 1
    return None, None


with open("input5.txt") as inpfile, open("output5.txt","w") as outfile:
    lst, t = adjList(inpfile)
    t, p = shortest_path(lst, 1, t)
    outfile.writelines(f"Time: {t}\n")
    outfile.writelines(f"Shortest path: {' '.join(map(str,p))}")


''' To find shortest distance, we use BFS appraoch. Here while exploring a vertex, I've kept another list to keep the track
of path from start to the vertex. So while a vertex is discovered first, we add them into queue with the path that has followed
it. So when it is being visited and matched as our target, the path is returned, else we explore that vertex and keep adding
the path to them.
'''
