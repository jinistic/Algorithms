import heapq

INF = int(1e9)
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
X, K = map(int, input().split())

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      if dist + 1 < distance[i]:
        distance[i] = dist + 1
        heapq.heappush(q, (dist + 1, i))

dijkstra(1)
dist_1_to_K = distance[K]
distance = [INF] * (N + 1)
dijkstra(K)
dist_K_to_X = distance[X]
if dist_1_to_K == INF or dist_K_to_X == INF:
  print(-1)
else:
  print(dist_1_to_K + dist_K_to_X)