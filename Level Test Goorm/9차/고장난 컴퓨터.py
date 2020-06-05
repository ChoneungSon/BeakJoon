n, limit = map(int, input().split())
arr = list(map(int, input().split()))
result = 1
for i in range(1, n):
    if arr[i] - arr[i-1] > limit: result = 1
    else: result += 1
print(result)