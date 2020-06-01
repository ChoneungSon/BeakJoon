for case in range(1, int(input())+1):
    node, edge, node1, node2 = map(int, input().split())
    edges = list(map(int, input().split()))
    p = [i for i in range(node+1)]
    for i in range(edge): p[edges[2*i+1]] = edges[2*i]
    arr, x, y = set(), node1, node2
    while p[x] != x:
        arr.add(p[x])
        x = p[x]
    while p[y] not in arr: y = p[y]
    for i in range(1, node+1):
        x = i
        while