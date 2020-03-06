def bfs(): # bfs 로 가장 큰 경로 찾기
    global arr, n, di, dj, start
    max_depth = 0
    for m in range(len(start)):
        q = [start[m]]
        lenq, depth = 1, 0
        while lenq:
            depth += 1
            for _ in range(lenq):
                x, y = q.pop(0)
                for k in range(4):
                    nx, ny = x + di[k], y + dj[k]
                    if 0 <= nx < n and 0 <= ny < n and arr[x][y] > arr[nx][ny]:
                        q.append((nx, ny))
            lenq = len(q)
        if depth > max_depth:
            max_depth = depth
    return max_depth

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for case in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_h = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > max_h:
                max_h = arr[i][j]
                start = [(i, j)]
            elif arr[i][j] == max_h:
                start.append((i, j))
    max_road = bfs() # 최대값은 처음 경로 변경 전 최대 경로
    for i in range(n):
        for j in range(n): # 변경할 지점을 고르고
            for m in range(1, k+1): # 최대 변경 범위까지 변경하면서, 최대 경로 찾기
                arr[i][j] -= 1
                road = bfs()
                if road > max_road:
                    max_road = road
            arr[i][j] += k
    print('#{} {}'.format(case, max_road))