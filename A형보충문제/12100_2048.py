import sys, copy, pprint
def game(d, mat): # 0 위, 1 좌, 2 아래, 3 우
    global n
    for _ in range(d):
        mat = rot(mat)
    for i in range(n):
        for j in range(n):
            if mat[j][i]:
                p = j
                while p < n-1:
                    p += 1
                    if mat[p][i] == mat[j][i]:
                        mat[p][i], mat[j][i] = 0, mat[j][i]*2
                    elif mat[p][i] == 0:
                        continue
                    else:
                        break
        for j in range(n):
            if mat[j][i] == 0:
                p = j
                while p < n-1:
                    p += 1
                    if mat[p][i]:
                        mat[p][i], mat[j][i] = mat[j][i], mat[p][i]
                        break

def rot(mat):
    global n
    temp_arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp_arr[i][j] = mat[n-j-1][i]
    return temp_arr

def dfs(m, mat):
    global n, max_value
    if m == 5:
        s = 0
        pprint.pprint(mat)
        for i in range(n):
            for j in range(n):
                if mat[i][j] > s:
                    s = mat[i][j]
        max_value = max(s, max_value)
    else:
        for i in range(4):
            g_mat = game(i, copy.deepcopy(mat))
            dfs(m+1, copy.deepcopy(g_mat))

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_value = 0
dfs(0, copy.deepcopy(arr))
print(max_value)