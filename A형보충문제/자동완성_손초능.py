def solution(words):
    words.sort()
    n, answer = len(words), 0
    arr = [0]*n
    for i in range(n-1):
        cnt1, cnt2 = find(words[i], words[i+1])
        arr[i], arr[i+1] = max(arr[i], cnt1), max(arr[i+1], cnt2)
    return sum(arr)

def find(s1, s2):
    cnt, i = 0, 0
    while 1:
        cnt += 1
        if i == s1.__len__(): return cnt-1, cnt
        elif i == s2.__len__(): return cnt, cnt-1
        else:
            if s1[i] != s2[i]: return cnt, cnt
        i += 1

print(solution(['go','gone','guild']))