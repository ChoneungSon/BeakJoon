def dfs(x):
    global arr, node
    level, point = find(x)
    if 2**(level+1)+2*point <= node:
        dfs(2**(level+1)+2*point)
        arr[x] += arr[2**(level+1)+2*point]
    if 2**(level+1)+2*point+1 <= node:
        dfs(2**(level+1)+2*point+1)
        arr[x] += arr[2**(level+1)+2*point+1]

def find(x):
    cnt, n = -1, x
    while n:
        cnt += 1; n //= 2
    return cnt, x-2**cnt

for case in range(1, int(input())+1):
    node, leaf, goal = map(int, input().split())
    arr = [0] * (node+1)
    for _ in range(leaf):
        n, num = map(int, input().split())
        arr[n] = num
    dfs(1)
    print('#{} {}'.format(case, arr[goal]))