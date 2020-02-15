def dfs():
    global 
n, m = map(int, input().split())
adj = [[0]*n for _ in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    adj[i][j] = 1
