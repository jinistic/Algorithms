words1 = input()
words2 = input()
n1 = len(words1)
n2 = len(words2)
dp = [0] * n2
for i in range(n1):
    max_dp = 0
    for j in range(n2):
        if max_dp < dp[j]:    
            max_dp = dp[j]
        elif words1[i] == words2[j]:
            dp[j] = max_dp + 1

print(max(n1, n2) - max(dp))
