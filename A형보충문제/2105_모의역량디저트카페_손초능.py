def dfs(i, j, m, count, d_order, visited):
    global sp, arr, max_count, n
    if m == 3 and sp == [i, j]:
        if count > max_count:
            max_count = count
    elif 0 <= i < n and 0 <= j < n and visited[arr[i][j]] == 0:
        visited[arr[i][j]] = 1
        dfs(i+di[d_order[m]], j+dj[d_order[m]], m, count+1, d_order, visited[:])
        if m != 3:
            dfs(i+di[d_order[m+1]], j+dj[d_order[m+1]], m+1, count+1, d_order, visited[:])

T = int(input())
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]
dir_list = [[1, 0, 3, 2], [0, 1, 2, 3]]

for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_count = -1
    for i in range(n):
        for j in range(n):
            sp = [i, j]
            for k in range(2):
                visited = [0]*101
                dfs(i, j, 0, 0, dir_list[k], visited)
                
    print('#{0} {1}'.format(case, max_count))