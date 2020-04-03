def bfs():
    global arr, visit, n
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                visit[i][j], q = 1, [(i, j)]
                while q:
                    x, y = q.pop(0)
                    for k in range(4):
                        nx, ny = x + di[k], y + dj[k]
                        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 1 and visit[nx][ny] == 0:
                            if arr[nx][ny] == 3:
                                return visit[x][y]-1
                            else:
                                visit[nx][ny] = visit[x][y] + 1
                                q.append((nx, ny))
                return 0

di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
for case in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    print('#{} {}'.format(case, bfs()))