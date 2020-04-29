import sys
n = int(sys.stdin.readline())
memo = [0] * (n+1)
for i in range(2, n+1):
    min_value = n + 1
    if i % 3 == 0:
        min_value = min(min_value, memo[i//3] + 1)
    if i % 2 == 0:
        min_value = min(min_value, memo[i//2] + 1)
    min_value = min(min_value, memo[i-1] + 1)
    memo[i] = min_value
print(memo[n])
