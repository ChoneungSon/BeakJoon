for case in range(1, int(input())+1):
    n = int(input())
    times, count = [0] * n, [0] * (n + 1)
    for i in range(n):
        times[i] = list(map(int, input().split()))
    times = [[0, 0]] + sorted(times, key=lambda x: x[0])
    for i in range(1, n+1):
        idx = 0
        for j in range(i):
            if times[j][1] <= times[i][0] and count[j] > count[idx]: idx = j
        count[i] = count[idx] + 1
    print('#{} {}'.format(case, max(count)))