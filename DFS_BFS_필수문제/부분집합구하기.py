def dfs(m, k):
    global p_list, A
    if m == k:
        p = []
        for i in range(len(A)):
            if visited[i] == 1:
                p.append(A[i])
        p_list.append(p)
    else:
        dfs(m+1, k)
        visited[m] = 1
        dfs(m+1, k)
        visited[m] = 0

# n = int(input())
A = [1,2,3]
visited = [0]*len(A)
p_list = []
dfs(0, len(A))
print(p_list)