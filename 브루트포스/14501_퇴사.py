def dfs(day, s):
    global p, max_b, n
    b_day = day
    a_day = day
    for i in range(n):
        if i >= day and i + p[i][0] <= n:
            a_day += p[i][0]
            s += p[i][1]
            dfs(i+p[i][0], s)
            s -= p[i][1]
    if b_day == a_day:
        if s > max_b:
            max_b = s

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
max_b = 0
dfs(0, 0)
print(max_b)