import sys

read_input = sys.stdin.readline
T = int(read_input())
for _ in range(T):
    n, m = map(int, read_input().split())
    numbers = list(map(int, read_input().split()))
    gold = [numbers[i * m:(i + 1) * m] for i in range(n)]
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = gold[i][0]

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = gold[i][j] + max(               0, dp[i][j - 1], dp[i + 1][j - 1])
            elif i == n - 1:
                dp[i][j] = gold[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1],                0)
            else:
                dp[i][j] = gold[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])

    result = 0
    for i in range(n):
        result = max(result, dp[i][-1])

    print(result)