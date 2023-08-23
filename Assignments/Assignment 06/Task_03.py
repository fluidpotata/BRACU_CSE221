def adjList(inp):
    n,m = map(int, inp.readline().split())
    given = []
    for i in range(m):
        given.append([int(i) for i in inp.readline().split()])

    adjlist = [[] for k in range(n + 1)]
    for j in range(len(given)):
        u, v, w= given[j]
        adjlist[u].append((v,w))
    return adjlist


def findMinimumDistance(queue):
    mindist = queue[0][1]
    minind = 0
    for i in range(len(queue)):
        if queue[i][1]<mindist:
            mindist = queue[i][1]
            minind = i
    return queue.pop(minind)


def dijkstra(graph,start=1):
    n = len(graph)
    visited = [0 for i in range(n)]
    distance = [-1 for i in range(n)]
    queue = []
    visited[start] = 1
    distance[start] = 0
    for i in graph[start]:
        queue.append(i)
    while queue:
        currNode = findMinimumDistance(queue)
        if visited[currNode[0]]==0:
            visited[currNode[0]] = 1
            distance[currNode[0]] = currNode[1]
            for i in graph[currNode[0]]:
                queue.append((i[0],max(i[1],currNode[1])))

    return distance[-1]



with open("input3.txt") as input_file, open("output3.txt","w") as output_file:
    lst  = adjList(input_file)
    x = dijkstra(lst)
    output_file.writelines(str(x))
