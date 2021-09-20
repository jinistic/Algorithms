from collections import defaultdict

data = ["a", "b", "b", "c", "a", "b", "a", "b", "c", "e"]
ip = defaultdict(list)
for i, d in enumerate(data):
    ip[d].append(i)

print(ip)
for v in ip.values():
    if len(v) >= 4:
        print("4이상 index: ", v)
