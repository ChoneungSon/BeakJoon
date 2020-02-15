# 일단은 DFS부터 구현
def dfs(p):
    global n, count
    visited[p] = 1
    count += 1 # 마지막 부분은 띄어쓰기 없애기 위해서 count를 세어준다.
    if count == n:
        print(p+1)
    else:
        print(p+1, end=' ') # 방문한 원소를 출력
    for i in range(n):
        if visited[i] == 0 and adj[p][i] == 1: # 인접 노드 중에서 방문하지 않은 노드에 가서 dfs 진행
            dfs(i)

n, m, s = map(int, input().split())
adj = [[0]*n for _ in range(n)]
visited = [0]*n
for _ in range(m):
    i, j = map(int, input().split())
    adj[i-1][j-1], adj[j-1][i-1] = 1, 1
count = 0
dfs(s-1)