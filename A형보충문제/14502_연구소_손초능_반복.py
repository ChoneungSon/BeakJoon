import copy, sys
def bfs(mat):
    global r, c, di, dj, sp, max_s
    q = copy.deepcopy(sp)
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + di[i]
            ny = y + dj[i]
            if 0 <= nx < r and 0 <= ny < c and mat[nx][ny] == 0:
                q.append((nx, ny))
                mat[nx][ny] = 2
    cnt = 0
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 0:
                cnt += 1
    if cnt > max_s:
        max_s = cnt

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
r, c = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
max_s, sp = 0, []
for i in range(r):
    for j in range(c):
        if arr[i][j] == 2:
            sp.append((i, j))
for i in range(r*c-2):
    if arr[i//c][i%c] == 0:
        for j in range(i+1, r*c-1):
            if arr[j//c][j%c] == 0:
                for k in range(j+1, r*c):
                    if arr[k//c][k%c] == 0:
                        for k1 in [i, j, k]:
                            arr[k1//c][k1%c] = 1
                        s = bfs(copy.deepcopy(arr))
                        for k1 in [i, j, k]:
                            arr[k1//c][k1%c] = 0
print(max_s)