def solution(user_id, banned_id):
    visited, answer, n, limit, visits = [[0]*len(user_id) for _ in range(len(banned_id))], 0, len(user_id), len(banned_id), []
    for i in range(limit):
        for j in range(n):
            if equal(user_id[j], banned_id[i]):
                visited[i][j] = 1
    def find(m, visit):
        nonlocal answer, visited, n, limit, visits
        if m == limit:
            if visit not in visits:
                answer += 1
                visits.append(visit[:])
        else:
            for i in range(n):
                if visit[i] == 0 and visited[m][i]:
                    visit[i] = 1
                    find(m+1, visit[:])
                    visit[i] = 0
    find(0, [0]*n)
    return answer

def equal(cand, standard):
    if len(cand) == len(standard):
        for i in range(len(cand)):
            if standard[i] == '*': continue
            else:
                if cand[i] != standard[i]: return 0
    else: return 0
    return 1

u = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["*rodo", "*rodo", "******"]
print(solution(u, b))