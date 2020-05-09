import pprint
def solution(board):
    r, c = len(board), len(board[0])
    dx, dy = [0, 1, 0], [1, 0, -1]
    answer, visited, visit = 0, [[0] * c for _ in range(r)], [0] * c
    for i in range(r):
        for j in range(c):
            if board[i][j]:
                visited[i][j], flag, value = 1, 0, board[i][j]
                q = [(i, j)]
                x_list, y_list, point = [i], [j], []
                while q:
                    x, y = q.pop(0)
                    for k in range(3):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == value and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                            if nx not in x_list: x_list.append(nx)
                            if ny not in y_list: y_list.append(ny)
                for k in range(len(x_list)):
                    for m in range(len(y_list)):
                        point.append((x_list[k], y_list[m]))
                for k in range(6):
                    x, y = point[k]
                    if x-1 >= 0 and board[x][y] != value and board[x-1][y] == value:
                        flag = 1; break
                    if board[x][y] != value and visit[y]:
                        flag = 1; break
                for k in range(6):
                    if board[point[k][0]][point[k][1]] == value: board[point[k][0]][point[k][1]] = 0
                if flag:
                    for k in range(len(y_list)): visit[y_list[k]] = 1
                else: answer += 1
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