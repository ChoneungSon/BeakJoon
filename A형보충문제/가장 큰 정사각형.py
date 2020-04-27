r, c = map(int, input().split())
arr = [list(map(int, input())) for _ in range(r)]
max_value = 0
for i in range(1, r):
    for j in range(1, c):
        if arr[i][j]:
            arr[i][j] = min(arr[i-1][j], arr[i-1][j-1], arr[i][j-1]) + 1
for i in range(r):
    max_value = max(max_value, max(arr[i]))
print(max_value**2)