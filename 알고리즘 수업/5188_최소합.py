# for case in range(1, int(input())+1):
#     dx = [0, 1]; dy = [1, 0]
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     visited = [[0]*n for _ in range(n)]
#     visited[0][0] = arr[0][0]; stack = [(0, 0)]
#     while stack:
#         x, y = stack.pop()
#         for i in range(2):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and (visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + arr[nx][ny]):
#                 visited[nx][ny] = visited[x][y] + arr[nx][ny]
#                 stack.append((nx, ny))
#     print('#{} {}'.format(case, visited[n-1][n-1]))

for case in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not(i == 0 and j == 0):
                min_value = 100 * 25 + 1
                if 0 <= i-1 < n: min_value = min(min_value, arr[i][j] + arr[i-1][j])
                if 0 <= j-1 < n: min_value = min(min_value, arr[i][j] + arr[i][j-1])
                arr[i][j] = min_value
    print('#{} {}'.format(case, arr[n-1][n-1]))