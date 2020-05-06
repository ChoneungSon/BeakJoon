import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(3):
        min_value = 2**31-1
        for k in range(3):
            if j != k: min_value = min(min_value, arr[i][j]+arr[i-1][k])
        arr[i][j] = min_value
print(min(arr[n-1]))

