def ok(x, l):
    global arr
    r, c = x//10, x%10
    for i in range(l):
        for j in range(l):
            nr, nc = r+i, c+j
            if 0 <= nr < 10 and 0 <= nc < 10:
                if arr[r+i][c+j] == 0:
                    return 0
            else:
                return 0
    return 1

def dfs(x, remain, s):
    global arr, min_count, v
    if s >= min_count:
        return
    elif remain == 0:
        if s < min_count:
            min_count = s
        return
    else:
        for i in range(x, 100):
            if arr[i//10][i%10]:
                for j in range(4, -1, -1):
                    if ok(i, j+1) and v[j]:
                        r, c = i//10, i%10
                        for k1 in range(j+1):
                            for k2 in range(j+1):
                                arr[r+k1][c+k2] = 0
                        v[j] -= 1
                        dfs(i+1, remain-(j+1)**2, s+1)
                        for k1 in range(j+1):
                            for k2 in range(j+1):
                                arr[r+k1][c+k2] = 1
                        v[j] += 1
                break

arr = [list(map(int, input().split())) for _ in range(10)]
cnt = 0
for i in range(10):
    for j in range(10):
        if arr[i][j]:
            cnt += 1
min_count = 26
v = [5]*5
dfs(0, cnt, 0)
if min_count == 26:
    if cnt == 0:
        print(0)
    else:
        print(-1)
else:
    print(min_count)