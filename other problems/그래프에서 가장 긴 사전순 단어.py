from pprint import pprint

def dfs(x, y, visited, count, words):
    visited[x][y] = True
    words += board[x][y]
    flag_end = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if visited[nx][ny]:
            continue

        if board[x][y] < board[nx][ny]:
            dfs(nx, ny, visited, count, words)
            visited[nx][ny] = False     # key part !!!
            flag_end = False
        elif board[x][y] > board[nx][ny] and count == 0:
            dfs(nx, ny, visited, count + 1, words)
            visited[nx][ny] = False     # key part !!!
            flag_end = False

    if flag_end:
        temp.append(words)


board = [["A", "B", "T", "T", "T"],
         ["T", "C", "D", "E", "T"],
         ["T", "T", "T", "F", "T"], 
         ["B", "A", "H", "G", "F"], 
         ["C", "D", "E", "F", "G"]]
N = len(board)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []
for i in range(N):
    for j in range(N):
        temp = []
        visited = [[False] * N for _ in range(N)]
        dfs(i, j, visited, 0, "")
        # answer.append(max(map(len, temp)))
        answer.append(sorted(temp, key=len)[-1])

# print(max(answer))
pprint(answer)
answer = sorted(answer, key=len, reverse=True)
print(len(answer[0]))
