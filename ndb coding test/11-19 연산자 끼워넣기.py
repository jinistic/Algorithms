import sys

read_input = sys.stdin.readline
N = int(read_input())
numbers = list(map(int, read_input().split()))
add, sub, mul, div = map(int, read_input().split())
min_result = 1e9
max_result = -1e9

def dfs(i, now, add, sub, mul, div):
# def dfs(i, now):
    global min_result, max_result
    # global min_result, max_result, add, sub, mul, div
    if add > 0:
        dfs(i + 1, now + numbers[i], add - 1, sub, mul, div)  
        # add -= 1
        # dfs(i + 1, now + numbers[i])
        # add += 1

    if sub > 0:
        dfs(i + 1, now - numbers[i], add, sub - 1, mul, div)  
        # sub -= 1
        # dfs(i + 1, now - numbers[i])
        # sub += 1

    if mul > 0:
        dfs(i + 1, now * numbers[i], add, sub, mul - 1, div)  
        # mul -= 1
        # dfs(i + 1, now * numbers[i])
        # mul += 1

    if div > 0:
        dfs(i + 1, int(now / numbers[i]), add, sub, mul, div - 1)  
        # div -= 1
        # dfs(i + 1, int(now / numbers[i]))
        # div += 1

    if i == N:
        if now < min_result:
            min_result = now
        if now > max_result:
            max_result = now

dfs(1, numbers[0], add, sub, mul, div)
# dfs(1, numbers[0])
print(max_result)
print(min_result)

# from itertools import permutations
# import sys

# read_input = sys.stdin.readline
# N = int(read_input())
# numbers = list(map(int, read_input().split()))
# num_operators = list(map(int, read_input().split()))
# oper_list = []
# for i in range(4):
#     oper_list += [i] * num_operators[i]

# min_result = 1e9
# max_result = -1e9
# for perm in set(permutations(oper_list)):
#     temp = numbers[0]
#     for i in range(N - 1):
#         if perm[i] == 0:
#             temp += numbers[i + 1]
#         elif perm[i] == 1:
#             temp -= numbers[i + 1]
#         elif perm[i] == 2:
#             temp *= numbers[i + 1]
#         elif perm[i] == 3 and temp >= 0:
#             temp //= numbers[i + 1]
#         else:
#             temp = -(-temp // numbers[i + 1])
    
#     if temp < min_result:
#         min_result = temp

#     if temp > max_result:
#         max_result = temp

# print(max_result)
# print(min_result)
