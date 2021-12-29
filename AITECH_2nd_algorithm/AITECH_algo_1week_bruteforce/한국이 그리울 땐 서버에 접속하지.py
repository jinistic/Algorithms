import sys
from itertools import combinations

read_input = sys.stdin.readline

N = int(read_input())
left_pattern, right_pattern = read_input().split("*")
left_len, right_len = len(left_pattern), len(right_pattern)

for _ in range(N):
    file_name = read_input()
    if (
        len(file_name) >= left_len + right_len
        and file_name[:left_len] == left_pattern
        and file_name[-right_len:] == right_pattern
    ):
        print("DA")
    else:
        print("NE")
