def dfs(s):
    n = 0
    stack = [s]
    visited = [0]*node
    while len(stack) != 0:
        np = stack.pop()
        if visited[np] == 0:
            visited[np] = 1
            if n == node-1:
                print(np+1)
                return
            else:
                print(np+1, end = ' ')
                n += 1
        for i in range(node-1,-1,-1):
            if adj[np][i] == 1 and visited[i] == 0:
                stack.append(i)

def bfs(s):
    queue = [s]
    visited = [0]*node
    lenq = 1
    n = 0
    while lenq != 0:
        for i in range(lenq):
            for j in range(node):
                if adj[queue[i]][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    queue.append(j)
        for _ in range(lenq):
            if n == node-1:
                print(queue.pop(0)+1)
                return
            else:
                print(queue.pop(0)+1, end = ' ')
                n += 1
        lenq = len(queue)


node, edge, start = map(int, input().split())
adj = [[0] * node for _ in range(node)]
for _ in range(edge):
    i, j = map(int, input().split())
    adj[i-1][j-1] = 1
    adj[j-1][i-1] = 1
dfs(start-1)
bfs(start-1)