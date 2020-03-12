n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
di = [0, 1, 1]
dj = [1, 1, 0]
d = [[0, 1], [0, 1, 2], [1, 2]]
visit = [[[0]*3 for _ in range(n)] for _ in range(n)]
visit[0][1][0] = 1
for i in range(n):
    for j in range(n):
        for k in range(3):
            if visit[i][j][k]:
                for m in d[k]:
                    x, y = i+di[m], j+dj[m]
                    if x < n and y < n:
                        if (m == 0 or m == 2) and arr[x][y] == 1: continue
                        elif m == 1 and (arr[x][y] or arr[x-1][y] or arr[x][y-1]): continue
                        visit[x][y][m] += visit[i][j][k]
print(sum(visit[n-1][n-1]))