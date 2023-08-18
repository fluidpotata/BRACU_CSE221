def adjList(inp):
    n, m = inp.readline().split()
    n, m = int(n), int(m)
    given = []
    for i in range(m):
        given.append([int(i) for i in inp.readline().split()])

    adjlist = [[] for a in range(n+1)]
    for j in range(len(given)):
        u, v, w = given[j]
        if w == 1:
            adjlist[u].append(w)
        else:
            if len(adjlist[u]) > 0:
                adjlist[u].append(tuple((v, w)))
            else:
                adjlist[u] = [tuple((v, w))]

    return adjlist


with open("input1.txt") as input_file, open("output1_b.txt", "w") as output_file:
    lst = adjList(input_file)
    for k in range(len(lst)):
        output_file.writelines(f"{k}: {' '.join(map(str, lst[k]))}")
        output_file.writelines('\n')


''' First we read the number of edges and vertices, then we create a list with length of (n+1). Each list contains None
or multiple tuple, None represents for no outgoing edge, each tuple represents outgoing edge, first element of the tuple
stands for destination node and second element is the weight.'''