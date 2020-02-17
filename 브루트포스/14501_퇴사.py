def dfs():
    global p, max_b, day, n
    for i in range(n):
        np = p[i]
        while

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
max_b = 0
dfs(-1, 0)
print(max_b)