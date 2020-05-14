def solution(p):
    if is_right(p): return p
    elif p:
        count, result = [0] * 2, ''
        for i in range(len(p)):
            if p[i] == '(': count[0] += 1
            elif p[i] == ')': count[1] += 1
            if count[0] == count[1]: break
        if is_right(p[:i+1]):
            result += p[:i+1] + solution(p[i+1:])
        else:
            add_str = ''
            for j in range(1, i):
                if p[j] == '(': add_str += ')'
                else: add_str += '('
            result += '(' + solution(p[i+1:]) + ')' + add_str
        return result
    else: return ''

def is_right(string):
    stack = []
    for i in range(len(string)):
        if not stack:
            if string[i] != '(': return 0
            else: stack.append(string[i])
        elif stack[-1] == string[i]: stack.append(string[i])
        else: stack.pop()
    if stack: return 0
    else: return 1

print(solution("()))((()"))