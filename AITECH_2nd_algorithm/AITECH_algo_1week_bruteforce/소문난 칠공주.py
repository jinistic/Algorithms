import sys
from collections import deque
from itertools import combinations

graph = []
location = []
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def check_connection(comb):
    check = [[False] * 5 for _ in range(5)]
    visited = [[False] * 5 for _ in range(5)]
    for x, y in comb:
        check[x][y] = True

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True
        count = 1

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                    continue

                if visited[nx][ny]:
                    continue

                if check[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1

                if count == 7:
                    return True

        return False

    return bfs(comb[0][0], comb[0][1])


def check_more_s(comb):
    count = 0
    for x, y in comb:
        if graph[x][y] == "S":
            count += 1
    return count >= 4


for i in range(5):
    graph.append(sys.stdin.readline().rstrip())
    for j in range(5):
        location.append((i, j))

answer = 0
combs = combinations(location, 7)
for comb in combs:
    if check_more_s(comb) and check_connection(comb):
        answer += 1
print(answer)
