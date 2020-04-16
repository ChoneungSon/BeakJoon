for case in range(1, int(input())+1):
    edge, node = map(int, input().split())
    c1, c2 = [0]*(edge+2), [0]*(edge+2)
    arr, stack, cnt = list(map(int, input().split())), [node], 1
    for i in range(edge):
        if c1[arr[2*i]] == 0:
            c1[arr[2*i]] = arr[2*i+1]
        else:
            c2[arr[2*i]] = arr[2*i+1]
    while stack:
        x = stack.pop()
        if c1[x]: cnt +=1; stack.append(c1[x])
        if c2[x]: cnt +=1; stack.append(c2[x])
    print('#{} {}'.format(case, cnt))