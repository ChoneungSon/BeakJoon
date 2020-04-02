import sys, pprint
def rot():
    global piece, x, y
    copy_arr = [[0]*y for _ in range(x)]
    for i in range(x):
        for j in range(y):
            copy_arr[i][j] = piece[y-j-1][i]
    piece = copy_arr

def find(x, y, len1, len2):
    global piece, arr, r, c
    if x+len1-1 >= r or y+len2-1 >= c: return 0
    for i in range(len1):
        for j in range(len2):
            if piece[i][j] == 0: continue
            elif arr[x+i][y+j] == 1: return 0
    return 1

def define():
    global piece, x, y, cnt, arr, r, c
    for k in range(4):
        for i in range(r-x+1):
            for j in range(c-y+1):
                if find(i, j, x, y):
                    for row in range(x):
                        for col in range(y):
                            if piece[row][col]:
                                arr[i+row][j+col] = 1
                                cnt += 1
                    return
        if k == 3: return
        x, y = y, x
        rot()

r, c, n = map(int, sys.stdin.readline().split())
arr, cnt = [[0]*c for _ in range(r)], 0
for t in range(n):
    x, y = map(int, sys.stdin.readline().split())
    piece, flag = [list(map(int, sys.stdin.readline().split())) for _ in range(x)], 0
    define()
    if cnt == r*c: break
print(cnt)