import sys
from heapq import heappop, heappush

def dijkstra(start):
    q = [(0, start)]
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heappush(q, (cost, i))


INF = int(1e9)
read_input = sys.stdin.readline
N, M = map(int, read_input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, read_input().split())
    graph[A].append(B)
    graph[B].append(A)

distance = [INF] * (N + 1)
dijkstra(1)
max_dist = max(distance[1:])
print(distance[1:].index(max_dist) + 1, max_dist, distance[1:].count(max_dist))
