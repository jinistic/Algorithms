def is_balanced(p):
    if p.count("(") == p.count(")"):
        return True
    else:
        return False


def is_right(p):
    if is_balanced(p):
        left = 0
        right = 0
        for i in p:
            if i == "(":
                left += 1
            else:
                right += 1

            if left < right:
                return False
        else:
            return True

    else:
        return False


def reverse(p):
    result = []
    for i in p:
        if i == "(":
            result.append(")")
        else:
            result.append("(")

    return "".join(result)


def solution(p):
    if is_right(p):
        return p
    else:
        for i in range(2, len(p) + 1):
            if is_balanced(p[:i]):
                u = p[:i]
                v = p[i:]
                break
        
        if is_right(u):
            return u + solution(v)
        else:
            return "(" + solution(v) + ")" + reverse(u[1:-1])
