T = [0]*31
T[0] = T[1] = 1; T[2] = 3; T[3] = 6
for case in range(1, int(input())+1):
    n = int(input())
    for i in range(2, n+1):
        if T[i] == 0:
            T[i] = T[i-1] + 2 * T[i-2] + T[i-3]
    print('#{} {}'.format(case, T[n]))