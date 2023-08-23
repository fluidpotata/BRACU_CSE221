def adjList(inp):
    n , m = map(int, inp.readline().split())
    # print(n,m)
    given = [[] for i in range(n+1)]
    for i in range(m):
        u, v = map(int, inp.readline().split())
        given[u].append(v)

    # print(given)
    return n, given


def BFS(lst, start, path, visited):
    # visited[start] = 1
    queue.append(start)
    while queue:
        u = queue.pop(0)
        if visited[u]==0:
            visited[u]=1
            path.append(u)
        for j in lst[u]:
            queue.append(j)

    return path





with open("input1.txt") as input_file, open("output1.txt","w") as output_file:
    n, lst = adjList(input_file)
    # adjacency list
    output_file.writelines("Adjacency List:\n")
    for i in range(1,len(lst)):
        output_file.writelines(f"{i}: ")
        for j in lst[i]:
            output_file.writelines(f"{j} ")
        output_file.writelines("\n")

    # Part one
    in_degree = [0 for i in range(n+1)]
    for i in range(n+1):
        for j in lst[i]:
            in_degree[j]+=1

    # print(in_degree)

    queue = []
    queue2 = []
    for i in range(1, len(in_degree)):
        if in_degree[i]==0:
            queue.append(i)
            queue2.append(i)

    # print(queue)
    visited = [0 for i in range(n+1)]
    path = []
    while queue:
        u = queue.pop(0)
        if visited[u]==0:
            visited[u]=1
            path.append(u)
        for k in lst[u]:
            queue.append(k)

    # print(path)
    output_file.writelines("Before adding rule:\n")
    if 0 in visited[1:]:
        output_file.writelines("Cannot make route\n")
    else:
        output_file.writelines(' '.join(map(str, path)))
        output_file.writelines("\n")


    # Part two
    # path2 = []
    # visited2 = [0 for i in range(n + 1)]
    # for j in queue2:
    #     BFS(lst,j,path2, visited2)

    output_file.writelines("After adding rule:\n")
    if 0 in visited[1:]:
        output_file.writelines("Cannot make route")
    else:
        largest = path.pop(path.index(max(path)))
        path.append(largest)
        output_file.writelines(' '.join(map(str, path)))
        output_file.writelines("\n")
