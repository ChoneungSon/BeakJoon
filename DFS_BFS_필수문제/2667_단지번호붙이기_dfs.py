def dfs(p):
    global arr, count, n
    arr[p[0]][p[1]] = '0'
    count += 1
    for i in range(4):
        np = [p[0]+di[i], p[1]+dj[i]]
        if 0 <= np[0] < n and 0 <= np[1] < n and arr[np[0]][np[1]] == '1':
            dfs(np)    

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
n = int(input())
arr = [list(input()) for _ in range(n)]
counts = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
            count = 0
            dfs([i, j])
            counts.append(count)
counts = sorted(counts)
print(len(counts))
for i in range(len(counts)):
    print(counts[i])