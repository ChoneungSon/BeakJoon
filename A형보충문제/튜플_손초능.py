def solution(s):
    lsts, answer = s[2:-1].split(',{'), []
    for i in range(len(lsts)):
        idx = i
        for j in range(i, len(lsts)):
            if lsts[idx].__len__() > lsts[j].__len__():
                idx = j
        lsts[idx], lsts[i] = lsts[i], lsts[idx]
        for num in map(int, lsts[i][:-1].split(',')):
            if num not in answer:
                answer.append(num)
    return answer

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))