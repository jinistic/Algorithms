N = int(input())
dp = [0] * N
dp[0] = 1
dp[1] = 3

for i in range(2, N):
  dp[i] = (2 * dp[i - 2] + dp[i - 1]) % 796796

print(dp[-1])