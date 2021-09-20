# def solution(food_times, k):
#     flag_no_more_food = False
    
#     while not flag_no_more_food:
#         flag_no_more_food = True
#         for i, time in enumerate(food_times):
#             if time > 0:
#                 if k == 0:
#                     return i + 1
#                 food_times[i] -= 1
#                 k -= 1
#                 flag_no_more_food = False
    
#     return -1
import numpy
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    
    for i, time in enumerate(food_times):
        heapq.heappush(q, (time, i + 1))
    
    sum_time = 0
    prev_min_time = 0
    length = len(food_times)

    while sum_time + (q[0][0] - prev_min_time) * length <= k:
        print(sum_time, length, prev_min_time)
        min_time = heapq.heappop(q)[0]
        sum_time += (min_time - prev_min_time) * length
        length -= 1
        prev_min_time = min_time

    q.sort(key=lambda x: x[1])
    return q[(k - sum_time) % length][1]
    