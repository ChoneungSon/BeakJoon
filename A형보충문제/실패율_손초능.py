def solution(N, stages):
    user = [0]*(N+2) # 인덱스와 스테이지를 일치시키기 위해 
    stay = [0]*(N+2) # 또한, 전부 클리어한 유저를 저장시키기 위해
    for i in range(len(stages)):
        stay[stages[i]] += 1 # 해당 스테이지에 머물러 있는 유저의 수를 저장
        for j in range(1, stages[i]+1):
            user[j] += 1
            # 해당 스테이지 이전 단계는 모두 통과한 상태이므로 이전 스테이지 이용 유저를 저장
    for i in range(1, N+1):
        # 해당 zero division error를 발생시키지 않기 위해 이용 유저의 수가 0이 아닌 경우 실패율을 저장
        if user[i]: stay[i] = stay[i] / user[i]
    # 실패율을 기준으로 내림차순 정렬
    answer = sorted(range(1, N+1), key=lambda x:stay[x], reverse=True)
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))