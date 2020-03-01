import sys
def find(x, y, d): # 구슬의 좌표와 방향을 받아서 이동할 수 있는 점을 리턴
    global r, c, arr
    count = 0
    while 1:
        x += di[d]
        y += dj[d]
        count += 1
        if arr[x][y] == '#': # 벽에 닿으면 flag를 1로 리턴
            return [x-di[d], y-dj[d]], count-1, 1
        elif arr[x][y] == 'O': # 구멍에 빠지면 flag를 0으로 리턴
            return [x, y], count, 0

def dfs(red, blue, cnt):
    global arr, r, c, min_cnt
    if cnt >= min_cnt: # 최소 cnt가 넘어가면 중단
        return
    else:
        for i in range(4): # 각 방향으로 기울이기
            nrp, rlen, rflag = find(red[0], red[1], i)
            nbp, blen, bflag = find(blue[0], blue[1], i)
            if bflag and rflag: # 둘다 벽에 닿았을 때
                if nrp == nbp: # 리턴된 최종 좌표가 같을 때
                    if rlen > blen: # 원래 좌표에서 최종 좌표까지의 거리가 먼 쪽이 최종좌표보다 현재 방향의 1 뒤에 있는 좌표로 최종좌표를 변경
                        nrp[0] -= di[i]
                        nrp[1] -= dj[i]
                    else:
                        nbp[0] -= di[i]
                        nbp[1] -= dj[i]
                if nrp == red and nbp == blue:
                    continue # 이동한 좌표가 이동하기 전 좌표와 같으면 넘어가기
                dfs(nrp[:], nbp[:], cnt+1) # 새 좌표로 cnt 변경하여 재귀호출
            else: # 둘 중 하나가 구멍에 빠졌을 때
                if not bflag: # 파란구슬이 빠지면 실패
                    continue
                elif not rflag: # 파란구슬이 빠지지 않고, 빨간구슬이 빠지면 성공
                    if cnt < min_cnt:
                        min_cnt = cnt

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
r, c = map(int, sys.stdin.readline().split())
arr = [list(input()) for _ in range(r)]
min_cnt = 10
for i in range(r):
    for j in range(c): # 각 구슬의 위치를 저장하고, 자리를 점으로 바꾼다.
        if arr[i][j] == 'R':
            rp = [i, j]
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            bp = [i, j]
            arr[i][j] = '.'
dfs(rp[:], bp[:], 0)
if min_cnt == 10:
    min_cnt = -2
print(min_cnt+1)