T = int(input())
for case in range(1, T+1):
    n_connect, n_repair, cost, v_connect, v_repair = map(int, input().split())
    list_connect = list(map(int, input().split()))
    list_repair = list(map(int, input().split()))
    t_cost = list(map(int, input().split()))
    visit = [0] * cost
    connect = [0] * n_connect
    repair = [0] * n_repair
    s = 0
    for i in range(cost):
        idx = 0
        for j in range(n_connect):
            if connect[j] < connect[idx]:
                idx = j
            if connect[j] <= t_cost[i]:
                connect[j] = t_cost[i] + list_connect[j]
                t_cost[i] = connect[j]
                visit[i] = j
                break
        else:
            connect[idx] += list_connect[idx]
            t_cost[i] = connect[idx]
            visit[i] = idx
    visited = [0] * cost
    cnt = 0
    while cnt < cost:
        flag = 1
        for i in range(cost):
            if visited[i] == 0 and flag:
                idx = i
                flag = 0
            elif t_cost[i] < t_cost[idx] and visited[i] == 0:
                idx = i
            elif t_cost[i] == t_cost[idx] and visited[i] == 0 and visit[idx] > visit[i]:
                idx = i
        visited[idx] = 1
        for i in range(n_repair):
            if repair[i] <= t_cost[idx]:
                repair[i] = t_cost[idx] + list_repair[i]
                r_idx = i
                break
        else:
            r_idx = 0
            for i in range(1, n_repair):
                if repair[i] < repair[r_idx]:
                    r_idx = i
            repair[r_idx] += list_repair[r_idx]
        if visit[idx] == v_connect-1 and r_idx == v_repair-1:
            s += idx+1
        cnt += 1
    if s == 0:
        s = -1
    print('#{} {}'.format(case, s))