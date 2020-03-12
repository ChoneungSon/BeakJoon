def choose(start, k, v):
    global n, cnt_chicken, m, used, Min, cnt_home, home
    if k == m:
        s = 0
        for i in range(cnt_home):
            s += find_short(v, home[i])
        if Min > s:
            Min = s
    else:
        for i in range(start, cnt_chicken):
            if used[i] == 0:
                used[i] = 1
                v[k] = i
                choose(i+1, k+1, v[:])
                used[i] = 0

def find_short(list_chicken, point):
    global cnt_chicken, chicken, m
    min_length = 100000
    for i in range(m):
        length = (abs(chicken[list_chicken[i]][0] - point[0]) + abs(chicken[list_chicken[i]][1] - point[1]))
        if length < min_length:
            min_length = length
    return min_length

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt_home, cnt_chicken = 0, 0
home, chicken = [], []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt_home += 1
            home.append((i, j))
        elif arr[i][j] == 2:
            cnt_chicken += 1
            chicken.append((i, j))
Min = 101
used = [0] * cnt_chicken
choose(0, 0, [0]*m)
print(Min)