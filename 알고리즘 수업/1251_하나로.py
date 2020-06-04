import heapq
for case in range(1, int(input())+1):
    n = int(input())
    points, result = [0]*2, 0
    for i in range(2):
        points[i] = list(map(int, input().split()))
    e = float(input())
    adj = [[float('inf')]*n for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            adj[i][j] = adj[j][i] = ((points[0][i] - points[0][j])**2 + (points[1][i] - points[1][j])**2) * e
    q, visited = [(0, 0)], [0]*n
    while q:
        weight, x = heapq.heappop(q)
        if visited[x]: continue
        visited[x] = 1
        result += weight
        if sum(visited) == n: break
        for i in range(n):
            if i != x and visited[i] == 0: heapq.heappush(q, (adj[x][i], i))
    print('#{} {}'.format(case, round(result)))


