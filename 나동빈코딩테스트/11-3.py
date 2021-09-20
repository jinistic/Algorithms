S = input()
consecutive_number = int(S[0])
count = 0

for s in S[1:]:
    i = int(s)
    if consecutive_number != i:
        consecutive_number = i
        count += 1

print((count + 1) // 2)