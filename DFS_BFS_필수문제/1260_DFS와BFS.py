def dfs(k, used):
    global n, adj, s, nums
    for i in range(n):
        if adj[k][i] == 1 and used[i] == 0:
            used[i] = 1
            nums.append(str(i+1))
            dfs(i, used)

def bfs(k, used):
    global n, adj, s
    q = [k]
    used[k] = 1
    nums = [str(k+1)]
    while q:
        x = q.pop(0)
        for i in range(n):
            if adj[x][i] == 1 and used[i] == 0:
                used[i] = 1
                q.append(i)
                nums.append(str(i+1))
    print(' '.join(nums))

n, m, s = map(int, input().split())
adj = [[0]*n for _ in range(n)]
visited = [0]*n
for _ in range(m):
    i, j = map(int, input().split())
    adj[i-1][j-1], adj[j-1][i-1] = 1, 1
used = [0]*n
used[s-1] = 1
nums = [str(s)]
dfs(s-1, used)
print(' '.join(nums))
bfs(s-1, [0]*n)