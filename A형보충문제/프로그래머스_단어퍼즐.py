def solution(strs, t):
    n, m = len(t), len(strs)
    dp = [20001] * (n+1)
    for i in range(1, n+1):
        for j in range(m):
            if n-i+1 >= len(strs[j]):
                for k in range(len(strs[j])):
                    if t[i+len(strs[j])-1-k] != strs[j][len(strs[j])-k]:
                        if i == len(strs[j]):
                            dp[i] = 1
                            break
                        elif dp[i-len(strs[j])] != 20001 and dp[i] > dp[i-len(strs[j])]+1:
                            dp[i] = dp[i-len(strs[j])]+1
    if dp[-1] <= 20000:
        return dp[-1]
    else:
        return -1

print(solution(["ba", "na", "n", "a"], "banana"))
