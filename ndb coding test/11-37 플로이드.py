import sys

read_input = sys.stdin.readline
n = int(read_input())
m = int(read_input())
INF = int(1e9)
graph = [[INF] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, read_input().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    
    print()
