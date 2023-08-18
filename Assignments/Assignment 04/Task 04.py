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

def DFS(lst, start=1):
    n = len(lst)
    visited = [0 for i in range(n)]
    p = []
    return dfs_visit(lst, visited, start, p)



def dfs_visit(lst, visited, start, path):
    visited[start] = 1
    path.append(start)
    for i in lst[start]:
        if visited[i] == 0:
            if dfs_visit(lst, visited, i, path):
                return True
        elif i in path:
            return True
    path.pop()
    return False


with open('input4.txt') as inpfile, open('output4.txt','w') as outfile:
    lst = adjList(inpfile)
    has_cycle = DFS(lst)
    if has_cycle:
        outfile.writelines("YES")
    else:
        outfile.writelines("NO")


''' Since DFS discovers the full path first, we use DFS to find out if there is any loop in a graph. Here we check while
 exploring a vertex that if a vertex is already present in the stack, that means it has a loop. That's what this algorithm
 finds. '''