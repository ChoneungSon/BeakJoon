import sys
n, k = map(int, sys.stdin.readline().split())
if n == 3:
    print('NO')
elif n == 2:
    print('YES')
    for i in range(5):
        print('swap 1 2')
else:
    print('YES')
    if k == 1:
        print('reverse 2 {}'.format(n))
        print('reverse 2 {}'.format(n))
        print('reverse 2 {}'.format(n))
        print('swap 1 {}'.format(n))
        print('reverse 2 {}'.format(n-1))
    elif k == n-1:
        print('reverse 1 {}'.format(k))
        print('reverse 1 {}'.format(k))
        print('reverse 1 {}'.format(k))
        print('swap 1 {}'.format(n))
        print('reverse 2 {}'.format(n-1))
    else:
        print('reverse 1 {}'.format(k))
        print('reverse {} {}'.format(k+1, n))
        print('reverse 1 {}'.format(n))
        print('reverse 1 {}'.format(n))
        print('reverse 1 {}'.format(n))