for case in range(1, int(input())+1):
    n = int(input())
    arr, point, result = [0]*(n+1), 1, 0
    nums = list(map(int, input().split()))
    for i in range(n):
        arr[point], m, p = nums[i], point//2, point
        while m:
            if arr[m] > arr[p]:
                arr[m], arr[p] = arr[p], arr[m]
                p = m; m //= 2
            else: break
        point += 1
    while n:
        n //= 2
        result += arr[n]
    print('#{} {}'.format(case, result))