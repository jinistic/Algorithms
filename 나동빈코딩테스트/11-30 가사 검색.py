import bisect


def solution(words, queries):
    answer = []
    words_list_by_length = [[] for _ in range(10001)]
    words_list_by_length_reversed = [[] for _ in range(10001)]
    for word in words:
        words_list_by_length[len(word)].append(word)
        words_list_by_length_reversed[len(word)].append(word[::-1])
        
    for i in range(10001):
        words_list_by_length[i].sort()
        words_list_by_length_reversed[i].sort()

    for query in queries:
        n = len(query)
        if set(query) == {"?"}:
            answer.append(len(words_list_by_length[n]))
        elif query.endswith("?"):
            i = query.index("?")
            key = query[:i]
            j = bisect.bisect_left(words_list_by_length[n], key)
            k = bisect.bisect_left(words_list_by_length[n], key + "~")
            answer.append(k - j)
        elif query.startswith("?"):
            i = query.rindex("?")
            key = query[:i:-1]
            j = bisect.bisect_left(words_list_by_length_reversed[n], key)
            k = bisect.bisect_left(words_list_by_length_reversed[n], key + "~")
            answer.append(k - j)
            
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
 ["fro??", "????o", "fr???", "fro???", "pro?"]), [3, 2, 4, 1, 0])

# def solution(words, queries):
#     answer = []
#     words_list = {}
#     for word in words:
#         n = len(word)
#         for i in range(n - 1):
#             key1 = word[:i + 1] + "?" * (n - i - 1)
#             key2 = "?" * (i + 1) + word[i + 1:]
#             words_list[key1] = words_list.get(key1, 0) + 1
#             words_list[key2] = words_list.get(key2, 0) + 1

#         key3 = "?" * n
#         words_list[key3] = words_list.get(key3, 0) + 1

#     for query in queries:
#         answer.append(words_list.get(query, 0))

#     return answer

# print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
#  ["fro??", "????o", "fr???", "fro???", "pro?"]), [3, 2, 4, 1, 0])