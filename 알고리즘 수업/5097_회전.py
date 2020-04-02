T = int(input())
for case in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(case, arr[m % n]))