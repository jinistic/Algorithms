def rotate_90(key):
    M = len(key)
    rotated_key = [[0] * M for _ in range(M)]

    for i in range(M):
        for j in range(M):
            rotated_key[i][j] = key[-j-1][i]
            
    return rotated_key


def check(key, lock):
    M = len(key)
    N = len(lock)
    zero_pad_lock = [[0] * (2 * M + N) for _ in range(2 * M + N)]

    for i in range(N):
        for j in range(N):
            zero_pad_lock[i + M][j + M] = lock[i][j]
    
    for i0 in range(M + N):
        for j0 in range(M + N):
            zero_pad_key = [[0] * (2 * M + N) for _ in range(2 * M + N)]
            for i in range(i0, i0 + M):
                for j in range(j0, j0 + M):
                    zero_pad_key[i][j] = key[i - i0][j - j0]

            flag_sum_one = True
            for i in range(M, M + N):
                for j in range(M, M + N):
                    if zero_pad_lock[i][j] + zero_pad_key[i][j] != 1:
                        flag_sum_one = False
                        break
                if not flag_sum_one:
                    break
            if flag_sum_one:
                return True
                
    return False


def solution(key, lock):
    M = len(key)
    N = len(lock)
    
    for _ in range(4):
        key = rotate_90(key)
        if check(key, lock):
            return True

    return False