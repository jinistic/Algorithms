import sys
import bisect

read_input = sys.stdin.readline
N, C = map(int, read_input().split())
houses = [int(read_input()) for _ in range(N)]
houses.sort()

start = 1
end = houses[N - 1] - houses[0]
while True:
    if start > end:
        break

    mid = (start + end) // 2
    next_index = 0
    count = 1
    # installed_pos = houses[0]
    # for i in range(1, N):
    #     if houses[i] >= installed_pos + mid:
    #         installed_pos = houses[i]
    #         count += 1
    
    # if count >= C:
    #     result = mid
    #     start = mid + 1
    # else:
    #     end = mid - 1
    
    max_disjoint_dist = 1e9
    while count < C:
        installed_pos = houses[next_index]
        next_index = bisect.bisect_left(houses, installed_pos + mid) 
        if next_index == N:
            end = mid - 1
            break

        if houses[next_index] > installed_pos + mid:
            max_disjoint_dist = min(max_disjoint_dist, houses[next_index] - installed_pos)
        else:
            max_disjoint_dist = mid

        count += 1
    else:
        result = max_disjoint_dist
        start = mid + 1
    
print(result)
