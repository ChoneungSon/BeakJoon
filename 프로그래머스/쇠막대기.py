def solution(arrangement):
    score, count = 0, 1
    for i in range(1, len(arrangement)):
        if arrangement[i] == '(':
            if arrangement[i-1] == ')':
                score += margin
                count -= margin
            count += 1
        else:
            if arrangement[i-1] == '(':
                count -= 1
                margin = 0
                score += count
            else:
                margin += 1
    score += margin
    return score

print(solution('()(((()())(())()))(())'))