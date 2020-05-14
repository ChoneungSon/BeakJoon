n = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = list(map(int, input().split())) + [0] * (n-1-i)
    if i != 0:
        for j in range(i+1):
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
print(max(arr[n-1]))