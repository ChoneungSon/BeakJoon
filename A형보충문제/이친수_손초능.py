n = int(input())
arr = [0] * 91
arr[0] = arr[1] = 1
for i in range(2, n+1):
    arr[i] = sum(arr[:i-1])
print(arr[n])