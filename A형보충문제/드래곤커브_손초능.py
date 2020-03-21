import sys
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
n = int(sys.stdin.readline())
arr = [[0]*101 for _ in range(101)]
for _ in range(n): # 원리를 생각해보면, 이전 이동하는 회전 방향들을 최초에 왼쪽으로 회전한 뒤, 그것들의 반대로 회전하면서 직선을 그려나감 
    y, x, d, g = map(int, sys.stdin.readline().split())
    nx, ny = x+di[d], y+dj[d]
    arr[x][y], arr[nx][ny] = 1, 1
    count, v = 0, []
    while count < g:
        count += 1
        add_root = [0] * (len(v)+1)
        add_root[0] = 1
        for i in range(len(v)):
            add_root[i+1] = -v[len(v)-1-i]
        for i in range(len(v)+1):
            d = (d + add_root[i]) % 4
            nx += di[d]; ny += dj[d]
            arr[nx][ny] = 1
        v += add_root
cnt = 0
for i in range(100):
    for j in range(100):
        for k in range(4):
            if arr[i+k//2][j+k%2] == 0:
                break
        else:
            cnt += 1
print(cnt)