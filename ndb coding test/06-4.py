N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
count = 0
for i in range(N):
  if A[i] < B[i]:
    A[i] = B[i]
    count += 1
    if count == K:
      break
  else:
    break
print(sum(A))