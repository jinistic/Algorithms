import sys

read_input = sys.stdin.readline
N = int(read_input())
dp = [0] * (N + 2)
current_max = 0
for i in range(1, N + 1):
    T, P = map(int, read_input().split())

    if dp[i] > current_max:
        current_max = dp[i]

    if i + T > N + 1:
        continue
    
    dp[i + T] = max(current_max + P, dp[i + T])

print(dp[-1])

# T = []
# P = []
# for _ in range(N):
#     t, p = map(int, read_input().split())
#     T.append(t)
#     P.append(p)
# 
# dp = [0] * (N + 1)
# current_max = 0
# for i in range(N - 1, -1, -1):
#     if i + T[i] <= N:
#         dp[i] = max(current_max, P[i] + dp[i + T[i]])
#         current_max = dp[i]
#     else:
#         dp[i] = current_max
# 
# print(dp[0])


# T = [0]
# P = [0]
# for _ in range(N):
#     t, p = map(int, read_input().split())
#     T.append(t)
#     P.append(p)
# 
# dp = [0] * (N + 1)
# for i in range(1, N + 1):
#     current_max = dp[i - 1]
#     for j in range(i - 4, i + 1):
#         if j <= 0:
#             continue
# 
#         if T[j] == i - j + 1:
#             current_max = max(current_max, dp[j - 1] + P[j])
# 
#     dp[i] = current_max
# 
# print(dp[-1])
