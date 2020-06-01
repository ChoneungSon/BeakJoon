def dfs(x, cnt, length):
    global n, adj, visited, min_len, route, min_route
    if length >= min_len: return
    elif cnt == n:
        if min_len > length+adj[x][0]:
            route[x] = 0
            min_route, min_len = route[:], length+adj[x][0]
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                route[x] = i
                dfs(i, cnt+1, length+adj[x][i])
                visited[i] = 0

for case in range(1, int(input())+1):
    n, result = int(input()), float('inf')
    arr = list(map(int, input().split()))
    adj, visited, min_len = [[0] * n for _ in range(n)], [0] * n, float('inf')
    start, end, route, min_route, visited[0] = [0]*n, [0]*n, [0]*n, 1, [0]*n
    for i in range(n):
        start[i] = abs(arr[0] - arr[2*i+4]) + abs(arr[1] - arr[2*i+5])
        end[i] = abs(arr[2] - arr[2*i+4]) + abs(arr[3] - arr[2*i+5])
        for j in range(n):
            if i != j:
                adj[i][j] = adj[j][i] = abs(arr[2*i+4] - arr[2*j+4]) + abs(arr[2*i+5] - arr[2*j+5])
    dfs(0, 1, 0)
    print(min_route)
    for i in range(n):
        result = min(result, min_len - adj[i][min_route[i]] + start[min_route.index(i)] + end[min_route[i]])
    print('#{} {}'.format(case, result))
