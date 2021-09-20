import heapq
import sys

INF = int(1e9)
my_input = sys.stdin.readline
N, M, C = map(int, my_input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
  a, b, c = map(int, my_input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  
dijkstra(C)
count = 0 
max_time = 0

for d in distance:
  if 0 < d < INF:
    count += 1
    if d > max_time:
      max_time = d

print(count, max_time)
