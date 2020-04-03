def bfs():
    global adj, visit, node, start, end
    q, visit[start] = [start], 1
    while q:
        x = q.pop(0)
        for i in range(node):
            if adj[x][i] and visit[i] == 0:
                if i == end: return visit[x]
                else:
                    visit[i] = visit[x] + 1
                    q.append(i)
    return 0

for case in range(1, int(input())+1):
    node, edge = map(int, input().split())
    adj = [[0]*node for _ in range(node)]
    for _ in range(edge):
        s, e = map(int, input().split())
        adj[s-1][e-1] = adj[e-1][s-1] = 1
    start, end = map(int, input().split())
    start -= 1; end -= 1
    visit = [0] * node
    print('#{} {}'.format(case, bfs()))