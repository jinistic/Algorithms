from collections import deque

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]
for _ in range(K):
    row, col= map(int, input().split())
    board[row - 1][col - 1] = "apple"

L = int(input())
i, j = 0, 0
tail = deque([(i, j)])
cnt = 0
direction = (0, 1)
rotate_L = {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1)}
rotate_D = {(0, 1): (1, 0), (-1, 0): (0, 1), (0, -1): (-1, 0), (1, 0): (0, -1)}
game_end = False
for _ in range(L):
    inputs = input().split()
    X = int(inputs[0])
    C = inputs[1]
    for t in range(cnt + 1, X + 1):
        i += direction[0]
        j += direction[1]
        if i < 0 or i >= N or j < 0 or j >= N or board[i][j] == 1:
            print(t)
            game_end = True
            break

        tail.append((i, j))
        # apple 아니라면 tail 삭제
        if board[i][j] == 0:
            i_tail, j_tail = tail.popleft()
            board[i_tail][j_tail] = 0

        board[i][j] = 1

    if game_end:
        break

    cnt = X

    if C == "L":
        direction = rotate_L[direction]
    else:
        direction = rotate_D[direction]
# 현재 방향으로 끝날 때까지 진행
else:
    while True:
        cnt += 1
        i += direction[0]
        j += direction[1]
        if i < 0 or i >= N or j < 0 or j >= N or board[i][j] == 1:
            print(cnt)
            break

        tail.append((i, j))
        # apple 아니라면 tail 삭제
        if board[i][j] == 0:
            i_tail, j_tail = tail.popleft()
            board[i_tail][j_tail] = 0
            
        board[i][j] = 1
