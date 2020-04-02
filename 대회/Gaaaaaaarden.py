import sys
def dfs(m, cr, cg, count):
    global arr, r, c, limit, visit
    if limit < cr+cg+count: return
    elif cr == 0 and cg == 0:
        bfs()
    else:
        for i in range(m, r*c):
            if arr[i // c][i % c] == 2:
                dfs(i + 1, cr, cg, count+1)
                if cr:
                    visit[i] = 3
                    dfs(i+1, cr-1, cg, count+1)
                    visit[i] = 0
                if cg:
                    visit[i] = 4
                    dfs(i+1, cr, cg-1, count+1)
                    visit[i] = 0
                break

def bfs():
    global arr, r, c, max_cnt, di, dj, visit
    visited, q, cnt = [[0]*c for _ in range(r)], [], 0
    for i in range(r*c):
        if visit[i]:
            visited[i//c][i%c] = (visit[i], 0)
            q.append((i//c, i%c, visit[i], 0))
    while len(q):
        length = len(q)
        for _ in range(length):
            x, y, color, l = q.pop(0)
            if visited[x][y][0] != 1:
                for i in range(4):
                    nx, ny = x+di[i], y+dj[i]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != 0:
                        if visited[nx][ny]:
                            if visited[nx][ny][1] < l+1: continue
                            else:
                                if visited[nx][ny][0] == color: continue
                                elif visited[nx][ny][0] != 1:
                                    cnt += 1
                                    visited[nx][ny] = [1, 0]
                        else:
                            visited[nx][ny] = [color, l+1]
                            q.append((nx, ny, color, l+1))
    max_cnt = max(max_cnt, cnt)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
r, c, green, red = map(int, sys.stdin.readline().split())
arr, max_cnt, limit, visit = [list(map(int, sys.stdin.readline().split())) for _ in range(r)], 0, 0, [0]*(r*c)
for i in range(r*c):
    if arr[i//c][i%c] == 2: limit += 1
dfs(0, red, green, 0)
print(max_cnt)