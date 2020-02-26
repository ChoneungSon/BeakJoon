def dfs(m, count, v):
    global n, min_diff
    if count == n//2:
        s = diff(v[:])
        if s < min_diff:
            min_diff = s
    else:
        for i in range(m+1,m+):
            v[i] = 1
            dfs(i, count+1, v[:])
            v[i] = 0
            dfs(i, count, v[:])

def diff(visited):
    global arr, n
    s = 0
    for i in range(n):
        for j in range(n):
            if visited[i] == 1 and visited[j] == 1:
                s += arr[i][j]
            if visited[i] == 0 and visited[j] == 0:
                s -= arr[i][j]
    return abs(s)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
min_diff = 100*20*21//2+1
dfs(0, 0, [0]*n)
print(min_diff)