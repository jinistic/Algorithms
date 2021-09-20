import sys

read_input = sys.stdin.readline
N = int(read_input())
students = []
for _ in range(N):
    name, kor, eng, math = read_input().split()
    students.append((name, int(kor), int(eng), int(math)))

for i in sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0])):
    print(i[0])
