def dfs(x, cnt):
    global n, b, arr, min_value
    if cnt >= b: min_value = min(min_value, cnt-b)
    else:
        for i in range(x+1, n):
            dfs(i, cnt+arr[i])

for case in range(1, int(input())+1):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    min_value = float('inf')
    dfs(-1, 0)
    print('#{} {}'.format(case, min_value))