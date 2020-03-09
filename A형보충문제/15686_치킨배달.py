def choose(k):
    global n, cnt_chicken, m
    if k == m:
        pass
    else:
        for i in range(cnt_chicken):
           if visit[i] == -1:
               visit[i] = i

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
visit = [0] * cnt_chicken
choose(0)