for case in range(1, int(input())+1):
    dx, dy = [0,1,0,-1], [1,0,-1,0]
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[float('inf')]*n for _ in range(n)]
    visited[0][0] = arr[0][0]
    q = [(0, 0)]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny]+visited[x][y] < visited[nx][ny]:
                visited[nx][ny] = arr[nx][ny]+visited[x][y]
                q.append((nx, ny))
    print('#{} {}'.format(case, visited[n-1][n-1]))