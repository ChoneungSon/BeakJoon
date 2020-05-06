def solution(board):
    r, c, column = len(board), len(board[0]), []
    answer = 0
    def yes_no(x, y, value):
        nonlocal board, r, c, column
        column_cand = []
        for i in range(-2, 3):
            for j in range(-2, 3):
                nx, ny = x+i, y+j
                if 0 <= nx < r and 0 <= ny < c:
                    if board[nx][ny] == value:
                        if (ny not in column): column_cand.append(ny)
                        else: column += column_cand; return 1
                    if 0 <= nx-1 and board[nx-1][ny] == value and board[nx][ny] != value: column += column_cand; return 1
        return 0
    for i in range(r):
        for j in range(c):
            if board[i][j] and (j not in column):
                if yes_no(i, j, board[i][j]): continue
                else: answer += 1
    return answer


print(solution([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]))