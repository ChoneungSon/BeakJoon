def dfs(x):
    global arr, node1, node2, parent
    flag = 0
    if x==node1 or x==node2: flag=1
    if arr[x][0] == 0 and arr[x][1] == 0: return flag, 0
    else:
        cnt = 0
        for i in range(2):
            if arr[x][i]:
                flag_part, cnt_part = dfs(arr[x][i])
                if flag_part == 2: return 2, cnt_part
                flag += flag_part
                cnt += cnt_part+1
        if flag == 2: parent = x
        return flag, cnt

for case in range(1, int(input())+1):
    node, edge, node1, node2 = map(int, input().split())
    parent = 0
    edges = list(map(int, input().split()))
    arr = [[0]*3 for _ in range(node+1)]
    for i in range(edge):
        for j in range(2):
            if arr[edges[2*i]][j] == 0:
                arr[edges[2*i]][j] = edges[2*i+1]
                break
            arr[edges[2*i+1]][2] = edges[2*i]
    for i in range(1, node+1):
        if arr[i][2] == 0:
            flag, cnt = dfs(i)
            break
    print('#{} {} {}'.format(case, parent, cnt+1))