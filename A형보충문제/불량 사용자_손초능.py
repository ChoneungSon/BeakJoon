def solution(user_id, banned_id):
    answer, adj, visited = 0, [[0]*len(banned_id) for _ in range(len(user_id))], []
    for i in range(len(user_id)):
        for j in range(len(banned_id)):
            if find(user_id[i], banned_id[j]): adj[i][j] = 1
    def dfs(visit, cnt):
        nonlocal user_id, banned_id, answer, visited
        if cnt == len(banned_id):
            if visit not in visited:
                visited.append(visit[:])
                answer += 1
        else:
            for i in range(len(user_id)):
                if adj[i][cnt] and visit[i] == 0:
                    visit[i] = 1
                    dfs(visit[:], cnt+1)
                    visit[i] = 0
    dfs([0]*len(user_id), 0)
    return answer

def find(str1, str2):
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str2[i] == '*': continue
            elif str1[i] != str2[i]: return 0
        return 1
    else: return 0

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))














