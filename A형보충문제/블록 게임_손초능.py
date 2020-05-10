import pprint
# def yes_no(board, visit, i, j, r, c):
#     nonlocal answer
#     visited = [[0] * c for _ in range(r)]
#     visited[i][j], flag, value = 1, 0, board[i][j]
#     q = [(i, j)]; dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
#     x_list, y_list, point = [i], [j], []
#     while q:
#         x, y = q.pop(0)
#         for k in range(4):
#             nx, ny = x + dx[k], y + dy[k]
#             if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == value and visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 q.append((nx, ny))
#                 if nx not in x_list: x_list.append(nx)
#                 if ny not in y_list: y_list.append(ny)
#     for k in range(len(x_list)):
#         for m in range(len(y_list)):
#             point.append((x_list[k], y_list[m]))
#     print(point)
#     for k in range(6):
#         x, y = point[k]
#         if x - 1 >= 0 and board[x][y] != value and board[x - 1][y] == value:
#             flag = 1;
#         if x - 1 >= 0 and board[x][y] == value and board[x - 1][y] != 0 and board[x - 1][y] != value:
#             return;
#         if board[x][y] != value and visit[y]:
#             flag = 1;
#     for k in range(6):
#         if board[point[k][0]][point[k][1]] == value: board[point[k][0]][point[k][1]] = 0
#     if flag:
#         for k in range(len(y_list)): visit[y_list[k]] = 1
#     else:
#         answer += 1
#     print(visit)
#     print(answer)
#
# def solution(board):
#     r, c = len(board), len(board[0])
#     answer, visit = 0, [0]*c
#     def yes_no(board, visit, i, j, r, c):
#         nonlocal answer
#         visited = [[0] * c for _ in range(r)]
#         visited[i][j], flag, value = 1, 0, board[i][j]
#         q = [(i, j)];
#         dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
#         x_list, y_list, point = [i], [j], []
#         while q:
#             x, y = q.pop(0)
#             for k in range(4):
#                 nx, ny = x + dx[k], y + dy[k]
#                 if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == value and visited[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     q.append((nx, ny))
#                     if nx not in x_list: x_list.append(nx)
#                     if ny not in y_list: y_list.append(ny)
#         for k in range(len(x_list)):
#             for m in range(len(y_list)):
#                 point.append((x_list[k], y_list[m]))
#         print(point)
#         for k in range(6):
#             x, y = point[k]
#             if x - 1 >= 0 and board[x][y] != value and board[x - 1][y] == value:
#                 flag = 1;
#             if x - 1 >= 0 and board[x][y] == value and board[x - 1][y] != 0 and board[x - 1][y] != value:
#                 return;
#             if board[x][y] != value and visit[y]:
#                 flag = 1;
#         for k in range(6):
#             if board[point[k][0]][point[k][1]] == value: board[point[k][0]][point[k][1]] = 0
#         if flag:
#             for k in range(len(y_list)): visit[y_list[k]] = 1
#         else:
#             answer += 1
#     for i in range(r):
#         for j in range(c):
#             if board[i][j]:
#                 yes_no(board, visit, i, j, r, c)
#                 pprint.pprint(board)
#     return answer


def solution1(board):
    r, c, answer = len(board), len(board[0]), 0
    def paint():
        nonlocal board, r, c
        flag = 0
        for i in range(c):
            for j in range(r):
                if board[j][i] == 0:
                    flag, board[j][i] = 1, 201
                elif board[j][i] == 201: continue
                else: break
        return flag
    def yes_no(x, y, value):
        nonlocal board, r, c, visited, answer
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        x_list, y_list, q, point = [], [], [(x, y)], []
        while q:
            x, y = q.pop(0)
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and board[nx][ny] == value:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    if nx not in x_list: x_list.append(nx)
                    if ny not in y_list: y_list.append(ny)
        for i in range(len(x_list)):
            for j in range(len(y_list)):
                point.append((x_list[i], y_list[j]))
        if point:
            for i in range(6):
                if board[point[i][0]][point[i][1]] != value and board[point[i][0]][point[i][1]] != 201: return
            answer += 1
            for i in range(6):
                board[point[i][0]][point[i][1]] = 0
        else: return
    while paint():
        pprint.pprint(board)
        visited = [[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j] != 0 and board[i][j] != 201:
                    yes_no(i, j, board[i][j])
    return answer

print(solution1(
    [[0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,3,0,4,0,0,0],
     [0,0,0,2,3,4,4,0,5,5],
     [1,2,2,2,3,3,4,0,0,5],
     [1,1,1,0,0,0,0,0,0,5]]))
print(solution1(
    [[0,0,6,7,0,0,0,8,0,0],
     [6,6,6,7,7,7,8,8,8,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,9,9,4,0,0,0,0],
     [0,0,0,9,3,4,0,0,0,0],
     [0,0,2,9,3,4,4,0,0,5],
     [1,2,2,2,3,3,0,0,0,5],
     [1,1,1,0,0,0,0,0,5,5]]))