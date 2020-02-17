import sys
def f(m):
    cnt = 0
    while m != 0:
        r = m % 10
        m //= 10
        cnt += 1
        if cnt == 2:
            diff = b_r - r
        elif cnt > 2:
            if diff != b_r - r:
                return 0
        b_r = r
    return 1

n = int(sys.stdin.readline())
count = 0
for i in range(1, n+1):
    if f(i):
        count += 1
print(count)