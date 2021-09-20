N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
n0 = numbers[0]
n1 = numbers[1]
q = M // (K + 1)
r = M % (K + 1)
print(q * (K * n0 + n1) + r * n0)