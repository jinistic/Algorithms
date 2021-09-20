import sys

read_input = sys.stdin.readline
N = int(read_input())
numbers = list(map(int, read_input().split()))
start = 0
end = N - 1
while True:
    mid = (start + end) // 2
    if start > mid:
        print(-1)
        break
    if numbers[mid] == mid:
        print(mid)
        break
    elif numbers[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1
