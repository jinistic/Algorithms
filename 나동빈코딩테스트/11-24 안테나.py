import sys

read_input = sys.stdin.readline
N = int(read_input())
houses = list(map(int, read_input().split()))
houses.sort()
print(houses[(N - 1) // 2])