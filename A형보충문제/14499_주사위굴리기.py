import sys
def rot(d):
    global direc
    if d == 1: # 오른쪽으로 돌리기
        for i in range(6):
            if direc[i] == 0:
                direc[i] = 2
            elif direc[i] == 1:
                direc[i] = 3
            elif direc[i] == 2:
                direc[i] = 1
            elif direc[i] == 3:
                direc[i] = 0
    else: # 위쪽으로 돌리기
        for i in range(6):
            if direc[i] == 0:
                direc[i] = 5
            elif direc[i] == 1:
                direc[i] = 4
            elif direc[i] == 4:
                direc[i] = 0
            elif direc[i] == 5:
                direc[i] = 1

di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

r, c, i, j, k = map(int, sys.stdin.readline().split())
sp = [i, j]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
cube = [0]*6
direc = [0, 1, 2, 3, 4, 5]
c_list = list(map(int, sys.stdin.readline().split()))
for i in range(k):
    p = [sp[0]+di[c_list[i]], sp[1]+dj[c_list[i]]]
    if 0 <= p[0] < r and 0 <= p[1] < c:
        if c_list[i] == 1:
            rot(1)
        elif c_list[i] == 2:
            for _ in range(3):
                rot(1)
        elif c_list[i] == 3:
            rot(2)
        elif c_list[i] == 4:
            for _ in range(3):
                rot(2)
        sp = p[:]
        for j in range(6):
            if arr[sp[0]][sp[1]] == 0 and direc[j] == 1:
                arr[sp[0]][sp[1]] = cube[j]
            elif arr[sp[0]][sp[1]] != 0 and direc[j] == 1:
                cube[j] = arr[sp[0]][sp[1]]
                arr[sp[0]][sp[1]] = 0
            if direc[j] == 0:
                print(cube[j])