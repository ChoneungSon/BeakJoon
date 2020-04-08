def solution(msg):
    dic, answer, i = list(map(chr, range(65, 91))), [], 0
    while i < len(msg):
        j, num = 0, 0
        while i+j < len(msg):
            if msg[i:i+j+1] in dic:
                num = dic.index(msg[i:i+j+1])
                if i+j == len(msg)-1:
                    answer.append(num+1)
                    i += j
                    break
            else:
                dic.append(msg[i:i+j+1])
                answer.append(num+1)
                i += j-1
                break
            j += 1
        i += 1
    return answer

print(solution('TOBEORNOTTOBEORTOBEORNOT'))