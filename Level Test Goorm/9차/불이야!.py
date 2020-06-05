r, c = map(int, input().split())
arr = ['#'*(c+2)] + ['#'+input()+'#' for _ in range(r)] + ['#'*(c+2)]
dx, dy, flag = [0, 1, 0, -1], [1, 0, -1, 0], 0
visited = [[float('inf')]*(c+2) for _ in range(r+2)]
q, front, rear = [], -1, -1
for i in range(1, r+1):
    for j in range(1, c+1):
        if arr[i][j] == '@':
            q.append((i, j))
            visited[i][j] = 0
            front += 1
while front != rear:
    rear += 1
    x, y = q[rear]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if arr[nx][ny] != '#' and visited[nx][ny] == float('inf'):
            if arr[nx][ny] == '&':
                flag = 1
                print(visited[x][y])
            visited[nx][ny] = visited[x][y]+1
            q.append((nx, ny))
            front += 1
    if flag: break
if not flag: print(-1)