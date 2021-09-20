from collections import deque
import sys

read_input = sys.stdin.readline
N, M, K, X = map(int, read_input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, read_input().split())
    graph[i].append(j)

visited = [False] * (N + 1)
dist = [0] * (N + 1)
result = []
queue = deque([X])
visited[X] = True
while queue:
    node = queue.popleft()
    for i in graph[node]:
        if not visited[i]:
            dist[i] = dist[node] + 1
            visited[i] = True
            if dist[i] == K:
                result.append(i)
            else:
                queue.append(i)

if result:
    for i in sorted(result):
        print(i)
else:
    print(-1)
