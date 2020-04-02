import sys
subin, sister = map(int, sys.stdin.readline().split())
visit = [0] * 100001
visit[subin] = 1
if subin != sister:
    q = [subin]
else:
    q, result = [], 0
while q:
    x = q.pop(0)
    if x - 1 >= 0:
        if sister == x-1 and visit[x-1] == 0:
            result = visit[x]
            break
        elif visit[x-1] == 0:
            visit[x-1] = visit[x] + 1
            q.append(x-1)
    if x + 1 <= 100000 and visit[x+1] == 0:
        if sister == x+1:
            result = visit[x]
            break
        elif visit[x+1] == 0:
            visit[x + 1] = visit[x] + 1
            q.append(x+1)
    if 2*x <= 100000 and visit[2*x] == 0:
        if sister == 2*x:
            result = visit[x]
            break
        elif visit[2*x] == 0:
            visit[2*x] = visit[x] + 1
            q.append(2*x)
print(result)