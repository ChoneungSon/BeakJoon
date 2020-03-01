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
            if connect[j] < connect[idx]: # 가장 작은 시간을 가진 접수처의 인덱스를 저장
                idx = j
            if connect[j] <= t_cost[i]: # 고객의 도착시간보다 작거나 같은 시간을 가지는 접수처를 선택
                connect[j] = t_cost[i] + list_connect[j] # 고객의 시간에 처리 시간을 더함
                t_cost[i] = connect[j] # 고객의 탈출 시간을 저장
                visit[i] = j # 고객이 방문한 접수처의 번호를 저장
                break
        else:
            connect[idx] += list_connect[idx] # 작거나 같은 시간을 가지는 접수처가 없으면
            t_cost[i] = connect[idx] # 가장 작은 시간을 가진 접수처에서 기다리고, 탈출 시간을 기록
            visit[i] = idx
    visited = [0] * cost
    cnt = 0
    while cnt < cost:
        flag = 1
        for i in range(cost):
            if visited[i] == 0 and flag: # 접수처를 가장 빨리 나온 고객을 알아내기 위해 최소 시간을 가지는 인덱스를 찾기
                idx = i
                flag = 0
            elif t_cost[i] < t_cost[idx] and visited[i] == 0:
                idx = i
            elif t_cost[i] == t_cost[idx] and visited[i] == 0 and visit[idx] > visit[i]: # 탈출 시간이 같을 때는, 접수처의 번호가 작은 고객 부터
                idx = i
        visited[idx] = 1
        for i in range(n_repair): # 고객의 접수처 탈출 시간보다 작거나 같은 수리처 찾기
            if repair[i] <= t_cost[idx]:
                repair[i] = t_cost[idx] + list_repair[i]
                r_idx = i # 그 때의 수리처 번호 저장
                break
        else:
            r_idx = 0 # 작거나 같은 수리처가 없으면
            for i in range(1, n_repair):
                if repair[i] < repair[r_idx]:
                    r_idx = i # 최소시간을 가지는 수리처에 방문
            repair[r_idx] += list_repair[r_idx]
        if visit[idx] == v_connect-1 and r_idx == v_repair-1: # 원하는 접수처와 수리처를 방문한 손님일 때, 손님의 인덱스를 합한다.
            s += idx+1
        cnt += 1
    if s == 0:
        s = -1
    print('#{} {}'.format(case, s))