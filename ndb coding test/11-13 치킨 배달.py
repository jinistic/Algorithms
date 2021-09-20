from itertools import combinations

N, M = map(int, input().split())
data = [input().split() for _ in range(N)]
house = []
chicken = []
chicken_dist = []
result = []
for i in range(N):
    for j in range(N):
        if data[i][j] == "1":
            house.append((i, j))
        elif data[i][j] == "2":
            chicken.append((i, j))

for c in chicken:
    temp_dist = []
    for h in house:
        temp_dist.append(abs(h[0] - c[0]) + abs(h[1] - c[1]))
    chicken_dist.append(temp_dist)

for co in combinations(range(len(chicken)), M):
    result.append(sum(map(min, zip(*[chicken_dist[i] for i in co]))))
            
print(min(result))
