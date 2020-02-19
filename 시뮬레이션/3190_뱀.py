import pprint
def c_dir(a):
    global d
    if a == 'D':
        d = 4 + (d+1) % 4
    else:
        d = 4 + (d+3) % 4

n = int(input())
num_a = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
arr = [[2]*(n+2)] + [[2]+[0]*n+[2] for _ in range(n)] + [[2]*(n+2)]
for _ in range(num_a):
    i, j = map(int, input().split())
    arr[i][j] = 1
arr[1][1] = 4
hp, ep = [1, 1], [1, 1]
d = 4
num_t = int(input())
turn = [0]*num_t

for i in range(num_t):
    time, direc = input().split()
    turn[i] = [int(time), direc]

count = 0
time, direc = turn.pop(0)

while 1:
    count += 1
    nhp = [hp[0] + di[d % 4], hp[1] + dj[d % 4]]
    if arr[nhp[0]][nhp[1]] == 0:
        bep = ep[:]
        ep[0] += di[arr[bep[0]][bep[1]] % 4]
        ep[1] += dj[arr[bep[0]][bep[1]] % 4]
        arr[bep[0]][bep[1]] = 0
    elif arr[nhp[0]][nhp[1]] > 1:
        print(count)
        break
    if count == time:
        c_dir(direc)
        if len(turn) != 0:
            time, direc = turn.pop(0)
    arr[nhp[0]][nhp[1]] = d
    hp = nhp[:]