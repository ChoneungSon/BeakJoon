def solution(board, moves):
    stack, point, cnt = [], [-1]*len(board), 0
    for i in range(len(board[0])):
        p = point[i]
        while 1:
            p += 1
            if p == len(board[0]) or board[p][i]:
                point[i] = p
                break
    for i in range(len(moves)):
        p = moves[i] - 1
        if point[p] != len(board):
            if stack and stack[-1] == board[point[p]][p]:
                stack.pop()
                cnt += 2
            else: stack.append(board[point[p]][p])
            point[p] += 1
    return cnt

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))