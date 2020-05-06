def dfs(row, value, end):
    global adj, min_value, visited, n
    if value >= min_value: return
    elif sum(visited) == n-1: min_value = min(min_value, value+adj[row][end])
    else:
        for i in range(n):
            if i != row and i != end and visited[i] == 0:
                visited[i] = 1
                dfs(i, value+adj[row][i], end)
                visited[i] = 0

for case in range(1, int(input())+1):
    n = int(input())
    adj = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    min_value = 100*10 + 1
    dfs(0, 0, 0)
    print('#{} {}'.format(case, min_value))