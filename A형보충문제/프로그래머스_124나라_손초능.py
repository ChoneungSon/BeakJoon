def solution(n): # 0을 4로 보는 3진법과 같음
    result = ''
    while n > 0:
        remain = n % 3
        if remain == 0:
            result = '4' + result
            n -= 3
        else:
            result = str(remain) + result
        n //= 3
    return result