S = input()
alphabets = []
sum_num = 0

for s in S:
    if s.isalpha():
        alphabets.append(s)
    else:
        sum_num += int(s)

print("".join(sorted(alphabets)) + str(sum_num))
