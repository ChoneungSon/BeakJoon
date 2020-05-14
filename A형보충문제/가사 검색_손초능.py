class Word:
    def __init__(self):
        self.count = 1
        self.next = {}

def solution(words, queries):
    front, back, answer = {}, {}, [0]*len(queries)
    for i in range(len(words)):
        if len(words[i]) not in front:
            front[len(words[i])], back[len(words[i])] = Word(), Word()
        else:
            front[len(words[i])].count += 1
            back[len(words[i])].count += 1
        f, b = front[len(words[i])], back[len(words[i])]
        for j in range(len(words[i])):
            if words[i][j] in f.next: f.next[words[i][j]].count += 1
            else: f.next[words[i][j]] = Word()
            if words[i][len(words[i])-j-1] in b.next: b.next[words[i][len(words[i])-j-1]].count += 1
            else: b.next[words[i][len(words[i])-j-1]] = Word()
            f, b = f.next[words[i][j]], b.next[words[i][len(words[i])-1-j]]
    for i in range(len(queries)):
        if len(queries[i]) not in front: continue
        if queries[i][0] == '?': find, cnt, q = back[len(queries[i])], back[len(queries[i])].count, queries[i][::-1]
        else: find, cnt, q = front[len(queries[i])], front[len(queries[i])].count, queries[i]
        for j in range(len(q)):
            if q[j] == '?':
                answer[i] = cnt
                break
            if q[j] in find.next: find = find.next[q[j]]
            else: break
            cnt = find.count
        else:
            answer[i] = cnt
    return answer


def solution1(words, queries):
    front, back, answer = {}, {}, [0] * len(queries)
    for i in range(len(words)):
        if len(words[i]) in front:
            front[len(words[i])]['count'] += 1
            back[len(words[i])]['count'] += 1
        else:
            front[len(words[i])], back[len(words[i])] = {'count':1 }, {'count':1 }
        f, b = front[len(words[i])], back[len(words[i])]
        for j in range(len(words[i])):
            if words[i][j] in f: f[words[i][j]]['count'] += 1
            else: f[words[i][j]] = {'count': 1}
            if words[i][len(words[i])-j-1] in b: b[words[i][len(words[i])-j-1]]['count'] += 1
            else: b[words[i][len(words[i])-j-1]] = {'count': 1}
            f, b = f[words[i][j]], b[words[i][len(words[i])-j-1]]
    for i in range(len(queries)):
        if len(queries[i]) not in front: continue
        if queries[i][0] == '?': find, cnt, q = back[len(queries[i])], back[len(queries[i])]['count'], queries[i][::-1]
        else: find, cnt, q = front[len(queries[i])], front[len(queries[i])]['count'], queries[i]
        for j in range(len(q)):
            if q[j] == '?' or cnt == 1: answer[i] = cnt; break
            elif q[j] not in find: break
            else: find = find[q[j]]; cnt = find['count']
    return answer

print(solution1(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["fro??", "????o", "fr???", "fro???", "pro?", "a????"]
))

print(solution1(
    ["abcde", "aabcc", "aaaaa", "bbbbb", "ababa", "babab"],
    ["a????", "????c", "ab???", "abc???", "bb???", "ba???"]
))