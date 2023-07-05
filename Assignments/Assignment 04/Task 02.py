def adjList(inp):
    n, m = inp.readline().split()
    n, m = int(n), int(m)
    given = []
    for i in range(m):
        given.append([int(i) for i in inp.readline().split()])

    adjlist = [[]] * (n+1)
    for j in range(len(given)):
        u, v= given[j]
        if len(adjlist[u]) > 0:
            adjlist[u].append(v)
        else:
            adjlist[u] = [v]


    return adjlist

queue = []

def colorC(ad_list):
    color = []
    for i in range(len(ad_list)):
        color.append(0)
    return color

def BFS(ad_list,s=1):
    color = colorC(ad_list)
    q = []
    q.append(s)
    path = []
    while q:
        u = q.pop(0)
        if color[u] == 0:
            color[u] == 1
            path.append(u)
        for v in ad_list[u]:
            q.append(v)
    print(path)



with open("input2.txt") as inpfile:
    lst = adjList(inpfile)
    print(lst)
    BFS(lst)
