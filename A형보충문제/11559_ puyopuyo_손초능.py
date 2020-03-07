def bfs(x, y, color):
    global arr, r, c, di, dj
    cnt = 0
    q, visit = [(x, y)], [[0]*c for _ in range(r)]
    visit[x][y] = 1
    while q:
        x, y = q.pop(0)
        cnt += 1
        for i in range(4):
            nx, ny = x+di[i], y+dj[i]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == color and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append((nx, ny))
    if cnt >= 4:
        for i in range(r):
            for j in range(c):
                if visit[i][j]:
                    arr[i][j] = '.'
        return 1
    else:
        return 0

def sort_arr():
    global arr, r, c
    for i in range(c):
        for j in range(r-1, -1, -1):
            if arr[j][i] == '.':
                p = j
                while p > 0:
                    p -= 1
                    if arr[p][i] != '.':
                        arr[p][i], arr[j][i] = arr[j][i], arr[p][i]
                        break

r, c, total = 12, 6, 0
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
arr = [list(input()) for _ in range(r)]
while 1:
    count = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] != '.':
                count += bfs(i, j, arr[i][j])
    if count:
        sort_arr()
        total += 1
    else:
        break
print(total)