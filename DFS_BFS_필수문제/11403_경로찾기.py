def dfs():
    global adj, n
    for i in range(n):
        visited = [0]*n
        stack = [i]
        while len(stack) != 0:
            np = stack.pop()
            for j in range(n):
                if adj[np][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    arr[i][j] = 1
                    stack.append(j)

n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
arr = [[0]*n for _ in range(n)]
dfs()

for i in range(n):
    for j in range(n):
        if j == n-1:
            print(arr[i][j])
        else:
            print(arr[i][j], end=' ')