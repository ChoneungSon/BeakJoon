for case in range(1, int(input())+1):
    v, e = map(int, input().split())
    adj, INF = {i:[] for i in range(v+1)}, float('inf')
    visited = [INF for _ in range(v+1)]
    visited[0] = 0
    for _ in range(e):
        s, e, w = map(int, input().split())
        adj[s].append((e, w))
    for i in range(v):
        for end, weight in adj[i]:
            visited[end] = min(visited[end], visited[i]+weight)
    print('#{} {}'.format(case, visited[v]))