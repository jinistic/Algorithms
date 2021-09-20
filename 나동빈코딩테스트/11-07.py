N = input()
half_length = len(N) // 2
left_part = N[:half_length]
right_part = N[half_length:]
sum_left = sum(map(int, left_part))
sum_right = sum(map(int, right_part))

if sum_left == sum_right:
    print("LUCKY")
else:
    print("READY")
