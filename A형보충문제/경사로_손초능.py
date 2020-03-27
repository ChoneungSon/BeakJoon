import sys
n, L = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    length, j, flag1 = 1, 1, 1
    while j < n:
        if abs(arr[i][j-1] - arr[i][j]) > 1: flag1 = 0; break
        elif arr[i][j-1] == arr[i][j]: length += 1
        elif arr[i][j-1] - arr[i][j] == -1:
            if length >= L: length = 1
            else: flag1 = 0; break
        elif arr[i][j-1] - arr[i][j] == 1:
            if j+L-1 < n:
                for k in range(1, L):
                    if arr[i][j] != arr[i][j+k]: flag1 = 0; break
                else:
                    j += L
                    length = 1
            else: flag1 = 0; break
        if flag1 == 0: break
        j += 1
    cnt += flag1
    print(i, cnt)
    length, j, flag2 = 1, 1, 1
    while j < n:
        if abs(arr[j-1][i] - arr[j][i]) > 1: flag2 = 0; break
        elif arr[j-1][i] == arr[j][i]: length += 1
        elif arr[j-1][i] - arr[j][i] == -1:
            if length >= L: length = 1
            else: flag2 = 0; break
        elif arr[j-1][i] - arr[j][i] == 1:
            if j + L - 1 < n:
                for k in range(1, L):
                    if arr[j][i] != arr[j+k][i]: flag2 = 0; break
                else:
                    j += L
                    length = 1
            else: flag2 = 0; break
        if flag2 == 0: break
        j += 1
    cnt += flag2
    print(i, cnt)
print(cnt)