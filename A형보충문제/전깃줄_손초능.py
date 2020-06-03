n = int(input())
arr = [0] * 501
length = [0]*501
for _ in range(n):
    x, y = map(int, input().split())
    arr[x] = y
for i in range(1, 501):
    if arr[i]:
        d = 0
        for j in range(1, i):
            if arr[j] != 0 and arr[j] < arr[i]:
                d = max(d, length[j])
        length[i] = d+1
print(n-max(length))