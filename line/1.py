def solution(inputString):
    open = ['(', '{', '[', '<']
    close = [')', '{', ']', '>']
    stack, cnt = [], 0
    for i in range(inputString.__len__()):
        if inputString[i] in open:
            stack.append(inputString[i])
        elif inputString[i] in close:
            if stack:
                stack.pop()
                cnt += 1
            else: return -1
    return cnt

print(solution('> <'))