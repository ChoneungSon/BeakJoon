def solution(user_id, banned_id):
    answer, adj = 0, [[0]*len(banned_id) for _ in range(len(user_id))]
    for i in range(len(user_id)):
        for j in range(len(banned_id)):
            if find(user_id[i], banned_id[j]): adj[i][j] = 1
    for i in range(len(user_id)):
        print(adj[i])
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














