n = int(input())
arr = list(map(int, input().split()))
visited = [0]*n
visited[0] = 1
for i in range(1, n):
    result = 0
    for j in range(i):
        if arr[i] > arr[j]: result = max(result, visited[j])
    visited[i] = result + 1
print(n-max(visited))