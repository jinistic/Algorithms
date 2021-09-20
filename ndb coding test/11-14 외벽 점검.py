from collections import deque
from itertools import permutations


def solution(n, weak, dist):
    m = len(weak)
    dist_between = []
    for i in range(m - 1):
        dist_between.append(weak[i + 1] - weak[i])
    
    dist_between.append(n + weak[0] - weak[-1])
    dist_between = dist_between + dist_between[:-2]
    result = set()
    for i in range(m):
        dist_cycle = dist_between[i:i + m - 1]
        for perm in permutations(dist, len(dist)):
            queue = deque(dist_cycle)
            cnt = 0
            flag_arrived = True
            for p in perm:
                temp = 0
                while queue:
                    temp += queue.popleft()
                    if p < temp:
                        cnt += 1
                        flag_arrived = False
                        break
                    else:
                        flag_arrived = True
                else:
                    flag_arrived = True                                    
            if flag_arrived:
                result.add(cnt + 1)
            else:
                result.add(-1)

    if max(result) == -1:
        return -1

    result.discard(-1)
    return min(result)

# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# print(solution(30, [0, 3, 11, 21], [4, 10]))
print(solution(200, [0, 99], [1, 2]))
print(solution(200, [0], [1, 2]))
