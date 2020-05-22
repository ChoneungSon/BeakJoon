def bfs():
    global n, arr, dx, dy, charge
    charge[0][0], q = 0, [(0, 0)]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                length = charge[x][y] + 1
                if arr[nx][ny] > arr[x][y]: length += arr[nx][ny] - arr[x][y]
                if charge[nx][ny] > length:
                    charge[nx][ny] = length
                    q.append((nx, ny))

for case in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    INF = float('inf')
    charge = [[INF]*n for _ in range(n)]
    bfs()
    print('#{} {}'.format(case, charge[n-1][n-1]))