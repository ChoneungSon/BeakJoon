def dfs(sp, ep, price, visited):
    global arr, min_price, n
    if visited[ep] == 2 and 0 not in visited:
        if price < min_price:
            min_price = price
    else:
        for i in range(n):
            if (visited[i] == 0 or (i == ep and 0 not in visited)) and arr[sp][i]:
                visited[i] += 1
                dfs(i, ep, price+arr[sp][i], visited[:])
                visited[i] -= 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
min_price = 1000000*100+1
for i in range(n):
    visit = [0]*n
    visit[i] = 1
    dfs(i, i, 0, visit[:])
print(min_price)