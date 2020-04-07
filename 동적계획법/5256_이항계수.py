tower = [[0]*(i+1) for i in range(71)]
for case in range(1, int(input())+1):
    n, a, b = map(int, input().split())
    for i in range(n+1):
        for j in range(min(i+1, a+1)):
            if (j == 0 or j == i) and tower[i][j] == 0:
                tower[i][j] = 1
            elif tower[i][j] == 0:
                tower[i][j] = tower[i-1][j] + tower[i-1][j-1]
    print('#{} {}'.format(case, tower[n][a]))