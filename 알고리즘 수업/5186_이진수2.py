for case in range(1, int(input())+1):
    n = float(input())
    num, cnt = ['0'] * 12, 0
    while cnt < 12:
        if n - 1/(2**(cnt+1)) >= 0:
            num[cnt] = '1'
            n -= 1/(2**(cnt+1))
            if n == 0: cnt+=1; break
        cnt += 1
    if n: print('#{} overflow'.format(case))
    else: print('#{} {}'.format(case, "".join(num[:cnt])))