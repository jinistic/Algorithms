N = int(input())
moves = input().split()
dirs = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
x, y = 0, 0
for move in moves:
  dx, dy = dirs[move]
  nx, ny = x + dx, y + dy
  if 0 <= nx < N and 0 <= ny < N:
    x, y = nx, ny
print(x + 1, y + 1)