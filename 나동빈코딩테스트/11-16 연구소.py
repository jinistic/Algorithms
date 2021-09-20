from collections import deque
from itertools import combinations
from copy import deepcopy
import sys

read_input = sys.stdin.readline
N, M = map(int, read_input().split())
data = [list(map(int, read_input().split())) for _ in range(N)]
empty, virus = [], []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            empty.append((i, j))
        elif data[i][j] == 2:
            virus.append((i, j))


def disjoint(xy):
    x, y = xy
    result = []
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            result.append((nx, ny))
    
    return result


def infect(v, d):
    queue = deque([v])
    while queue:
        now = queue.popleft()
        for i, j in disjoint(now):
            if d[i][j] == 0:
                d[i][j] = 2
                queue.append((i, j))


result = []
for comb in combinations(empty, 3):
    data_walls_added = deepcopy(data)
    for i, j in comb:
        data_walls_added[i][j] = 1

    for v in virus:
        infect(v, data_walls_added)

    cnt = 0
    for row in data_walls_added:
        cnt += row.count(0)

    result.append(cnt)

print(max(result))
