N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort(reverse=True)
for number in numbers:
  print(number, end=" ")