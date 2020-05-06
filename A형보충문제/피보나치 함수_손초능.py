import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    dp = [[0]*2 for _ in range(n+1)]
    for i in range(n+1):
        if i == 0: dp[0] = [1, 0]
        elif i == 1: dp[1] = [0, 1]
        else:
            dp[i] = [dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]]
    print(dp[n][0], dp[n][1])
