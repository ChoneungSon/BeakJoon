import sys
s = 0
max_s = 0
for _ in range(4):
    m, p = map(int, sys.stdin.readline().split())
    s = s+p-m
    if s > max_s:
        max_s = s
print(max_s)