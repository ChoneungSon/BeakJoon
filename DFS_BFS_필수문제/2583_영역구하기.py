import sys
def dfs(p):
    global r, c, arr, counts
    stack = [p[:]]
    arr[p[0]][p[1]] = 1
    count = 0
    while len(stack) != 0:
        np = stack.pop()
        count += 1
        for i in range(4):
            new_p = [np[0]+di[i], np[1]+dj[i]]
            if 0 <= new_p[0] < r and 0 <= new_p[1] < c and arr[new_p[0]][new_p[1]] == 0:
                arr[new_p[0]][new_p[1]] = 1
                stack.append(new_p[:])
    counts.append(count)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
r, c, n = map(int, sys.stdin.readline().split())
arr = [[0]*c for _ in range(r)]
counts = []
for _ in range(n):
    s_c, s_r, e_c, e_r = map(int, sys.stdin.readline().split())
    for i in range(s_r, e_r):
        for j in range(s_c, e_c):
            arr[i][j] = 1
for i in range(r):
    for j in range(c):
        if arr[i][j] == 0:
            dfs([i, j])
counts = sorted(counts)
print(len(counts))
for i in range(len(counts)):
    if i == len(counts) - 1:
        print(counts[i])
    else:
        print(counts[i], end=' ')