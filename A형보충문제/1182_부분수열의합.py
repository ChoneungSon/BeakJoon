def dfs(m, time, ss):
    global arr, count, s
    if m == n:
        if ss == s and time > 0:
            count += 1
    else:
        dfs(m+1, time+1, ss+arr[m])
        dfs(m+1, time, ss)

n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
dfs(0, 0, 0)
print(count)