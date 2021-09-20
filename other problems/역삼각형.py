import sys
from itertools import chain

read_input = sys.stdin.readline
N = int(read_input())
data = [[0] * (N - i) for i in range(N)]
row = -1
col = N
num = 1
for i in range(N):
    for _ in range(N - i):
        if i % 3 == 0:
            row += 1
            col -= 1
        elif i % 3 == 1:
            row -= 1
        elif i % 3 == 2:
            col += 1

        data[row][col] = num
        num += 1

for i in range(N):
    for j in range(N - i):
        print(data[i][j], end=" ")

    print()

print(list(chain(*data)))