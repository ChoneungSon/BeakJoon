import sys
n = int(sys.stdin.readline())
for i in range(1, n+1):
    m = i
    s = i
    while m != 0:
        s += m % 10
        m //= 10
    if s == n:
        print(i)
        break
else:
    print(0)