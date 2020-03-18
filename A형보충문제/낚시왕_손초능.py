import sys, copy, pprint
def catch(x):
    global arr, r, c
    for i in range(r):
        if arr[i][x]:
            temp, arr[i][x] = arr[i][x][4], 0
            return temp
    return 0

def move():
    global arr, r, c
    visit = [0] * (r*c)
    v = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j]:
                if arr[i][j][0] or arr[i][j][1]:
                    arr[i][j][2] = (arr[i][j][2] + arr[i][j][0]) % (2*r - 2)
                    arr[i][j][3] = (arr[i][j][3] + arr[i][j][1]) % (2*c - 2)
                if visit[dr[arr[i][j][2]]*c + dc[arr[i][j][3]]] < arr[i][j][4]:
                    visit[dr[arr[i][j][2]]*c + dc[arr[i][j][3]]] = arr[i][j][4]
                    v[dr[arr[i][j][2]]][dc[arr[i][j][3]]] = arr[i][j][:]
    return v

di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]
r, c, num = map(int, sys.stdin.readline().split())
arr = [[0]*c for _ in range(r)]
total = 0
dr = list(map(int, range(r))) + list(map(int, range(r-2, 0, -1)))
dc = list(map(int, range(c))) + list(map(int, range(c-2, 0, -1)))
for _ in range(num):
    x, y, v, d, big = map(int, sys.stdin.readline().split())
    arr[x-1][y-1] = [v*di[d-1], v*dj[d-1], x-1, y-1, big]
total += catch(0)
for i in range(1, c):
    arr = move()
    total += catch(i)
print(total)