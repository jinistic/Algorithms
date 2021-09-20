# import sys
# from bisect import bisect_left

# read_input = sys.stdin.readline
# N = int(read_input())
# array = list(map(int,read_input().split()))
# lis = [array[0]]
# for value in array:
#     if value > lis[-1]:
#         lis.append(value)
#     else:
#         lis[bisect_left(lis, value)] = value

# print(len(lis))

# 수열 길이 개수는 맞았지만, 수열 자체는 다르다.
# for i in lis:
#     print(i, end=" ")    # 결과 틀림


import sys

read_input = sys.stdin.readline
N = int(read_input())
array = list(map(int, read_input().split()))
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            