# def dfs(x):
#     global arr, adj, n, visited
#     visited[x] = 0
#     for i in range(1, n+1):
#         if adj[x][i]:
#             adj[x][i] = adj[i][x] = 0
#             dfs(i)
#
# for case in range(1, int(input())+1):
#     n, m = map(int, input().split())
#     arr = list(map(int, input().split()))
#     adj, cnt = [[0] * (n+1) for _ in range(n+1)], 0
#     visited = [1] * (n+1); visited[0] = 0
#     for i in range(m):
#         adj[arr[i*2]][arr[i*2+1]] = 1
#         adj[arr[i*2+1]][arr[i*2]] = 1
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if adj[i][j]:
#                 dfs(i)
#                 cnt += 1
#                 break
#     print('#{} {}'.format(case, cnt+sum(visited)))

def find_set(x):
    global heads
    if heads[x] == x: return x
    else:
        heads[x] = find_set(heads[x])
        return heads[x]

def union(px, py):
    global rank, heads
    if rank[px] < rank[py]: heads[px] = py
    else:
        heads[py] = px
        if rank[px] == rank[py]: rank[px] += 1

for case in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    heads, rank, cnt = [i for i in range(n)], [0] * n, 0
    for i in range(m):
        union(find_set(arr[2*i]-1), find_set(arr[2*i+1]-1))
    print(heads)
    for i in range(n):
        find_set(heads[i])
        if heads[i] == i: cnt += 1
    print('#{} {}'.format(case, cnt))