import sys
from itertools import combinations

read_input = sys.stdin.readline

N = int(read_input())
total_max_units = -float("inf")
person_number_with_max_units = 0

for person_number in range(1, N + 1):
    five_cards = list(map(int, read_input().split()))
    personal_max_units = -float("inf")

    for three_cards in combinations(five_cards, 3):
        units = sum(three_cards) % 10

        if units >= personal_max_units:
            personal_max_units = units

    if personal_max_units >= total_max_units:
        total_max_units = personal_max_units
        person_number_with_max_units = person_number

print(person_number_with_max_units)
