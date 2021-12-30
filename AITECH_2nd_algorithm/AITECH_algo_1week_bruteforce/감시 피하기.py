import sys
from itertools import combinations
from typing import List

read_input = sys.stdin.readline

boards = []
empty_spaces = []
N = int(read_input())

for i in range(N):
    row = read_input().split()
    for j in range(N):
        if row[j] == "X":
            empty_spaces.append((i, j))
    boards.append(row)


def chech_monitoring(array: List) -> bool():
    try:
        obs = array.index("O")
        return chech_monitoring(array[:obs]) and chech_monitoring(array[obs + 1 :])
    except:
        if "S" in array and "T" in array:
            return False
        else:
            return True


def check_rows(boards: List) -> bool():
    for row in boards:
        if not chech_monitoring(row):
            return False
    return True


def check_columns(boards: List) -> bool():
    for j in range(N):
        column = []
        for i in range(N):
            column.append(boards[i][j])
        if not chech_monitoring(column):
            return False
    return True


for comb in combinations(empty_spaces, 3):
    for i, j in comb:
        boards[i][j] = "O"
    if check_rows(boards) and check_columns(boards):
        print("YES")
        break
    for i, j in comb:
        boards[i][j] = "X"
else:
    print("NO")
