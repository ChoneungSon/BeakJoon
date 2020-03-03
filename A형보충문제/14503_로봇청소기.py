import pprint
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
r, c = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
count, rot_cnt = 1, 0
arr[x][y] = 2
while 1:
    nx = x + di[(d+3)%4]
    ny = y + dj[(d+3)%4]
    rot_cnt += 1
    if arr[nx][ny] == 0:
        arr[nx][ny] = 2
        x, y = nx, ny
        d = (d+3) % 4
        rot_cnt = 0
        count += 1
    elif rot_cnt < 4:
        d = (d+3) % 4
    elif rot_cnt == 4:
        d = (d+3)%4
        x -= di[d]
        y -= dj[d]
        rot_cnt = 0
        if arr[x][y] == 1:
            break
print(count)