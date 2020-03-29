def solution(k, room_number):
    answer, n = [], len(room_number)
    def find(a):
        nonlocal answer
        for i in range(answer):
            if a == answer[i]:
                return 0
        return 1
    for i in range(n):
        if find(room_number[i]):
            answer.append(room_number[i])
        else:
            p = room_number[i]
            while 1:
                p += 1
                if find(p):
                    answer.append(p)
                    break
    return answer

import pprint

pprint.pprint(solution(10**12, list(map(int, range(1, 200001)))))