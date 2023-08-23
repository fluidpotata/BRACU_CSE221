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


# def cycle_finder(lst):
#     n = len(lst)
#     visited = [0 for _ in range(n)]
#     for i in range(n):
#         if visited[i] == 0:
#             if dfs(lst, visited, i, parent=None):
#                 return True
#     return False
#
#
# def dfs(lst, visited, start, parent):
#     visited[start] = 1
#     for i in lst[start]:
#         if visited[i] == 0:
#             if dfs(lst, visited, i, parent=start):
#                 return True
#         elif i != parent:
#             return True
#     return False


def cycle_finder(lst, start=1):
    n = len(lst)
    visited = [0 for i in range(n)]
    p = []
    return dfs_visit_cycle(lst, visited, start, p)


def dfs_visit_cycle(lst, visited, start, path):
    visited[start] = 1
    path.append(start)
    for i in lst[start]:
        if visited[i] == 0:
            if dfs_visit_cycle(lst, visited, i, path):
                return True
        elif i in path[:-1]:
            return True
    path.pop()
    return False


def DFS(lst,p,visited,start=1):
    n = len(lst)
    # visited = [0 for i in range(n)]
    dfs_visit(lst, visited, start, p)
    return p


def dfs_visit(lst, visited, start, path):
    visited[start] = 1
    path.append(start)
    for i in lst[start]:
        if visited[i] == 0:
            dfs_visit(lst, visited, i,path)


with open("input1.txt") as input_file, open("output1.txt","w") as output_file:
    graph = adjList(input_file)
    visited = [0 for i in range(len((graph)))]
    has_cycle = False
    in_degree = [0 for i in range(len(graph))]
    choice = []
    for i in graph:
        for j in i:
            in_degree[j] += 1
    print(in_degree)
    for i in range(1,len(in_degree)):
        if in_degree[i]==0:
            has_cycle = has_cycle or cycle_finder(graph,i)
    if has_cycle:
        choice = ["IMPOSSIBLE"]
    else:
        for i in range(1, len(in_degree)):
            if in_degree[i] == 0:
                DFS(graph,choice,visited)
    print(visited)
    if len(choice) != len(graph)-1:
        choice = ["IMPOSSIBLE"]
    # if 0 in visited[1:]:
    #     choice = ["IMPOSSIBLE"]

    output_file.writelines(f"{' '.join(map(str, choice))}")
