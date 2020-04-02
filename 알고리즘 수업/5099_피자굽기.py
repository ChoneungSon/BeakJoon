T = int(input())
for case in range(1, T+1):
    n, pizza = map(int, input().split())
    c, value = list(map(int, input().split())), 0
    times = list(map(int, range(n)))
    member = [0] * n
    for i in range(pizza):
        j = 0
        while 1:
            if 2**j <= c[i] < 2**(j+1):
                count = j + 1
                break
            j += 1
        member[times.index(min(times))] = i+1
        times[times.index(min(times))] += count*n
    print('#{} {}'.format(case, member[times.index(max(times))]))