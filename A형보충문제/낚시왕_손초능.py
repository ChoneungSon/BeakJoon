import sys, copy, pprint
def catch(x): # 이동했을 때, 가장 윗 부분의 고기를 잡는 함수
    global arr, r, c
    for i in range(r):
        if arr[i][x]:
            temp, arr[i][x] = arr[i][x][4], 0
            return temp
    return 0

def move(): # 물고기의 위치를 변환하는 함수
    global arr, r, c
    visit = [0] * (r*c)
    v = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j]:
                if arr[i][j][0] or arr[i][j][1]: # 변화하는 좌표의 수가 둘 중에 하나가 0이 아니면, 좌표를 변경
                    arr[i][j][2] = (arr[i][j][2] + arr[i][j][0]) % (2*r - 2) # 현재 좌표에서 초마다 이동하는 좌표 변환의 수만 더하고 간단한 인덱스 연산을 통해 
                    arr[i][j][3] = (arr[i][j][3] + arr[i][j][1]) % (2*c - 2) # 나중 위치를 정함
                if visit[dr[arr[i][j][2]]*c + dc[arr[i][j][3]]] < arr[i][j][4]:
                    visit[dr[arr[i][j][2]]*c + dc[arr[i][j][3]]] = arr[i][j][4]
                    v[dr[arr[i][j][2]]][dc[arr[i][j][3]]] = arr[i][j][:]
    return v

di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]
r, c, num = map(int, sys.stdin.readline().split())
arr = [[0]*c for _ in range(r)]
total = 0
dr = list(map(int, range(r))) + list(map(int, range(r-2, 0, -1))) # 행과 열에 대해 물고기가 이동할 수 있는 칸의 리스트를 순서대로 저장 
dc = list(map(int, range(c))) + list(map(int, range(c-2, 0, -1)))
for _ in range(num):
    x, y, v, d, big = map(int, sys.stdin.readline().split())
    arr[x-1][y-1] = [v*di[d-1], v*dj[d-1], x-1, y-1, big] # arr의 물고기가 있는 부분에 초마다 이동하는 좌표 변환의 수, 현재 좌표, 크기를 저장
total += catch(0)                                         # 방향과 속도만 정해주면 이후에는 좌표에 대한 연산이 복잡하지 않음
for i in range(1, c):
    arr = move()
    total += catch(i)
print(total)