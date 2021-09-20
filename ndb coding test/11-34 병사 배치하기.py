# 가장 긴 증가하는 부분 수열 (LIS)
from bisect import bisect_left

N = int(input())
array = list(map(int,input().split()))
lis = []
for value in array:
    i = bisect_left(lis, value)
    if i == len(lis):
        lis.append(value)
    else:
        lis[i] = value

print(len(lis))





# import sys

# read_input = sys.stdin.readline
# N = int(read_input())
# array = list(map(int, read_input().split()))
# dp = [1] * N
# for i in range(1, N):
#     for j in range(i):
#         if array[j] > array[i]:
#             dp[i] = max(dp[i], dp[j] + 1)

# print(N - max(dp))
