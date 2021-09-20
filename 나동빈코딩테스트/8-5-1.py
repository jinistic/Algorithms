def search_from_the_biggest(arr, value, count):
  if arr == []:
    return -1
  q = value // arr[-1]
  for i in range(q + 1):
    if value % arr[-1] == 0:
      return count + q
    result = search_from_the_biggest(arr[:-1], value - (q - i) * arr[-1], count + (q - i))
    if result != -1:
      return result
  return -1
    

N, M = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort()

print(search_from_the_biggest(coins, M, 0))