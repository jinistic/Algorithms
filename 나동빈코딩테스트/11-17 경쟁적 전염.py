from collections import deque
import sys

read_input = sys.stdin.readline
N, K = map(int, read_input().split())
data = [list(map(int, read_input().split())) for _ in range(N)]
S, X, Y = map(int, read_input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
virus = []

for i in range(N):
    for j in range(N):
        k = data[i][j]
        if k > 0:
            virus.append((k, i, j))

for _ in range(S):
    queue = deque(sorted(virus))
    virus = []
    while queue:
        k, x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 0:
                data[nx][ny] = k
                virus.append((k, nx, ny))
        
    if data[X - 1][Y - 1] != 0:
        break
    
print(data[X - 1][Y - 1])
