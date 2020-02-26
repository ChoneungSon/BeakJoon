T = int(input())
for _ in range(T):
    n, p = map(int, input().split())
    arr = list(map(int, input().split()))
    mp, count = -1, 0
    visit = [0]*n
    while 1:
        max_amp = 0
        for i in range(n):
            if arr[i] > max_amp and visit[i] == 0:
                max_amp = arr[i]
        while 1:
            mp = (mp+1)%n
            if arr[mp] == max_amp and visit[mp] == 0:
                visit[mp] = 1
                count += 1
                break
        if mp == p:
            print(count)
            break