n = int(input())
num_a = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
arr = [[2]*(n+2)] + [[2]+[0]*n+[2] for _ in range(n)] + [[2]*(n+2)]
for _ in range(num_a):
    i, j = map(int, input().split())
    arr[i][j] = 1
arr[1][1] = 3
hp, ep = [1, 1], [1, 1]
d = 0
num_t = int(input())
turn = [0]*num_t

for i in range(num_t):
    time, direc = input().split()
    if direc == 'L':
        direc = (d+1) % 4
    else:
        direc = (d+3) % 4
    turn[i] = [int(time), direc]

count = 0
time, direc = turn.pop(0)

while 1:
    count += 1
    if count == time:
        d = direc
        if len(turn) != 0:
            time, direc = turn.pop(0)
    nhp = [hp[0] + di[d], hp[1] + dj[d]]
    if arr[nhp[0]][nhp[1]] == 1:
        arr[nhp[0]][nhp[1]] = 3
    elif arr[nhp[0]][nhp[1]] == 0:
        arr[ep[0]][ep[1]] = 0
        ep = [ep[0]+di[d], ep[1]+dj[d]]
        arr[nhp[0]][nhp[1]] = 3
    elif arr[nhp[0]][nhp[1]] == 3 or arr[nhp[0]][nhp[1]] == 2:
        print(count)
        break
    hp = nhp[:]