n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[[0]*3 for _ in range(n)] for _ in range(n)]
visit[0][1][0] = 1
for i in range(n):
    for j in range(1, n):
        if arr[i][j] != 1:
            if i == 0:
                visit[i][j][0] += visit[i][j-1][0] + visit[i][j-1][1]
            else:
                visit[i][j][0] += visit[i][j-1][0] + visit[i][j-1][1]
                visit[i][j][2] += visit[i-1][j][2] + visit[i-1][j][1]
                if arr[i-1][j] != 1 and arr[i][j-1] != 1:
                    visit[i][j][1] += visit[i-1][j-1][0] + visit[i-1][j-1][1] + visit[i-1][j-1][2]
print(sum(visit[n-1][n-1]))
