def dfs(lev):
    global n, arr, di, dj
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    stack = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > lev and visited[i][j] == 0:
                stack.append([i, j])
                visited[i][j] = 1
                while len(stack) != 0:
                    np = stack.pop()
                    for k in range(4):
                        new_p = [np[0]+di[k], np[1]+dj[k]]
                        if 0 <= new_p[0] < n and 0 <= new_p[1] < n and arr[new_p[0]][new_p[1]] > lev and visited[new_p[0]][new_p[1]] == 0:
                            visited[new_p[0]][new_p[1]] = 1
                            stack.append(new_p[:])
                cnt += 1
    return cnt

import sys
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_area = 0

for level in range(1, 101):
    count = dfs(level)
    if count > max_area:
        max_area = count
    if count == 0:
        break

print(max_area)