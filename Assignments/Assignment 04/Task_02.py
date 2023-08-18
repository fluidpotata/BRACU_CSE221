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
        adjlist[v].append(u)
    return adjlist



def BFS(ad_list,s=1):
    visited = [0]*len(ad_list)
    q = []
    q.append(s)
    path = []
    while q:
        u = q.pop(0)
        if visited[u] == 0:
            visited[u] = 1
            path.append(u)
        for v in ad_list[u]:
            if visited[v]==0:
                q.append(v)
    return path



with open("input2.txt") as inpfile, open("output2.txt","w") as outfile:
    lst = adjList(inpfile)
    path = BFS(lst)
    outfile.writelines(f"{' '.join(map(str, path))}")


''' BFS traversing systems completely explores a vertex before moving on to a next vertex. In this code, I've used a queue, 
where we start by including our start. And a loop runs until the queue is empty, so while the queue is not empty, we dequeue
a vertex from queue, mark it visited then every unvisited vertex we can find with that we enqueue them. Since queue is FIFO
so first every node we found from a vertex is visited, meaning we go by level every time. So this approach fulfills the 
requirements of BFS.
'''
