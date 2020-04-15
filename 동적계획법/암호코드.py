num = input()
visit = [[0]*2 for _ in range(len(num))]
if num[-1] != '0': visit[-1][0] = 1
for i in range(len(num)-2, -1, -1):
    if int(num[i]) != 0: visit[i][0] = sum(visit[i+1])
    else: continue
    if 1 <= int(num[i:i+2]) <= 26:
        if i == len(num)-2: visit[i][1] = 1
        else: visit[i][1] = sum(visit[i+2])
print(sum(visit[0])%1000000)