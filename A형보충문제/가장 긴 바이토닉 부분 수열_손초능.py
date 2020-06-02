n = int(input())
arr = list(map(int, input().split()))
visited = [[0]*2 for _ in range(n)]
visited[0][0] = visited[n-1][1] = 1
for i in range(1, n):
    d = rd = 0
    for j in range(i):
        if arr[i] > arr[j]: d = max(d, visited[j][0])
        if arr[n-1-i] > arr[n-1-j]: rd = max(rd, visited[n-1-j][1])
    visited[i][0], visited[n-i-1][1] = d+1, rd+1
print(sum(max(visited, key=lambda x: sum(x)))-1)