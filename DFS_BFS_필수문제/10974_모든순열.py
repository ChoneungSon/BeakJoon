def dfs(m , k):
    if m == k:
        for i in range(k):
            if i == k-1:
                print(p[i])
            else:
                print(p[i], end=' ')
    else:
        for i in range(k):
            if visited[i] == 0:
                visited[i] = 1
                p[m] = i+1
                dfs(m+1, k)
                p[m] = 0
                visited[i] = 0

n = int(input())
visited = [0]*n
p = [0]*n
dfs(0, n)