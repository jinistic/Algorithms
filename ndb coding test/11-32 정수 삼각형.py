def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                left_up = 0
            else:
                left_up = triangle[i - 1][j - 1]
            if j == i:
                right_up = 0
            else:
                right_up = triangle[i - 1][j]
            
            triangle[i][j] += max(left_up, right_up)

    return max(triangle[-1])
