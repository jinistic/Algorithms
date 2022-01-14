import sys
from collections import Counter, deque

"""
read_input = sys.stdin.readline

board = []
for _ in range(5):
    board.append(read_input().strip())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
results = []


def check(arr):  # arr = [(1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 4)]
    char = []
    for x, y in arr:
        char.append(board[x][y])
    return Counter(char)["S"] >= 4


def dfs(x, y, visited, party):
    visited[x][y] = True
    party.append((x, y))

    if len(party) == 7:
        if check(party) and sorted(party) not in results:
            results.append(sorted(party))
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue

        if visited[nx][ny]:
            continue

        dfs(nx, ny, visited, party)
        visited[nx][ny] = False
        party.pop()


def bfs(x, y):
    visited = [[False] * 5 for _ in range(5)]
    queue = deque()
    queue.append((x, y))
    # visited[x][y] = True
    # party = [(x, y)]
    party = []

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        party.append((x, y))

        if len(party) == 7 and check(party) and sorted(party) not in results:
            results.append(sorted(party))
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue

            if visited[nx][ny]:
                continue

            queue.append((nx, ny))
            # visited[nx][ny] = True
            # party.append((nx, ny))

            # if len(party) == 7:
            #     if check(party) and sorted(party) not in results:
            #         results.append(sorted(party))
            #         continue


for i in range(5):
    for j in range(5):
        visited = [[False] * 5 for _ in range(5)]
        party = []
        dfs(i, j, visited, party)
print(results)
print(len(results))


YYYYY
SYSYS
YYYYY
YSYYS
YYYYY
"""

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
    """
    def dfs(x, y, count):
        if count == 7:
            return True

        visited[x][y] = 1

        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue

            if visited[nx][ny]:
                continue

            if check[nx][ny]:
                return dfs(nx, ny, count + 1)

    return dfs(comb[0][0], comb[0][1], 1)
    """

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
