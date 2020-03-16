import sys
def find(x, y):
    global n, arr, min_value
    for i in range(1, n-1):
        for j in range(1, n-i):
            if (x+i < n and y+i < n) and (x+i+j < n and y+i-j > 0) and (x+j < n and y-j > 0):
                v = [[0]*n for _ in range(n)]
                for m in range(i+1):
                    v[x+m][y+m], v[x+j+m][y-j+m] = 1, 1
                for m in range(j+1):
                    v[x+m][y-m], v[x+i+m][y+i-m] = 1, 1
                for ai in range(x+1, x+i+j):
                    flag = 0
                    for aj in range(n-1):
                        v[ai][aj] = flag
                        if v[ai][aj+1] == 1:
                            flag += 1
                            if flag == 2:
                                break
                count = [0]*5
                for ai in range(n):
                    for aj in range(n):
                        if v[ai][aj] == 0:
                            if ai < x+j and aj <= y and v[ai][aj] == 0:
                                count[0] += arr[ai][aj]
                            elif ai <= x+i and y < aj < n:
                                count[1] += arr[ai][aj]
                            elif x+j <= ai < n and aj < y-j+i:
                                count[2] += arr[ai][aj]
                            else:
                                count[3] += arr[ai][aj]
                        else:
                            count[4] += arr[ai][aj]
                min_value = min(min_value, max(count)-min(count))

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
min_value = 2**32-1
for i in range(n):
    for j in range(n):
        find(i, j)
print(min_value)