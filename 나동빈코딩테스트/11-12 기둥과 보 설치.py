def check(x, y, a, result):
    if a == 0:
        if y == 0 or \
          [x - 1, y, 1] in result or \
          [x, y, 1] in result or \
          [x, y - 1, 0] in result:
            return True
    else:
        if [x, y - 1, 0] in result or \
           [x + 1, y - 1, 0] in result or \
          ([x - 1, y, 1] in result and [x + 1, y, 1] in result):
            return True

    return False


def solution(n, build_frame):
    result = []
    for x, y, a, b in build_frame:
        if b == 1:         
            if check(x, y, a, result):
                result.append([x, y, a])
        else:
            result.remove([x, y, a])
            if a == 0:   
                if [x - 1, y + 1, 1] in result and not check(x - 1, y + 1, 1, result) or \
                   [x, y + 1, 0] in result and not check(x, y + 1, 0, result) or \
                   [x, y + 1, 1] in result and not check(x, y + 1, 1, result):
                    result.append([x, y, a])
            else:
                if [x - 1, y, 1] in result and not check(x - 1, y, 1, result) or \
                   [x, y, 0] in result and not check(x, y, 0, result) or \
                   [x + 1, y, 0] in result and not check(x + 1, y, 0, result) or \
                   [x + 1, y, 1] in result and not check(x + 1, y, 1, result):    
                    result.append([x, y, a])

    return sorted(result)
