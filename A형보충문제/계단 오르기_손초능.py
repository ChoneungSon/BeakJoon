n = int(input())
arr, sum1, sum2 = [0] * n, [0] * n, [0] * n
for i in range(n):
    arr[i] = int(input())
sum1[0] = arr[0]
if n >= 2: sum1[1], sum2[1] = arr[0] + arr[1], arr[1]
for i in range(2, n):
    sum2[i] = arr[i] + max(sum1[i-2], sum2[i-2])
    sum1[i] = arr[i] + sum2[i-1]
print(max(sum1[n-1], sum2[n-1]))

#      i-2        i
# i-3       i-1   i