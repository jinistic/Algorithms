def queen(i, col, diag1, diag2):
    global count
    if i == n:
        count += 1
        return

    for j in range(n):
        if j in col or (i + j) in diag1 or (i - j) in diag2:
            continue

        col.add(j)
        diag1.add(i + j)
        diag2.add(i - j)
        queen(i + 1, col, diag1, diag2)
        col.remove(j)
        diag1.remove(i + j)
        diag2.remove(i - j)


n = int(input())
col, diag1, diag2 = set(), set(), set()
count = 0
queen(0, col, diag1, diag2)
print(count)


# def queen(col):
#     global count
#     row = len(col)
#     if row == n:
#         count += 1
#         return

#     for j in range(n):
#         if j in col:
#             continue

#         for i in range(row):
#             if row - i == abs(j - col[i]):
#                 break
#         else:
#             queen(col + [j])


# n = int(input())
# global count
# count = 0
# for i in range(n):
#     queen([i])

# print(count)
