def bfs(x, y):
    global arr, n, di, dj
    q = [(x, y)]
    lenq = 1
    count = 0
    while lenq:
        count += 1
        for _ in range(lenq):
            x, y = q.pop(0)
            for i in range(4):
                nx = x + di[i]
                ny = y + dj[i]
                if 0 <= nx < n and 0 <= ny < n and arr[x][y] > arr[nx][ny]:
                    q.append((nx, ny))
        lenq = len(q)
    return count

def find():
    global arr, n, p
    max_s = 0
    for i in range(len(p)):
        x, y = p[i]
        s = bfs(x, y)
        if s > max_s:
            max_s = s
    return max_s

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for case in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_value = - 5
    for i in range(n):
        for j in range(n):
            if arr[i][j] > max_value:
                max_value = arr[i][j]
                p = [(i, j)]
            elif arr[i][j] == max_value:
                p.append((i, j))
    max_s = find()
    for i in range(n**2):
        for _ in range(k):
            arr[i//n][i%n] -= 1
            s = find()
            if s > max_s:
                max_s = s
        arr[i//n][i%n] += k
    print('#{} {}'.format(case, max_s))