import sys
case = int(sys.stdin.readline())
for _ in range(case):
    n = int(sys.stdin.readline())
    memo = [0] * (n+1)
    memo[1] = 1 # 1을 만드는 경우의 수는 1개 존재한다.
    for i in range(2, n+1):
        if i == 2: memo[i] = memo[1] + 1 # 2를 만드는 경우
        elif i == 3: memo[i] = memo[1] + memo[2] + 1 # 3을 만드는 경우
        else: memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        # 이외의 값에서는 원하는 값에서 1, 2, 3을 뺀 값들의 경우의 수의 합을 대입하면 된다.
    print(memo[n])