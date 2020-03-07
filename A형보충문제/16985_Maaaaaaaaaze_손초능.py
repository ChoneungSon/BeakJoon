def select(m, v):
    global choose
    if m == 5:
        choose.append(v[:])
    else:
        for i in range(5):
            if v[i] == -1:
                v[i] = m
                select(m+1, v[:])
                v[i] = -1

def rot(x):
    global arr
    rot_arr = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            rot_arr[i][j] = arr[x][4-j][i]
    arr[x] = rot_arr

def bfs(d):
    q = [(0, rotj[d], rotk[d], 1)]
    visit = [[[0]*5 for _ in range(5)] for _ in range(5)]
    while q:
        x, y, k, l = q.pop(0)
        if x == 4 and y == rotj[(d+2)%4] and k == rotk[(d+2)%4]:
            if l < min_length:
                min_length = l
        for i in range(6):
            nx, ny, nk = x+di[i], y+dj[i], k+dk[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nk < 5 and visit[nx][ny][nk] == 0:
                visit[nx][ny][nk] = 1
                q.append((nx, ny, nk, l+1))

di = [1, -1, 0, 0, 0, 0]
dj = [0, 0, 0, 1, 0, -1]
dk = [0, 0, 1, 0, -1, 0]
rotj = [0, 0, 4, 4]
rotk = [0, 4, 4, 0]
arr = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
choose = []
select(0, [-1]*5)

print(arr)