def dfs(x, battery, cnt):
    global arr, min_cnt
    if x >= arr[0]: min_cnt = min(min_cnt, cnt)
    elif cnt >= min_cnt: return
    else:
        for i in range(battery, 0, -1):
            if x + i >= arr[0]: dfs(arr[0], battery, cnt)
            else: dfs(x+i, arr[x+i], cnt+1)

for case in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    min_cnt = arr[0] + 1
    dfs(1, arr[1], 0)
    print("#{} {}".format(case, min_cnt))
