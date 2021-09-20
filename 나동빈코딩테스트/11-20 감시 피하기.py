import sys
from itertools import combinations
from copy import deepcopy

read_input = sys.stdin.readline
N = int(read_input())
data = []
empty = []
teachers = []
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(N):
    row = read_input().split()
    data.append(row)
    for j in range(N):
        if row[j] == "X":
            empty.append((i, j))
        elif row[j] == "T":
            teachers.append((i, j))    


def move(temp_data, postition, temp_direction):
    x = postition[0] + temp_direction[0]
    y = postition[1] + temp_direction[1]
    if 0 <= x < N and 0 <= y < N:
        if temp_data[x][y] == "X":
            return move(temp_data, (x, y), temp_direction)
        elif temp_data[x][y] == "T" or temp_data[x][y] == "O":
            return False
        elif temp_data[x][y] == "S":
            return True
    else:
        return False


for comb in combinations(empty, 3):
    flag_hit = False
    temp = deepcopy(data)
    for c in comb:
        temp[c[0]][c[1]] = "O"

    for t in teachers:
        for i in range(4):
            if move(temp, (t[0], t[1]), direction[i]):
               flag_hit = True
               break 

        if flag_hit:
            break

    if not flag_hit:
        break
    
if flag_hit:
    print("NO")
else:
    print("YES")