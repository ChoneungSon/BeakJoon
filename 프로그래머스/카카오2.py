def solution(s):
    stack, num_str = [0]*1000, ''
    for i in range(1, len(s)-1):
        if s[i] == '{':
            arr = []
        elif s[i] == '}':
            arr.append(int(num_str))
            stack[len(arr)] = arr[:]
            num_str = ''
        elif num_str and s[i] == ',':
            arr.append(int(num_str))
            num_str = ''
        elif s[i] != ',': num_str += s[i]
    i, result = 1, []
    while stack[i]:
        for j in range(i):
            if stack[i][j] not in result:
                result.append(stack[i][j])
        i += 1
    return result


print(solution("{{1,111},{111}}"))