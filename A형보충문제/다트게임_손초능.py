def solution(dartResult):
    answer, score, num = 0, [], ''
    for i in range(len(dartResult)):
        if dartResult[i] in ('S', 'D', 'T'):
            if dartResult[i] == 'S':
                num = int(num)
            elif dartResult[i] == 'D':
                num = int(num) ** 2
            elif dartResult[i] == 'T':
                num = int(num) ** 3
            if i < len(dartResult)-1 and dartResult[i+1] not in ('*', '#'):
                score.append(num)
                num = ''
            if i == len(dartResult)-1:
                score.append(num)
                num = ''
        elif dartResult[i] in ('*', '#'):
            if dartResult[i] == '*':
                num *= 2
                if len(score):
                    score[-1] *= 2
            else:
                num *= -1
            score.append(num)
            num = ''
        else:
            num += dartResult[i]
    return sum(score)

print(solution("1D2S#10S"))