N, M = map(int, input().split())
x, y, d = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = 1
rotate = 0

while True:  
  nd = (d + 1) % 4
  d = nd
  dx, dy = direction[nd]
  nx, ny = x + dx, y + dy
  if nx < 0 or nx >= N or ny < 0 or ny >= M or \
  game_map[nx][ny] == 1 or game_map[nx][ny] == 2:
    rotate += 90
    if rotate == 360:
      nd = (d - 1) % 4
      dx, dy = direction[nd]
      nx, ny = x + dx, y + dy
      if game_map[nx][ny] == 1:
        break
      x, y = nx, ny
      d = (d + 1) % 4
      rotate = 0
      break    
    continue
  game_map[x][y] = 2
  x, y = nx, ny
  # d = nd
  count += 1
  rotate = 0

print(count)