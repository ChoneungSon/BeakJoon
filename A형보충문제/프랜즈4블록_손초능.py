def solution(m, n, board):
    def find(r, c, d):
        nonlocal board, m, n
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        value = board[r][c]
        for i in range(1, 3):
            r, c = r + di[(d+i)%4], c + dj[(d+i)%4]
            if not(0 <= r < m and 0 <= c < n and board[r][c] != value):
                return 0
        return 1
    for i in range(m):
        for j in range(n):
            


    return answer