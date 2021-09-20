N, M = map(int, input().split())
bowling_balls = list(map(int, input().split()))
weights = [0] * (M + 1)
count = 0

for i in bowling_balls:
    weights[i] += 1

for i in range(1, M + 1):
    N -= weights[i] 
    count += N * weights[i]

print(count)
    