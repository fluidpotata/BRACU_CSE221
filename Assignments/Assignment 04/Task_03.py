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


def DFS(lst,start=1):
    n = len(lst)
    visited = [0 for i in range(n)]
    p = []
    dfs_visit(lst, visited, start, p)
    return p


def dfs_visit(lst, visited, start, path):
    visited[start] = 1
    path.append(start)
    for i in lst[start]:
        if visited[i] == 0:
            dfs_visit(lst, visited, i,path)

with open('input3.txt') as inpfile, open('output3.txt','w') as outfile:
    lst = adjList(inpfile)
    path = DFS(lst)
    outfile.writelines(f"{' '.join(map(str, path))}")