import sys
r, c = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline() for _ in range(r)]
visit, max_value = [[0]*c for _ in range(r)]
for i in range(r):
    flag = 0
    for j in range(c):
        if flag == 0 and arr[i][j] == '1':
            flag, visit[i][j] = 1, 1
        elif flag and arr[i][j] == '1':
            visit[i][j] = visit[i][j-1] + 1
        elif flag and arr[i][j] == '0':
            flag = 0