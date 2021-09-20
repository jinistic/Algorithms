N, M = map(int, input().split())
bowling_balls = list(map(int, input().split()))
count = 0

for i in range(len(bowling_balls) - 1):
    temp = bowling_balls[i]
    for j in range(i + 1, len(bowling_balls)):
        if bowling_balls[j] != temp:
            count += 1
    
print(count)
    