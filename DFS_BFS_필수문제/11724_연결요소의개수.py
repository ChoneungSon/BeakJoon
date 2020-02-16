import sys
def dfs(p):
    global adj, n
    stack = [p]
    visited[p] = 1
    while len(stack) != 0:
        np = stack.pop()
        for i in range(n):
            if adj[np][i] == 1:
                adj[np][i], adj[i][np] = 0, 0
                if visited[i] == 0:
                    visited[i] = 1
                    stack.append(i)

n, m = map(int, sys.stdin.readline().split())
adj = [[0]*n for _ in range(n)]
count = 0
visited = [0]*n
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    adj[i-1][j-1] = 1
    adj[j-1][i-1] = 1
for i in range(n):
    cnt = 0
    for j in range(n):
        if adj[i][j] == 1:
            count += 1
            dfs(i)
for i in range(n):
    if visited[i] == 0:
        count += 1
print(count)