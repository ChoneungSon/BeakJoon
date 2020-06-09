def solution(cookie):
    answer = -1
    n = len(cookie)
    cookies = [0] * (n+1)
    for i in range(1, n+1):
        cookies[i] = cookies[i-1] + cookie[i-1]

    for i in range(1, n+1):
        if num % 2 == 0:
            num //= 2
            left, right = idx, n
            while left < right:
                mid = (left+right) // 2
                if cookies[mid]
                if cookies
    return answer