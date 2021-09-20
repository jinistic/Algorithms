N = int(input())
h, m, s = 0, 0, 0
result = 0
while h <= N:
  if "3" in str(h) + str(m) + str(s):
    result += 1
  s += 1
  if s == 60:
    s = 0
    m += 1
    if m == 60:
      m = 0
      h += 1
print(result)