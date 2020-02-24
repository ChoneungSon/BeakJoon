def dfs(m, v):
    global n, r, c, arr, visited
    if m == n:
        visited.append(v[:])
    else:
        for i in range(c):
            v[m] = i
            dfs(m+1, v[:])

def rm(p, d, amp):
    global n, r, c, copy_arr, di, dj
    if amp == 0 or not(0 <= p[0] < r and 0 <= p[1] < c):
        return
    else:
        namp = copy_arr[p[0]][p[1]]
        copy_arr[p[0]][p[1]] = 0
        if amp < namp:
            amp = namp
        for i in range(4):
            np = [p[0]+di[i], p[1]+dj[i]]
            if 0 <= np[0] < r and 0 <= np[1] < c:
                if d == i:
                    rm(np[:], d, amp-1)
                else:
                    if namp != 0:
                        rm(np[:], i, namp-1)
            
def sort_arr():
    global copy_arr, r, c
    for i in range(c):
        for j in range(r-1, -1, -1):
            if copy_arr[j][i] == 0:
                x = j
                while 1:
                    x -= 1
                    if 0 <= x and copy_arr[x][i] != 0:
                        copy_arr[j][i], copy_arr[x][i] = copy_arr[x][i], copy_arr[j][i]
                        break
                    elif x < 0:
                        break

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for case in range(1, T+1):
    n, c, r = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(r)]
    visited = []
    visit = [0]*n
    dfs(0, visit)
    min_count = r*c+1
    for i in range(len(visited)):
        v_list = visited[i]
        count = 0
        copy_arr = [[0]*c for _ in range(r)]
        for j in range(r):
            for k in range(c):
                copy_arr[j][k] = arr[j][k]
        for j in range(n):
            for k in range(r):
                if copy_arr[k][v_list[j]] != 0:
                    a = copy_arr[k][v_list[j]]
                    copy_arr[k][v_list[j]] = 0
                    for k1 in range(3):
                        rm([k+di[k1], v_list[j]+dj[k1]], k1, a-1)
                    break
            sort_arr()
        for j in range(r):
            for k in range(c):
                if copy_arr[j][k] != 0:
                    count += 1
        if min_count > count:
            min_count = count
        if min_count == 0:
            break
    print('#{0} {1}'.format(case, min_count))