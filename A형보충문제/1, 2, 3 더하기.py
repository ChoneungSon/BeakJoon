import sys
case = int(sys.stdin.readline())
for _ in range(case):
    n = int(sys.stdin.readline())
    memo = [0] * (n+1)
    memo[1] = 1
    for i in range(2, n+1):
        if i == 2: memo[i] = memo[1] + 1
        elif i == 3: memo[i] = memo[1] + memo[2] + 1
        else: memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    print(memo[n])