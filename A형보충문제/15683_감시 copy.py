import sys, copy
def find(n, dirs):
    global arr, r, c, cctv, m_count, di, dj
    if n == len(cctv):
        c_arr = copy.deepcopy(arr)
        for i in range(n):
            p = [cctv[i][0], cctv[i][1]]
            for j in dir_list[cctv[i][2]-1][dirs[i]]:
                np = p[:]
                while 1:
                    np = [np[0]+di[j], np[1]+dj[j]]
                    if 0 <= np[0] < r and 0 <= np[1] < c and c_arr[np[0]][np[1]] != 6:
                        if c_arr[np[0]][np[1]] == 0:
                            c_arr[np[0]][np[1]] = 7
                    else:
                        break
        count = 0
        for i in range(r):
            for j in range(c):
                if c_arr[i][j] == 0:
                   count += 1
        if count < m_count:
            m_count = count
    else:
        if cctv[n][2] == 1 or cctv[n][2] == 3 or cctv[n][2] == 4:
            cut = 4
        elif cctv[n][2] == 2:
            cut = 2 
        elif cctv[n][2] == 5:
            cut = 1
        for i in range(cut):
            dirs.append(i)
            find(n+1, dirs)
            dirs.pop()

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
dir_list = [
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]
r, c = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
cctv = []
m_count = 65
for i in range(r):
    for j in range(c):
        if 0 < arr[i][j] < 6:
            cctv.append([i, j, arr[i][j]])
find(0, [])
print(m_count)