import sys, copy, pprint
def dfs(B): # 2. 벽을 세웠을 때, 안전영역을 탐색
    global r, c, min_b
    count = 0
    for i in range(len(bps)):
        stack = [bps[i]]
        while len(stack) != 0:
            np = stack.pop()
            count += 1
            if count > min_b:
                return r*c+1
            for i in range(4):
                new_p = [np[0]+di[i], np[1]+dj[i]]
                if 0 <= new_p[0] < r and 0 <= new_p[1] < c and B[new_p[0]][new_p[1]] == 0:
                    B[new_p[0]][new_p[1]] = 2
                    stack.append(new_p[:])
    return count

def m_arr(m, A): # 1. 벽을 세우는 모든 경우의 수를 출력
    global r, c, min_b
    m_a = copy.deepcopy(A)
    if m == 3:
        b_num = dfs(m_a)
        if b_num < min_b:
            min_b = b_num
    else:
        for i in range(r):
            for j in range(c):
                if m_a[i][j] == 0:
                    m_a[i][j] = 1
                    m_arr(m+1, m_a)
                    m_a[i][j] = 0

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
r, c = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
bps = []
min_b = r*c+1
count_wall = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == 2:
            bps.append((i, j))
        elif arr[i][j] == 1:
            count_wall += 1
m_arr(0, arr)
print(r*c-min_b-count_wall-3)