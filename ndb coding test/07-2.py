import sys

def binary_search(arr, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if arr[mid] == target:
    return mid
  elif arr[mid] > target:
    return binary_search(arr, target, start, mid - 1)
  else:
    return binary_search(arr, target, mid + 1, end)

input_data = sys.stdin.readline

N = int(input())
inventory = list(map(int, input_data().split()))
M = int(input())
request = list(map(int, input_data().split()))
inventory.sort()

for r in request:
  if binary_search(inventory, r, 0, N - 1) == None:
    print("no", end=" ")
  else:
    print("yes", end=" ") 