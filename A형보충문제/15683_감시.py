import sys, copy
def find(p, num, A):
    global arr, r, c
    min_count = 65
    if num == 1:
        rot = 1
    elif num == 2 or num == 3:
        rot = 2
    elif num == 4:
        rot = 3
    elif num == 5:
        rot = 4
    for i in range(len(dir_list[num-1])):
        copy_A = copy.deepcopy(A)
        count = 0
        for j in range(rot):
            np = p[:]
            while 1:
                np[0] += di[dir_list[num-1][i][j]]
                np[1] += dj[dir_list[num-1][i][j]]
                if 0 <= np[0] < r and 0 <= np[1] < c and copy_A[np[0]][np[1]] != 6:
                    copy_A[np[0]][np[1]] = 7
                else:
                    break
        for k in range(r):
            for m in range(c):
                if copy_A[k][m] == 0:
                    count += 1
        if count < min_count:
            min_count = count
            arr = copy.deepcopy(copy_A)
    return min_count

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
dir_list = [
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]
r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
cctv = []
m_count = 0
for i in range(r):
    for j in range(c):
        if 0 < arr[i][j] < 6:
            cctv.append([i, j, arr[i][j]])
for i in range(len(cctv)-1):
    for j in range(i+1, len(cctv)):
        if cctv[j-1][2] < cctv[j][2]:
            cctv[j-1], cctv[j] = cctv[j][:], cctv[j-1][:]
for i in range(len(cctv)):
    m_count = find([cctv[i][0], cctv[i][1]], cctv[i][2], arr)            

print(m_count)