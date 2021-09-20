from collections import deque

N, M = map(int, input().split())
graph = []

for _ in range(N):
  temp = []
  row = input()
  for r in row:
    temp.append(int(r))
  graph.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([(0, 0)])

while queue:
  x, y = queue.popleft()
  if (x, y) == (N - 1 , M - 1):
    break
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
      queue.append((nx, ny))
      graph[nx][ny] = graph[x][y] + 1

print(graph[-1][-1])