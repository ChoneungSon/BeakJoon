def solution(n, t, m, p):
    result, answer, cnt, i, num = '', '', 0, -1, 0
    while 1:
        string, length = mknum(n, num)
        result += string
        for j in range(1, length+1):
            i += 1
            if i % m == p-1:
                answer += result[i]
                cnt += 1
                if cnt == t:
                    return answer
        num += 1

def mknum(n, num):
    nums = '0123456789ABCDEF'
    result = ''
    while num >= n:
        result = str(nums[num % n]) + result
        num //= n
    result = str(nums[num]) + result
    return result, len(result)

print(solution(16, 16, 2, 2))