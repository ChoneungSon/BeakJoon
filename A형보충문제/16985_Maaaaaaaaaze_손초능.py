def select(m, v):
    global choose, min_length
    if m == 5:
        for i in range(4):
            rot(v[1])
            for j in range(4):
                rot(v[2])
                for k in range(4):
                    rot(v[3])
                    for l in range(4):
                        rot(v[4])
                        for d in range(4):
                            if arr[v[0]][rotj[d]][rotk[d]] == 1 and arr[v[4]][rotj[(d+2)%4]][rotk[(d+2)%4]] == 1:
                                bfs(d, v[:])
                                if min_length == 12: # 12가 모든 문제에서 가장 최소값이 될 수 있는 수 따라서 12가 이미 최솟값이면 함수 진행 X
                                    return
    else:
        for i in range(5):
            if v[i] == -1:
                v[i] = m
                select(m+1, v[:])
                v[i] = -1

def rot(x): # 배열 돌리기 함수
    global arr
    rot_arr = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            rot_arr[i][j] = arr[x][4-j][i]
    for i in range(5):
        for j in range(5):
            arr[x][i][j] = rot_arr[i][j]

def bfs(d, v):
    global min_length
    q = [(0, rotj[d], rotk[d], 0)]
    visit = [[[0]*5 for _ in range(5)] for _ in range(5)]
    while q:
        x, y, k, l = q.pop(0)
        for i in range(6):
            nx, ny, nk = x+di[i], y+dj[i], k+dk[i]
            if l >= min_length: # 앞에서 결정된 min_length보다 같거나 크면 탐색안함
                break
            elif 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nk < 5 and visit[v[nx]][ny][nk] == 0 and arr[v[nx]][ny][nk] == 1:
                visit[v[nx]][ny][nk] = 1
                q.append((nx, ny, nk, l+1))
                if nx == 4 and ny == rotj[(d + 2) % 4] and nk == rotk[(d + 2) % 4]:
                    if l+1 < min_length:
                        min_length = l+1
import pprint
di = [1, -1, 0, 0, 0, 0] # 탐색방향의 설정
dj = [0, 0, 0, 1, 0, -1]
dk = [0, 0, 1, 0, -1, 0]
rotj = [0, 0, 4, 4] # 시작되는 좌표의 설정
rotk = [0, 4, 4, 0]
arr = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
choose = []
min_length = 5**3 + 1
select(0, [-1]*5)
if min_length != 126:
    print(min_length)
else:
    print(-1)