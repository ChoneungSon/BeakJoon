import sys
n, k = map(int, sys.stdin.readline().split())
visit = [2**31]*(k+1)
visit[0] = 0
for i in range(n):
    num = int(sys.stdin.readline())
    for j in range(num, k+1):
        visit[j] = min(visit[j], 1+visit[j-num])
if visit[-1] != 2**31: print(visit[-1])
else: print(-1)