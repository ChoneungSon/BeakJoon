def rot(num):
    global d
    if num == 1:
        for i in range(len(d)):
            if d[i] == 1:
                d[i] = 6
            elif d[i] == 2:
                d[i] = 5
            elif d[i] == 5:
                d[i] = 1
            elif d[i] == 6:
                d[i] = 2
    else:
        for i in range(len(d)):
            if d[i] == 1:
                d[i] = 3
            elif d[i] == 2:
                d[i] = 4
            elif d[i] == 3:
                d[i] = 2
            elif d[i] == 4:
                d[i] = 1

def c_cube(num):
    if num == 1:
        rot(2)
    elif num == 2:
        for _ in range(3): rot(2)
    elif num == 3:
        rot(1)
    elif num == 4:
        for _ in range(3): rot(1)

cube = [0] * 6
d = [1, 6, 3, 4, 5, 2]
di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

r, c, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
orders = list(map(int, input().split()))
flag = 0
sp = [x, y]
for i in orders:
    np = [sp[0]+di[i], sp[1]+dj[i]]
    if 0 <= np[0] < r and 0 <= np[1] < c:
        c_cube(i)
        sp = np[:]
        if arr[np[0]][np[1]] == 0:
            for j in range(6):
                if d[j] == 2:
                    arr[np[0]][np[1]] = cube[j]
                    break
        else:
            for j in range(6):
                if d[j] == 2:
                    cube[j] = arr[np[0]][np[1]]
                    arr[np[0]][np[1]] = 0
                    break
        for j in range(6):
            if d[j] == 1:
                print(cube[j])
                break