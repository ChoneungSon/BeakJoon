r, c, t = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(r)]
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(r):
    if arr[i][0] == -1:
        up, down = [i, 0], [i+1, 0]
        break
for _ in range(t): # 시간에 대해 진행
    visit = [[0]*c for _ in range(r)]
    for i in range(r): # 먼지 있는 곳을 가서 퍼뜨림
        for j in range(c):
            if arr[i][j] > 0:
                count, dust = 0, []
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] != -1:
                        count += 1
                        dust.append((ni, nj))
                for k in range(count):
                    visit[dust[k][0]][dust[k][1]] += arr[i][j]//5
                arr[i][j] -= count * (arr[i][j] // 5)
    for i in range(r):
        for j in range(c):
            if visit[i][j] > 0:
                arr[i][j] += visit[i][j]
    x, y, dup, temp = up[0] + di[3], up[1] + dj[3], 3, 0 # 각 공기청정기 바람방향을 거꾸로 돌면서 위치를 최신화 시킴
    while 1:
        nx, ny = x + di[dup], y + dj[dup]
        if 0 <= nx <= up[0] and 0 <= ny < c:
            if arr[nx][ny] == -1:
                arr[x][y] = 0
                break
            else:
                temp = arr[nx][ny]
                arr[x][y], arr[nx][ny] = temp, 0
                x, y = nx, ny
        else:
            dup = (dup + 1) % 4
    x, y, ddown, temp = down[0] + di[1], down[1] + dj[1], 1, 0
    while 1:
        nx, ny = x + di[ddown], y + dj[ddown]
        if down[0] <= nx < r and 0 <= ny < c:
            if arr[nx][ny] == -1:
                arr[x][y] = 0
                break
            else:
                temp = arr[nx][ny]
                arr[x][y], arr[nx][ny] = temp, 0
                x, y = nx, ny
        else:
            ddown = (ddown + 3) % 4
cnt = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            cnt += arr[i][j]
print(cnt)