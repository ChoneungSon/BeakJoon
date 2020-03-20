def solution(strs, t):
    n, m = len(t), len(strs)
    dp = [20001] * (n+1)
    for i in range(1, n+1):
        for j in range(m, 0, -1):
            if n >= len(strs[j]):
                if t[i-j:i] == strs[j]:
                    if i == j:
                        dp[i] = 1
                        break
                    elif dp[i-j] != 20001 and dp[i] > dp[i-j]+1:
                        dp[i] = dp[i-j]+1
    if dp[-1] <= 20000:
        return dp[-1]
    else:
        return -1

print(solution(["ba", "an", "nan", "ban", "n"], "banana"))
