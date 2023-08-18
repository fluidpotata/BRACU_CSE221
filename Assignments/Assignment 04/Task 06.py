def flood_fill(R, H, grid):
    max_diamonds = 0
    for i in range(R):
        for j in range(H):
            if grid[i][j] != '#':
                diamonds = bfs(grid, i, j, R, H)
                max_diamonds = max(max_diamonds, diamonds)
    return max_diamonds

def bfs(grid, x, y, R, H):
    diamonds = 0
    visited = [[0 for i in range(H)] for j in range(R)]
    queue = [x * H + y]
    while queue:
        u = queue.pop(0)
        ux, uy = u // H, u % H
        if visited[ux][uy]==1:
            continue
        visited[ux][uy] = 1
        if grid[ux][uy] == 'D':
            diamonds += 1
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = ux + dx, uy + dy
            if 0 <= nx < R and 0 <= ny < H and not visited[nx][ny] and grid[nx][ny] != '#':
                queue.append(nx * H + ny)
    return diamonds

with open("input6.txt") as inputfile, open("output6.txt","w") as outfile:
    r,h = map(int,inputfile.readline().split())
    grid = []
    for i in range(r):
        row = inputfile.readline().rstrip()
        grid.append(row)

    print(grid)
    maxd = flood_fill(r,h,grid)
    outfile.writelines(str(maxd))