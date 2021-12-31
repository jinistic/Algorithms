import sys
from itertools import product

read_input = sys.stdin.readline

T = int(read_input())

for t in range(T):
    N = int(read_input())
    series = list(map(str, range(1, N + 1)))
    results = []

    for oper in product(("+", "-", " "), repeat=N - 1):
        math = series[0]

        for i, num in enumerate(series[1:]):
            math += oper[i] + num

        if eval(math.replace(" ", "")) == 0:
            results.append(math)

    for result in sorted(results):
        print(result)

    print()
