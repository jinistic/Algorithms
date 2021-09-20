def solution(s):
    if len(s) == 1:
        min_length = 1
    else:
        min_length = 9999
    for i in range(1, len(s)//2+1):
        length = 0
        count = 1
        for j in range(0, len(s), i):
            if s[j:j+i] == s[j+i:j+2*i]:
                count += 1
            else:
                if count > 1:
                    length += len(str(count)) + len(s[j:j+i])
                    count = 1
                else:
                    length += len(s[j:j+i])
        if length < min_length:
            min_length = length
    return min_length   


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))