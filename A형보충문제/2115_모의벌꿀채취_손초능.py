def dfs(p, s, s_sum, v):
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
            list_sum[i].append(max_s)
    for i in range(n):
        for j in range(n-m+1):
            max_a = list_sum[i][j]
            for k1 in range(i, n):
                for k2 in range(n-m+1):
                    if k1 == i:
                        if k2 >= j+m:
                            max_b = list_sum[k1][k2]
                        else:
                            continue
                    else:
                        max_b = list_sum[k1][k2]
                    s = max_a + max_b
                    if s > max_benefit:
                        max_benefit = s
    print('#{} {}'.format(case, max_benefit))