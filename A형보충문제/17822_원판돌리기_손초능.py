r, c, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
pivot = [0] * r # 각 원판에서 위를 향하는 좌표를 설정
for _ in range(T):
    x, d, k = map(int, input().split())
    for i in range(r):
        if (i+1) % x == 0: # 원판이 x의 배수일 때,
            if d: # 반시계 방향
                pivot[i] = (pivot[i]+k) % c
            else: # 시계 방향으로 pivot 값을 변경
                pivot[i] = (pivot[i]+(c-1)*k) % c
    flag = 1
    visit = [[0] * c for _ in range(r)]
    for i in range(c): # 규칙에 따라 각각의 숫자를 변경
        for j in range(r-1):
            if arr[j][(pivot[j]+i) % c] != 0 and arr[j][(pivot[j]+i) % c] == arr[j+1][(pivot[j+1]+i) % c]:
                visit[j][(pivot[j]+i) % c] += 1
                visit[j + 1][(pivot[j + 1] + i) % c] += 1
                flag = 0
        for j in range(r):
            if arr[j][i % c] != 0 and arr[j][i % c] == arr[j][(i+1) % c]:
                visit[j][i % c] += 1
                visit[j][(i+1) % c] += 1
                flag = 0
    if flag: # 변경된 숫자가 없을 경우의 규칙으로 진행
        sum_value, count = 0, 0
        for i in range(r):
            for j in range(c):
                if arr[i][j] != 0:
                    sum_value += arr[i][j]
                    count += 1
        if count: # count가 0일때, 0으로 나누면 ZeroDivision Error를 막기위해서
            average = sum_value/count
        else:
            average = 0
        for i in range(r):
            for j in range(c):
                if arr[i][j] != 0:
                    if arr[i][j] > average:
                        arr[i][j] -= 1
                    elif arr[i][j] < average:
                        arr[i][j] += 1
    else:
        for i in range(r):
            for j in range(c):
                if visit[i][j] > 0:
                    arr[i][j] = 0
cnt = 0
for i in range(r):
    for j in range(c):
        cnt += arr[i][j]
print(cnt)