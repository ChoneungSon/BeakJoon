def dfs(k, start, v):
    global arr, v_cnt, m, vi
    if k == m:
        bfs(v[:])
    else:
        for i in range(start, v_cnt):
            if used[i] == 0:
                used[i] = 1
                v[k] = i
                dfs(k+1, i+1, v[:])
                used[i] = 0

def bfs(list_vi):
    global arr, vi, n, m, min_length, road
    q, z_count, v_count, visit = [], 0, 0, [[0]*n for _ in range(n)]
    L = 0
    for i in range(m):
        q.append(vi[list_vi[i]] + [0])
        visit[vi[list_vi[i]][0]][vi[list_vi[i]][1]] = 1
    while q:
        x, y, l = q.pop(0)
        for i in range(4):
            nx, ny = x+di[i], y+dj[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    z_count += 1
                    visit[nx][ny] = 1
                    q.append([nx, ny, l+1])
                    L = l+1
                elif arr[nx][ny] == 2:
                    v_count += 1
                    visit[nx][ny] = 1
                    q.append([nx, ny, l+1])
    if min_length > L and z_count == road:
        min_length = L

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
vi, v_cnt, road = [], 0, 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            road += 1
        if arr[i][j] == 2:
            vi.append([i, j])
            v_cnt += 1
used, min_length = [0]*v_cnt, 2**32-1
dfs(0, 0, [0]*m)
if min_length == 2**32-1:
    print(-1)
else:
    print(min_length)