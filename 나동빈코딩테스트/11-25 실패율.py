def solution(N, stages):
    people_challenged = len(stages)
    failure_rate = [0] * (N + 2)
    for stage in stages:
        failure_rate[stage] += 1

    for i in range(1, N + 1):
        if people_challenged > 0:
            temp = failure_rate[i]
            failure_rate[i] /= people_challenged
            people_challenged -= temp
        else:
            break

    return [i[0] + 1 for i in sorted(enumerate(failure_rate[1:-1]), key=lambda x: (-x[1], x[0]))]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]	))
print(solution(4, [4, 4, 4, 4]	))


# def solution(N, stages):
#     fail = [[x+1] for x in range(N)]
#     sum_of_fail = 0
#     for i in range(N):
#         if sum_of_fail != len(stages):
#             failure_rate = stages.count(i+1) / (len(stages) - sum_of_fail)
#             sum_of_fail = sum_of_fail + stages.count(i+1)
#             fail[i].append(failure_rate)
#         else:
#             fail[i].append(0)
#     fail.sort(key=lambda x:x[1], reverse=True)
#     answer = [fail[i][0] for i in range(N)]
#     return answer