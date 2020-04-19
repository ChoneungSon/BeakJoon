def dfs(x):
    global c1, c2, cnt
    if c1[x]: cnt += 1; dfs(c1[x])
    if c2[x]: cnt += 1; dfs(c2[x])

for case in range(1, int(input())+1):
    edge, node = map(int, input().split())
    c1, c2 = [0]*(edge+2), [0]*(edge+2)
    arr, cnt = list(map(int, input().split())), 1
    for i in range(edge):
        if c1[arr[2*i]] == 0:
            c1[arr[2*i]] = arr[2*i+1]
        else:
            c2[arr[2*i]] = arr[2*i+1]
    dfs(node)
    print('#{} {}'.format(case, cnt))