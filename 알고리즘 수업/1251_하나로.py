import time
t = time.time()
import heapq
for case in range(1, int(input())+1):
    n = int(input())
    points, result = [0]*2, 0
    xarr = list(map(int, input().split()))
    yarr = list(map(int, input().split()))
    e = float(input())
    adj = [[float('inf')]*n for _ in range(n)]
    for i in range(n-1):
        for j in range(i+1, n):
            adj[i][j] = adj[j][i] = ((xarr[i] - xarr[j])**2 + (yarr[i] - yarr[j])**2)
    q, visited, key = [(0, 0)], [0]*n, [float('inf')]*n
    key[0], cnt = 0, 0
    while q:
        weight, x = heapq.heappop(q)
        if visited[x]: continue
        visited[x] = 1
        result += weight
        cnt += 1
        if cnt == n: break
        for i in range(n):
            if visited[i] == 0 and key[i] > adj[x][i]:
                heapq.heappush(q, (adj[x][i], i))
                key[i] = adj[x][i]
    print('#{} {}'.format(case, round(result*e)))
print(time.time()-t)

