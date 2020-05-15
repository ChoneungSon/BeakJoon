def dfs(x, sum):
    global arr, visited, min_sum, n
    if sum >= min_sum: return
    elif x == n: min_sum = min(min_sum, sum)
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                dfs(x+1, sum+arr[x][i])
                visited[i] = 0

for case in range(1, int(input())+1):
    n, min_sum = int(input()), 100*15
    arr, visited = [list(map(int, input().split())) for _ in range(n)], [0] * n
    for i in range(n):
        visited[i] = 1
        dfs(1, arr[0][i])
        visited[i] = 0
    print('#{} {}'.format(case, min_sum))
