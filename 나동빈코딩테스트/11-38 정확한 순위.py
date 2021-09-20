import sys

read_input = sys.stdin.readline
n, m = map(int, read_input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, read_input().split())
    graph[a - 1][b - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = max(graph[i][j], graph[i][k] * graph[k][j])

count = 0
for i in range(n):
    row = sum(graph[i])
    col = 0
    for j in range(n):
        col += graph[j][i]

    if row + col == n - 1:
        count += 1

print(count)
