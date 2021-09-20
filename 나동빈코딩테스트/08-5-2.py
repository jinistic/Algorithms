N, M = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort()
dp = [-1] * 10001

for coin in coins:
  dp[coin] = 1
  for i in range(coin + 1, M + 1):
    if dp[i - coin] != -1:
      dp[i] = dp[i - coin] + 1
      
print(dp[M])