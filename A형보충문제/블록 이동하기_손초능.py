def solution(board):
    n, min_cnt = len(board), 100 * 100 + 101
    move = [[[1, 0], [1, 0]], [[0, 1], [0, 1]], [[-1, 0], [-1, 0]], [[0, -1], [0, -1]]]
    turn = [[[0, 1], [1, 0]], [[0, 0], [1, -1]], [[-1, 0], [0, -1]], [[-1, 1], [0, 0]]]
    visited1 = [[0] * (n+2) for _ in range(n+2)]
    visited2 = [[0] * (n+2) for _ in range(n+2)]
    visited3 = [[0] * (n+2) for _ in range(n+2)]
    visited4 = [[0] * (n+2) for _ in range(n+2)]
    visited1[1][1] = visited2[1][2] = 1

    board = [[1] * (n+2)] + [[1] + board[i] + [1] for i in range(n)] + [[1] * (n+2)]
    robot = [[1, 1], [1, 2], 0]
    def dfs(point, cnt):
        nonlocal board, min_cnt, visited1, visited2, visited3, visited4, n, move, turn
        if point[1] == [n, n]: min_cnt = min(min_cnt, cnt)
        elif cnt >= min_cnt: return
        else:
            for i in range(4):
                x1, y1 = point[0][0]+move[i][0][0], point[0][1]+move[i][0][1]
                x2, y2 = point[1][0]+move[i][1][0], point[1][1]+move[i][1][1]
                print(x1, x2, y1, y2)
                if board[x1][y1] == 0 and board[x2][y2] == 0:
                    if point[2] == 0:
                        if visited1[x1][y1] == 0 and visited2[x2][y2] == 0:
                            visited1[x1][y1] = visited2[x2][y2] = 1
                            dfs([[x1, y1], [x2, y2], point[2]], cnt+1)
                            visited1[x1][y1] = visited2[x2][y2] = 0
                    else:
                        if visited3[x1][y1] == 0 and visited4[x2][y2] == 0:
                            visited3[x1][y1] = visited4[x2][y2] = 1
                            dfs([[x1, y1], [x2, y2], point[2]], cnt+1)
                            visited3[x1][y1] = visited4[x2][y2] = 0
            if point[2] == 0:
                x_set = {point[0][0], point[1][0]}
                y_set = {point[0][1], point[1][1]}
                x1, y1 = point[0][0]+turn[i][0][0], point[0][1]+turn[i][0][1]
                x2, y2 = point[1][0]+turn[i][1][0], point[1][1]+turn[i][1][1]
                x_set.add(x1); x_set.add(x2)
                y_set.add(y1); y_set.add(y2)
                if point[2] == 0:
                    count = 0
                    for x in x_set:
                        for y in y_set:
                           if board[x][y] == 0: count += 1
                    if count == 4:
                        if visited3[x1][y1] == 0 and visited4[x2][y2] == 0:
                            visited3[x1][y1] = visited4[x2][y2] = 1
                            dfs([[x1, y1], [x2, y2], (point[2]+1)%2], cnt+1)
                            visited3[x1][y1] = visited4[x2][y2] = 0
                else:
                    count = 0
                    for x in x_set:
                        for y in y_set:
                            if board[x][y] == 0: count += 1
                    if count == 4:
                        if visited1[x1][y1] == 0 and visited2[x2][y2] == 0:
                            visited1[x1][y1] = visited2[x2][y2] = 1
                            dfs([[x1, y1], [x2, y2], (point[2]+1)%2], cnt+1)
                            visited1[x1][y1] = visited2[x2][y2] = 0
    dfs(robot, 0)
    return min_cnt

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))