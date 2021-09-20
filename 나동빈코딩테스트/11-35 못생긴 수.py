n = int(input())
i2, i3, i5 = 0, 0, 0
next2, next3, next5 = 2, 3, 5
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    dp[i] = min(next2, next3, next5)
    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3
    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

print(dp[-1])



# from heapq import heappush, heappop

# n = int(input())
# multipliers = [2, 3, 5]
# dp = [1]
# count = 0
# while count < n:
#     i = heappop(dp)
#     count += 1
#     for m in multipliers:
#         if i * m not in dp:
#             heappush(dp, i * m)
    
# print(i)



# def ugly(i):
#     if i == 1:
#         return True

#     if i % 2 == 0:
#         return ugly(i // 2)
#     elif i % 3 == 0:
#         return ugly(i // 3)
#     elif i % 5 == 0:
#         return ugly(i // 5)
#     else:
#         return False

# n = int(input())
# i = 0
# count = 0
# while count < n:
#     i += 1
#     if ugly(i):
#         count += 1
    
# print(i)
