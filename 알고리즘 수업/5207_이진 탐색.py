def bin_find(num):
    global A, n
    l, r, direction = 0, n-1, ''
    while l <= r:
        middle = (l + r) // 2
        if A[middle] > num:
            if direction == 'l': return 0
            else: direction, r = 'l', middle-1
        elif A[middle] < num:
            if direction == 'r': return 0
            else: direction, l = 'r', middle+1
        else: return 1
    return 0

for case in range(1, int(input())+1):
    n, m = map(int, input().split())
    cnt = 0
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    for i in range(m):
        cnt += bin_find(B[i])
    print('#{} {}'.format(case, cnt))

