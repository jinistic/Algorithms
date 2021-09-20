N = int(input())
array = [input().split() for _ in range(N)]
array.sort(key=lambda x: int(x[1]))
for arr in array:
  print(arr[0], end=" ")