import sys
from collections import deque

read_input = sys.stdin.readline
N, L, R = map(int, read_input().split())
data = [list(map(int, read_input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global flag_union
    queue = deque([(x, y)])
    temp = [(x, y)]
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if L <= abs(data[x][y] - data[nx][ny]) <= R:
                queue.append((nx, ny))
                temp.append((nx, ny))
                visited[nx][ny] = True
                flag_union = True

    return temp


cnt = 0
flag_union = True
while flag_union:
    flag_union = False
    visited = [[False] * N for _ in range(N)]
    unions = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                temp = bfs(i, j)
                if len(temp) > 1:
                    unions.append(temp)
    
    for union in unions:
        people = sum([data[i][j] for i, j in union]) // len(union)
        for i, j in union:
            data[i][j] = people
    
    if flag_union:
        cnt += 1

print(cnt)


# import sys

# sys.setrecursionlimit(10**6)
# read_input = sys.stdin.readline
# N, L, R = map(int, read_input().split())
# data = [list(map(int, read_input().split())) for _ in range(N)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def dfs(x, y):
#     global flag_union
#     temp = [(x, y)]
#     visited[x][y] = True
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < N and 0 <= ny < N and \
#             not visited[nx][ny] and \
#             L <= abs(data[x][y] - data[nx][ny]) <= R:
#                 temp += dfs(nx, ny)
#                 flag_union = True

#     return temp


# cnt = 0
# flag_union = True
# while flag_union:
#     flag_union = False
#     visited = [[False] * N for _ in range(N)]
#     unions = []
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#                 temp = dfs(i, j)
#                 if len(temp) > 1:
#                     unions.append(temp)
    
#     for union in unions:
#         people = sum([data[i][j] for i, j in union]) // len(union)
#         for i, j in union:
#             data[i][j] = people
    
#     if flag_union:
#         cnt += 1

# print(cnt)
