import sys
import heapq

read_input = sys.stdin.readline
N = int(read_input())
cards = []
for _ in range(N):
    heapq.heappush(cards, int(read_input()))

cnt = 0
while len(cards) >= 2:
    i = heapq.heappop(cards)
    j = heapq.heappop(cards)
    heapq.heappush(cards, i + j)
    cnt += i + j

print(cnt)
