def dfs(cnt):
    global num, change, odd, even, max_value
    if cnt%2 and int(''.join(num)) in odd: return
    elif cnt%2==0 and int(''.join(num)) in even: return
    else:
        if cnt % 2: odd.append(int(''.join(num)))
        else: even.append(int(''.join(num)))
    if cnt == change: return
    else:
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                num[i], num[j] = num[j], num[i]
                dfs(cnt+1)
                num[i], num[j] = num[j], num[i]

for case in range(1, int(input())+1):
    num, change = input().split()
    num, change = list(num), int(change)
    odd, even = [], []
    dfs(0)
    result = max(odd) if change%2 else max(even)
    print('#{} {}'.format(case, result))