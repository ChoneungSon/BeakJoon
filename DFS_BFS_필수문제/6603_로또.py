import sys
def dfs(n, m):
    global count
    if count == 6:
        for i in range(6):
            if i == 5:
                print(b[i])
            else:
                print(b[i], end=' ')
    else:
        for i in range(m, n[0]-(6-m)+1):
            if i > n[0]:
                continue
            else:
                b[count] = n[i]
                count += 1
                dfs(n, i+1)
                count -= 1
                b[count] = 0 

n_list = []
while 1:
    n = list(map(int, sys.stdin.readline().split()))
    if n[0] == 0:
        break
    else:
        n_list.append(n[:])

for i in range(len(n_list)):
    b = [0]*6
    count = 0
    dfs(n_list[i], 1)
    if i != len(n_list)-1:
        print()