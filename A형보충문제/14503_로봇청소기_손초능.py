di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
r, c = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
count, rot_cnt = 1, 0
arr[x][y] = 2 # 처음 영역 청소
while 1:
    nx = x + di[(d+3)%4] # 왼쪽 부분부터 회전
    ny = y + dj[(d+3)%4]
    rot_cnt += 1 # 회전 수 표시
    if arr[nx][ny] == 0: # 청소 X, 로봇의 위치 변경 및 방향 변경
        arr[nx][ny] = 2
        x, y = nx, ny
        d = (d+3) % 4
        rot_cnt = 0 # 회전 수 초기화
        count += 1 # 청소 영역 수 증가
    elif rot_cnt < 4: # 로봇이 왼쪽으로 회전했을 때, 아직 한 바퀴를 전부 탐색하지 않았으면, 다른 방향을 탐색
        d = (d+3) % 4
    elif rot_cnt == 4: # 한 바퀴를 전부 탐색했을 때,
        d = (d+3)%4
        x -= di[d] # 뒤로 한 칸 이동
        y -= dj[d]
        rot_cnt = 0
        if arr[x][y] == 1: # 뒤로 이동했을 때, 벽이면 중지
            break
print(count)