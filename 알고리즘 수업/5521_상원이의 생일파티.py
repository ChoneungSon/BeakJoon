for case in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [[0]*n for _ in range(n)]
    visited = [0]*n
    visited[0] = 1
    q = [(0, 0)]
    for _ in range(m):
        r, c = map(int, input().split())
        arr[r-1][c-1] = arr[c-1][r-1] = 1
    while q:
        x, cnt = q.pop(0)
        for i in range(n):
            if visited[i] == 0 and arr[x][i] and cnt < 2:
                visited[i] = 1
                q.append((i, cnt+1))
    print('#{} {}'.format(case, sum(visited)-1))
