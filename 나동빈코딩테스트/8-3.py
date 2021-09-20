N = int(input())
numbers = list(map(int, input().split()))
dp = [0] * N
dp[0] = numbers[0]
dp[1] = max(dp[0], numbers[1])

for i in range(2, N):
  dp[i] = max(dp[i - 1], dp[i - 2] + numbers[i])

print(dp[-1])