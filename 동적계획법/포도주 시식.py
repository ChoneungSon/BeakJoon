import sys
n = int(sys.stdin.readline())
arr = [0]*n
for i in range(n):
    value = int(sys.stdin.readline())
    if i == 0: max_value = value
    elif i == 1: max_value = b_value+value
    elif i == 2: max_value = max(arr[0]+value, b_value+value, arr[i-1])
    else:
        max_value = max(arr[i-2]+value, arr[i-3]+b_value+value, arr[i-1])
    arr[i] = max_value
    b_value = value
print(arr[-1])