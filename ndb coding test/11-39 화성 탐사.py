import sys
from heapq import heappop, heappush

def next(x, y):
    result = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            result.append((nx, ny))
    
    return result


def dijkstra(start):
    i, j = start
    q = []
    heappush(q, (graph[i][j], start))
    cost[i][j] = graph[i][j]
    while q:
        c, (x, y) = heappop(q)
        if cost[x][y] < c:
            continue

        for nx, ny in next(x, y):
            temp = c + graph[nx][ny]
            if temp < cost[nx][ny]:
                cost[nx][ny] = temp
                heappush(q, (temp, (nx, ny)))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = int(1e9)
read_input = sys.stdin.readline
T = int(read_input())
for _ in range(T):
    N = int(read_input())
    graph = [list(map(int, read_input().split())) for _ in range(N)]
    cost = [[INF] * N for _ in range(N)]
    dijkstra((0, 0))
    print(cost[-1][-1])
