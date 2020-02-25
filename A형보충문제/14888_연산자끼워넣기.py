def dfs(m, n_list, visited):
    global n, num, cal, min_value, max_value
    if m == n-1:
        value = calcul(visited[:])
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
    else:
        for i in range(4):
            if n_list[i] > 0:
                n_list[i] -= 1
                visited[m] = i
                dfs(m+1, n_list[:], visited[:])
                n_list[i] += 1
                visited[m] = 0

def calcul(v):
    global n, num
    s1 = num[0]
    for i in range(1, n):
        s2 = num[i]
        if v[i-1] == 0:
            s1 += s2
        elif v[i-1] == 1:
            s1 -= s2
        elif v[i-1] == 2:
            s1 *= s2
        elif v[i-1] == 3:
            if s1 < 0:
                s1 = -(-s1//s2)
            else:
                s1 //= s2
    return s1

n = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split()))
big = [1, 1, 2, 2]
min_value = 1000000001
max_value = -1000000001
dfs(0, cal[:], [0]*(n-1))
print(max_value)
print(min_value)