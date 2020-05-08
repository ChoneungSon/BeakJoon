import pprint
def solution(board):
    r, c, column = len(board), len(board[0]), []
    answer, visited = 0, [0] * c
    def yes_no(x, y, value):
        nonlocal board, r, c, column, visited, answer
        point, flag = [], 0
        for i in range(-2, 3):
            for j in range(-2, 3):
                nx, ny = x+i, y+j
                if 0 <= nx < r and 0 <= ny < c:
                    if board[nx][ny] == value:
                        point.append((nx, ny))
                        if flag==0 and visited[ny]: flag = 1
                    elif nx-1 >= 0 and flag==0:
                        if ny-1 >= 0 and board[nx-1][ny]==value and board[nx][ny-1]==value and board[nx-1][ny-1]==value: flag = 1
                        if ny+1 < c and board[nx-1][ny]==value and board[nx][ny+1]==value and board[nx-1][ny+1]==value: flag = 1
        for i in range(4):
            board[point[i][0]][point[i][1]] = 0
            if flag: visited[point[i][1]] = 1
        if flag == 0: answer += 1
    for i in range(r):
        for j in range(c):
            if board[i][j]:
                yes_no(i, j, board[i][j])
    return answer


print(solution(
    [[0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,4,0,0,0],
     [0,0,0,0,0,4,4,0,0,0],
     [0,0,0,0,3,0,4,0,0,0],
     [0,0,0,2,3,0,0,0,5,5],
     [1,2,2,2,3,3,0,0,0,5],
     [1,1,1,0,0,0,0,0,0,5]]))
print(solution(
    [[6,6,6,7,7,7,8,8,8,0],
     [0,0,6,7,0,0,0,8,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,4,0,0,0,0],
     [0,0,0,0,3,4,0,0,0,0],
     [0,0,2,0,3,4,4,0,5,5],
     [1,2,2,2,3,3,0,0,0,5],
     [1,1,1,0,0,0,0,0,0,5]]))