def solution(N, stages):
    user = [0]*(N+2)
    stay = [0]*(N+2)
    for i in range(len(stages)):
        stay[stages[i]] += 1
        for j in range(1, stages[i]+1):
            user[j] += 1
    for i in range(1, N+1):
        if user[i]: stay[i] = stay[i] / user[i]
    answer = sorted(range(1, N+1), key=lambda x:stay[x], reverse=True)
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))