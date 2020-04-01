def solution(m, n, board):
    arr = [list(board[i]) for i in range(m)]
    def find(r, c, d):
        nonlocal arr, m, n
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        value = arr[r][c]
        visit = [(r, c)]
        for i in range(1, 4):
            r, c = r + di[(d+i)%4], c + dj[(d+i)%4]
            if not(0 <= r < m and 0 <= c < n and arr[r][c] == value):
                return 0
            visit.append((r, c))
        return visit

    def bfs(r, c):
        nonlocal arr, m, n
        visit = [[0]*n for _ in range(m)]
        q, flag = [], 0
        for i in range(4):
            evalu = find(r, c, i)
            if evalu:
                for j in range(4):
                    if visit[evalu[j][0]][evalu[j][1]] == 0:
                        q.append(evalu[j][:])
                        visit[evalu[j][0]][evalu[j][1]] = 1
        while q:
            x, y = q.pop(0)
            for i in range(4):
                evalu = find(x, y, i)
                if evalu:
                    for j in range(4):
                        if visit[evalu[j][0]][evalu[j][1]] == 0:
                            q.append(evalu[j][:])
                            visit[evalu[j][0]][evalu[j][1]] = 1
        for i in range(m):
            for j in range(n):
                if visit[i][j] == 1:
                    arr[i][j] = '0'
                    flag += 1
        return flag

    score = 0
    while 1:
        cnt = 0
        for i in range(m):
            for j in range(n):
                if arr[i][j] != '0':
                    cnt += bfs(i, j)
        if cnt:
            score += cnt
            for i in range(n):
                for j in range(m-1, 0, -1):
                    if arr[j][i] == '0':
                        p, flag = j, 1
                        while p > 0:
                            p -= 1
                            if arr[p][i] != '0':
                                arr[j][i], arr[p][i], flag = arr[p][i], arr[j][i], 0
                                break
                        if flag: break
        else: break
    return score

print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))