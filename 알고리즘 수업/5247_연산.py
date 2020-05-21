for case in range(1, int(input())+1):
    n, m = map(int, input().split())
    fun = [-1, 1, -10]
    arr = [-1] * 10000001
    arr[n] = 0
    for i in range(n, m):
        for j in range(3):
            nx = i+fun[j]
            if 1 <= nx <= 1000000:
                if arr[nx] == -1: arr[nx] = arr[i]+1
                else: arr[nx] = min(arr[nx], arr[i]+1)
        if 1 <= 2*i <= 1000000:
            if arr[2*i] == -1: arr[2*i] = arr[i]+1
            else: arr[2*i] = min(arr[2*i], arr[i] + 1)
    print('#{} {}'.format(case, arr[m]))