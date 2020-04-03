import sys, pprint
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
c, r = map(int, sys.stdin.readline().split())
arr = [[-1]*(c+2)]+[[-1]+list(map(int, sys.stdin.readline().split()))+[-1] for _ in range(r)]+[[-1]*(c+2)]
cnt, q, rear, front = 0, [0]*(r*c), -1, -1
for i in range(1, r+1):
    for j in range(1, c+1):
        if arr[i][j] == 0: cnt += 1
        elif arr[i][j] == 1:
            rear += 1
            q[rear] = i, j
if cnt == 0: print(0)
else:
    tot = 0
    while rear != front:
        front += 1
        x, y = q[front]
        for i in range(4):
            nx, ny = x+di[i], y+dj[i]
            if arr[nx][ny] == 0:
                rear += 1
                q[rear] = (nx, ny)
                arr[nx][ny] = arr[x][y] + 1
                t = arr[x][y]; tot += 1
    if cnt != tot: print(-1)
    else: print(t)