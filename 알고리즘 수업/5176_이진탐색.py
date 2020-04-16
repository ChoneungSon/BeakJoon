def dfs(x):
    global cnt, n, arr
    level, point = find(x)
    if 2**(level+1) + 2*point <= n:
        dfs(2**(level+1) + 2*point)
    else: arr[x] = cnt; cnt += 1; return
    arr[x] = cnt; cnt += 1
    if 2**(level+1) + 2*point + 1 <= n:
        dfs(2**(level+1) + 2*point + 1)

def find(x):
    cnt, n = -1, x
    while n:
        cnt += 1
        n //= 2
    return cnt, x-2**cnt

for case in range(1, int(input())+1):
    n = int(input())
    arr, cnt = [0] * (n+1), 1
    dfs(1)
    print('#{} {} {}'.format(case, arr[1], arr[n//2]))