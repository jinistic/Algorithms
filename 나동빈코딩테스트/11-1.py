N = int(input())
fear_list = list(map(int, input().split()))
fear_list.sort()
count_groups = 0
count_members = 0

for f in fear_list:
    if count_members == f - 1:
        count_members = 0
        count_groups += 1
    elif count_members < f - 1:
        count_members += 1

print(count_groups)
