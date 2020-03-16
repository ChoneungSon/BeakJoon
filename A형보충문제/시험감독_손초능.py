import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
main, sub = map(int, sys.stdin.readline().split())
total = 0
for i in range(n):
    if main < arr[i]:
        if (arr[i]-main) % sub:
            total += (arr[i]-main)//sub + 2
        else:
            total += (arr[i]-main)//sub + 1
    else:
        total += 1
print(total)