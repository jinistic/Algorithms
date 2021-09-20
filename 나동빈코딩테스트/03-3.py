N, M = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(N)]
answer = max([min(row) for row in numbers])
print(answer)