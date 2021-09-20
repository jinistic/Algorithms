def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
    
        if not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(nx, ny)


def dfs_diag(x, y):
    visited_diag[x][y] = True
    for i in range(8):
        nx = x + dx_diag[i]
        ny = y + dy_diag[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
    
        if not visited_diag[nx][ny] and graph[nx][ny] == 1:
            dfs_diag(nx, ny)


graph = [[1, 1, 0, 0], 
         [1, 1, 0, 0],
         [0, 0, 1, 1],
         [1, 0, 1, 1],
         [1, 0, 0, 0]]
m = len(graph)
n = len(graph[0])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dx_diag = [-1, -1, -1, 0, 0, 1, 1, 1]
dy_diag = [-1, 0, 1, -1, 1, -1, 0, 1]
visited = [[False] * n for _ in range(m)]
visited_diag = [[False] * n for _ in range(m)]
count = 0
count_diag = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            dfs(i, j)
            count += 1

        if not visited_diag[i][j] and graph[i][j] == 1:
            dfs_diag(i, j)
            count_diag += 1

print(count, count_diag)
