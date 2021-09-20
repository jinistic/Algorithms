from collections import deque


def next(x, y, direction, board, N):
    result = []
    if direction == "h":
        if y - 1 >= 0 and board[x][y - 1] == 0:
            result.append((x, y - 1, "h"))
        if y + 2 < N and board[x][y + 2] == 0:
            result.append((x, y + 1, "h"))
        if x - 1 >= 0 and board[x - 1][y] == 0 and board[x - 1][y + 1] == 0:
            result.append((x - 1, y, "h"))
            result.append((x - 1, y, "v"))
            result.append((x - 1, y + 1, "v"))
        if x + 1 < N and board[x + 1][y] == 0 and board[x + 1][y + 1] == 0:
            result.append((x + 1, y, "h"))
            result.append((x, y, "v"))
            result.append((x, y + 1, "v"))
    else:
        if x - 1 >= 0 and board[x - 1][y] == 0:
            result.append((x - 1, y, "v"))
        if x + 2 < N and board[x + 2][y] == 0:
            result.append((x + 1, y, "v"))
        if y - 1 >= 0 and board[x][y - 1] == 0 and board[x + 1][y - 1] == 0:
            result.append((x, y - 1, "h"))
            result.append((x + 1, y - 1, "h"))
            result.append((x, y - 1, "v"))
        if y + 1 < N and board[x][y + 1] == 0 and board[x + 1][y + 1] == 0:
            result.append((x, y, "h"))
            result.append((x + 1, y, "h"))
            result.append((x, y + 1, "v"))

    return result


def solution(board):
    N = len(board)
    time = {(0, 0, "h"): 0}
    queue = deque([(0, 0, "h")])
    while queue:
        x, y, direction = queue.popleft()
        t = time[x, y, direction]
        for nx, ny, nd in next(x, y, direction, board, N):
            if time.get((nx, ny, nd)) == None:
                time[(nx, ny, nd)] = t + 1
                queue.append((nx, ny, nd))
            elif time[(nx, ny, nd)] > t + 1:
                time[(nx, ny, nd)] = t + 1

    ans1 = time.get((N - 2, N - 1, "v"), 0)
    ans2 = time.get((N - 1, N - 2, "h"), 0)
    if ans1 > 0 and ans2 > 0:
        return min(ans1, ans2)
    else:
        return max(ans1, ans2)


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]), 7)
print(solution([[0, 0, 0, 0, 0],[1, 1, 1, 0, 0],[0, 0, 0, 0, 0],[0, 0, 1, 1, 1],[0, 0, 0, 0, 0]]), 13)