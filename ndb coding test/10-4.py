from collections import deque
import copy

N = int(input())
indegree = [0] * (N + 1)
course_time = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
  inputs = list(map(int, input().split()))
  course_time[i] = inputs[0]
  for x in inputs[1:-1]:
    indegree[i] += 1
    graph[x].append(i)

result = copy.deepcopy(course_time)

def topology_sort():
  q = deque()
  
  for i in range(1, N + 1):
    if indegree[i] == 0:
      q.append(i)
    
  while q:
    now = q.popleft()
    for i in graph[now]:
      result[i] = max(result[i], result[now] + course_time[i])
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
      
topology_sort()

for i in range(1, N + 1):
  print(result[i])