def dfs(day, benefit):
    global arr, max_b, n
    if day >= n:
        if benefit > max_b:
            max_b = benefit
    else:
        for i in range(n):
            if i >= day: # 입력날짜 보다 크거나 같은 날짜 선택
                if i + arr[i][0] <= n: # 더해진 날짜가 마지막 날짜와 작거나 같으면 dfs 진행
                    dfs(i + arr[i][0], benefit + arr[i][1])
                else: # 더해진 날짜가 마지막 날짜보다 크면 종료조건으로 진행
                    dfs(day + arr[i][0], benefit)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_b = 0
dfs(0, 0)
print(max_b)