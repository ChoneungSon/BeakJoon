def solution(board):
    n, INF = len(board), float('inf')
    move = [[[1, 0], [1, 0]], [[0, 1], [0, 1]], [[-1, 0], [-1, 0]], [[0, -1], [0, -1]]]
    turn = [
        [[[0, 1], [1, 0]], [[0, 0], [1, -1]], [[-1, 0], [0, -1]], [[-1, 1], [0, 0]]],
        [[[0, 0], [-1, 1]], [[0, -1], [-1, 0]], [[1, -1], [0, 0]], [[1, 0], [0, 1]]],
    ]
    visited = [[INF]*(n+2) for _ in range(n+2)]
    visited[1][1] = visited[1][2] = 0
    board = [[1] * (n+2)] + [[1] + board[i] + [1] for i in range(n)] + [[1] * (n+2)]
    q = [((1,1),(1,2),0)]
    while q:
        point1, point2, dest = q.pop(0)
        for i in range(4):
            x1, y1 = point1[0] + move[i][0][0], point1[1] + move[i][0][1]
            x2, y2 = point2[0] + move[i][1][0], point2[1] + move[i][1][1]
            if board[x1][y1] == board[x2][y2] == 0 and (visited[x1][y1] >= visited[point1[0]][point1[1]]+1 or visited[x2][y2] >= visited[point2[0]][point2[1]]+1):
                if visited[x1][y1] >= visited[point1[0]][point1[1]]+1: visited[x1][y1] = visited[point1[0]][point1[1]] + 1
                elif visited[x2][y2] >= visited[point2[0]][point2[1]]+1: visited[x2][y2] = visited[point2[0]][point2[1]] + 1
                q.append(((x1, y1), (x2,y2), dest))
        for i in range(4):
            x_set, y_set, count = {point1[0], point2[0]}, {point1[1], point2[1]}, 0
            x1, y1 = point1[0] + turn[dest][i][0][0], point1[1] + turn[dest][i][0][1]
            x2, y2 = point2[0] + turn[dest][i][1][0], point2[1] + turn[dest][i][1][1]
            x_set.add(x1); x_set.add(x2); y_set.add(y1); y_set.add(y2)
            for x in x_set:
                for y in y_set:
                    if board[x][y] == 0: count+=1
            if count == 4 and board[x1][y1] == board[x2][y2] == 0 and (visited[x1][y1] >= visited[point1[0]][point1[1]]+1 or visited[x2][y2] >= visited[point2[0]][point2[1]]+1):
                if visited[x1][y1] >= visited[point1[0]][point1[1]] + 1:
                    visited[x1][y1] = visited[point1[0]][point1[1]] + 1
                elif visited[x2][y2] >= visited[point2[0]][point2[1]] + 1:
                    visited[x2][y2] = visited[point2[0]][point2[1]] + 1
                q.append(((x1,y1), (x2,y2), (dest+1)%2))
    for i in range(n+2): print(visited[i])
    return visited[n][n]


print(solution([
    [0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0]
]))

print(solution([
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
]))