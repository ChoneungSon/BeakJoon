import heapq
for case in range(1, int(input())+1):
    v, E = map(int, input().split())
    visited = [0]*(v+1)
    key = [-1] * (v+1)
    adj = {i:[] for i in range(v+1)}
    hq, key[0], result = [(0, 0)], 0, 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((e, w))
        adj[e].append((s, w))
    while hq:
        w, node = heapq.heappop(hq)
        if visited[node]: continue
        visited[node] = 1
        result += w
        for e, w in adj[node]:
            if not visited[e] and (key[e] == -1 or key[e] > w):
                key[e] = w
                heapq.heappush(hq, (w, e))
    print('#{} {}'.format(case, result))