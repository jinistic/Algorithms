pos = input()
x = int(pos[1]) - 1
y = ord(pos[0]) - ord("a")
moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
count = 0
for dx, dy in moves:
  if 0 <= x + dx <= 7 and 0 <= y + dy <= 7:
    count += 1
print(count)