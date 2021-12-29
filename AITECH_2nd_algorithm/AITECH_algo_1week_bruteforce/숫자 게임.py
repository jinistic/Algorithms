import sys
from itertools import combinations

read_input = sys.stdin.readline

N = int(read_input())
total_max_units = -float("inf")
per_num_with_max_units = 0

for per_num in range(1, N + 1):
    five_cards = list(map(int, read_input().split()))
    per_max_units = -float("inf")

    for three_cards in combinations(five_cards, 3):
        units = sum(three_cards) % 10

        if units >= per_max_units:
            per_max_units = units

    if per_max_units >= total_max_units:
        total_max_units = per_max_units
        per_num_with_max_units = per_num

print(per_num_with_max_units)
