def solution(triangle):
    for i in range(len(triangle)-1):
        visit = [0] * (i+2)
        for j in range(i+1):
            visit[j] = max(visit[j], triangle[i+1][j]+triangle[i][j])
            visit[j+1] = max(visit[j+1], triangle[i+1][j+1] + triangle[i][j])
        triangle[i+1] = visit[:]
    return max(triangle[len(triangle)-1])

print(solution([[7], [3, 8], [8, 1, 0]]))