def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        sum_ddeok = sum([max(i - mid, 0) for i in arr])
        if sum_ddeok < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


N, M = map(int, input().split())
heights = list(map(int, input().split()))

heights.sort()
print(binary_search(heights, M, heights[0], heights[-1]))