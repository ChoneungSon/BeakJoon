def dfs(n, s):
    global flag
    if flag:
        return
    elif n == 7:
        if s == 100:
            flag = 1
            real.sort()
            for i in range(7):
                print(real[i])
    elif s > 100:
        return
    else:
        for i in range(9):
            if visited[i] == 0:
                visited[i] = 1
                s += list_boy[i]
                real[n] = list_boy[i]
                dfs(n+1, s)
                s -= list_boy[i]
                visited[i] = 0

list_boy = [0] * 9
visited = [0] * 9
for i in range(9):
    list_boy[i] = int(input())
real = [0]*7
flag = 0
dfs(0, 0)