def dfs(p, s, s_sum, v): # m개 씩 선택했을 때, 나올 수 있는 최대 벌꿀채취 이익
    global n, m, c, max_s
    if s > c:
        return
    elif p == m:
        if max_s < s_sum:
            max_s = s_sum
    else:
        dfs(p+1, s, s_sum, v)
        dfs(p+1, s+v[p], s_sum+v[p]**2, v)

T = int(input())
for case in range(1, T+1):
    n, m, c = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    list_sum = [[] for _ in range(n)]
    max_benefit = 0
    for i in range(n):
        for j in range(n-m+1):
            max_s = 0
            v = [arr[i][j+k] for k in range(m)]
            dfs(0, 0, 0, v[:])
            list_sum[i].append(max_s) # 3개 씩의 최대 이익들을 리스트에 저장
    for i in range(n): # 최대 이익 2개를 선택
        for j in range(n-m+1):
            max_a = list_sum[i][j]
            for k1 in range(i, n):
                for k2 in range(n-m+1):
                    if k1 == i: # 같은 줄일 때는 m개 이후의 이익부터 합의 최대를 검사
                        if k2 >= j+m:
                            max_b = list_sum[k1][k2]
                        else:
                            continue
                    else: # 다른 줄일 때는 하나씩 선택하며 합의 최대를 검사
                        max_b = list_sum[k1][k2]
                    s = max_a + max_b
                    if s > max_benefit:
                        max_benefit = s
    print('#{} {}'.format(case, max_benefit))