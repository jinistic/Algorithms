import sys
import bisect

read_input = sys.stdin.readline
N, x = map(int, read_input().split())
numbers = list(map(int, read_input().split()))
i = bisect.bisect_left(numbers, x)
j = bisect.bisect_right(numbers, x)
if i == j:
    print(-1)
else:
    print(j - i)
    