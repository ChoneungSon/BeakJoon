def solution(N, number):
    total, n = 0, number
    while n > N:
        cnt = 0
        while n > N:
            n //= N
            cnt += 1
        total += cnt
        n = number - N**cnt
        number = n
    return total

print(solution(5, 12))