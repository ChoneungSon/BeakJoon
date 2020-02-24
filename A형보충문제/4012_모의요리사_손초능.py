def comb(m): # 요리를 짝짓는 방법을 visited에 append 시키는 함수
    global n, visited
    for i in range(1<<n):
        visit = [0]*n
        count = 0
        for j in range(n):
            if i & 1<<j:
                count += 1
                visit[j] = 1
        if count == m:
            visited.append(visit)

T = int(input())

for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = []
    visit = [0] * n
    min_diff = 20000*8+1 # 초기 최솟값 설정
    comb(n//2)
    for t in range(len(visited)):
        adj = [[0]*n for _ in range(n)]
        for i in range(n): # dfs의 인접행렬과 같은 행렬을 생성 각각의 요리에 첨가된 재료들끼리 연결되도록
            if visited[t][i]:
                for j in range(i+1, n):
                    if visited[t][j] == 1:
                        adj[i][j], adj[j][i] = 1, 1
            else:
                for j in range(i+1, n):
                    if visited[t][j] == 0:
                        adj[i][j], adj[j][i] = 2, 2
        count_a, count_b = 0, 0
        for i in range(n):
            for j in range(n):
                if adj[i][j] == 1: # 각 요리에 들어간 재료들의 시너지 값을 각각 더해감
                    count_a += arr[i][j]
                elif adj[i][j] == 2:
                    count_b += arr[i][j]
        if min_diff > abs(count_a-count_b):
            min_diff = abs(count_a-count_b)
    print('#{0} {1}'.format(case, min_diff))