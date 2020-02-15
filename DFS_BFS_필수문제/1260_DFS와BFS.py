# 일단은 DFS부터 구현
def dfs(p):
    global n, count
    visited[p] = 1
    count += 1
    if count == n:
        print(p+1)
    else:
        print(p+1, end=' ')
    for i in range(n):
        if visited[i] == 0 and adj[p][i] == 1:
            dfs(i)

n, m, s = map(int, input().split())
adj = [[0]*n for _ in range(n)]
visited = [0]*n
for _ in range(m):
    i, j = map(int, input().split())
    adj[i-1][j-1], adj[j-1][i-1] = 1, 1
count = 0
dfs(s-1)