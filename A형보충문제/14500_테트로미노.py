import sys
tet = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (-1, 2)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (2, 0), (2, 1)], 
    [(0, 0), (1, 0), (0, 1), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (-1, 1), (-2, 1)],
    [(0, 0), (0, 1), (-1, 1), (-1, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (-1, 0), (-1, 1), (-2, 1)],
    [(0, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (0, 1), (-1, 1), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 0)],
    [(0, 0), (1, 0), (1, -1), (2, 0)]
]

def find(x, y):
    global arr, answer
    for i in range(19):
        result = 0
        for j in range(4):
            next_x = x+tet[i][j][0]
            next_y = y+tet[i][j][1]
            if 0 <= next_x < r and 0 <= next_y < c:
                result += arr[next_x][next_y]
        if result > answer:
            answer = result

r, c = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
answer = 0
for i in range(r):
    for j in range(c):
        find(i,j)
print(answer)