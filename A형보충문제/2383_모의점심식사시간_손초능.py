def dfs(m, v): # 각 학생들이 1번 출구를 갈껀지 2번 출구를 갈껀지 선택하는 모든 경우
    global arr, n, num, start, member, min_time
    if m == num:
        esc1, esc2 = [], []
        for i in range(num):
            if v[i] == 0:
                esc1.append(abs(start[0][0] - member[i][0]) + abs(start[0][1] - member[i][1]))
            else:
                esc2.append(abs(start[1][0] - member[i][0]) + abs(start[1][1] - member[i][1]))
        t1, t2 = 0, 0 # 학생들이 정해진 출구에 도착하는 시간을 2개의 출구에 저장하고, 시간 순으로 정렬
        esc1.sort()
        esc2.sort()
        if esc1:
            t1 = cal_time(esc1, 0)
        if esc2:
            t2 = cal_time(esc2, 1)
        if max(t1, t2) < min_time:
            min_time = max(t1, t2)
    else:
        dfs(m+1, v[:])
        v[m] = 1
        dfs(m+1, v[:])

def cal_time(A, i): # 차량정비소와 비슷한 방식으로 배열의 가장 마지막 사람이 계단을 빠져나가는 시간을 계산
    global arr, start, min_time
    length = len(A)
    end = (length-1) % 3
    A[end] += arr[start[i][0]][start[i][1]]
    while end < length-1:
        end += 3
        if A[end-3] >= A[end]:
            A[end] = A[end-3] + arr[start[i][0]][start[i][1]]
        else:
            A[end] += arr[start[i][0]][start[i][1]]
    return A[length-1]

T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    num, start, member, min_time = 0, [], [], 10**3 + 1
    for i in range(n):
        for j in range(n): # 출구와 학생들 위치를 각각 저장
            if arr[i][j] == 1:
                num += 1
                member.append((i, j))
            elif arr[i][j] > 1:
                start.append((i, j))
    dfs(0, [0]*num)
    print('#{} {}'.format(case, min_time+1))