from collections import deque

N, M = map(int, input().split())
ice = []

for _ in range(N):
  temp = []
  row = input()
  for r in row:
    temp.append(int(r))
  ice.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

for i in range(N):
  for j in range(M):
    if ice[i][j] == 0:
      queue = deque([(i, j)])
      ice[i][j] = 1
      count += 1
      while queue:
        x, y = queue.popleft()
        for k in range(4):
          nx = x + dx[k]
          ny = y + dy[k]
          if 0 <= nx < N and 0 <= ny < M and ice[nx][ny] == 0:
            queue.append((nx, ny))
            ice[nx][ny] = 1
print(count)