words1 = input()
words2 = input()
dp = [0] * len(words2)
for i in range(len(words1)):
    max_dp = 0
    for j in range(len(words2)):
        if max_dp < dp[j]:    
            max_dp = dp[j]
        elif words1[i] == words2[j]:
            dp[j] = max_dp + 1

print(max(dp))
