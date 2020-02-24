def dfs(m, v): # dfs로 각 기회별로 구슬을 떨어뜨릴 방법을 visited에 append 하는 함수
    global n, r, c, arr, visited
    if m == n:
        visited.append(v[:])
    else:
        for i in range(c):
            v[m] = i
            dfs(m+1, v[:])

def rm(p, d, amp):
    global n, r, c, copy_arr, di, dj
    if amp == 0 or not(0 <= p[0] < r and 0 <= p[1] < c): # 입력 점이 arr의 공간을 넘어가거나 이전 amp이 1인 경우에 함수 호출
        return
    else:
        namp = copy_arr[p[0]][p[1]]
        copy_arr[p[0]][p[1]] = 0
        if amp < namp: # 새로 터진 블록의 값이 현재의 반경 보다 클 때, 폭발 범위가 증가하므로 amp를 변경
            amp = namp
        for i in range(4): # 각 방향별로 블록을 제거
            np = [p[0]+di[i], p[1]+dj[i]]
            if 0 <= np[0] < r and 0 <= np[1] < c:
                if d == i:
                    rm(np[:], d, amp-1) # 이전에 터졌던 블록과 방향이 같은 블록, 최신화된 폭발반경을 가짐
                else:
                    if namp != 0: # 이전에 터졌던 블록과 방향이 다른 블록
                        rm(np[:], i, namp-1) # 그 블록이 가지고 있는 폭발 반경과 같음
            
def sort_arr(): # 제거된 블록을 정리
    global copy_arr, r, c
    for i in range(c):
        for j in range(r-1, -1, -1):
            if copy_arr[j][i] == 0:
                x = j
                while 1:
                    x -= 1
                    if 0 <= x and copy_arr[x][i] != 0:
                        copy_arr[j][i], copy_arr[x][i] = copy_arr[x][i], copy_arr[j][i]
                        break
                    elif x < 0:
                        break

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for case in range(1, T+1):
    n, c, r = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(r)]
    visited = []
    visit = [0]*n
    dfs(0, visit)
    min_count = r*c+1
    for i in range(len(visited)):
        v_list = visited[i]
        count = 0
        copy_arr = [[0]*c for _ in range(r)]
        for j in range(r):
            for k in range(c):
                copy_arr[j][k] = arr[j][k]
        for j in range(n):
            for k in range(r):
                if copy_arr[k][v_list[j]] != 0: # 선택된 줄에서 가장 위의 블록을 찾음
                    a = copy_arr[k][v_list[j]]
                    copy_arr[k][v_list[j]] = 0 # 블록을 제거하고
                    for k1 in range(3): # 폭발 반경내의 블록을 검색
                        rm([k+di[k1], v_list[j]+dj[k1]], k1, a-1)
                    break
            sort_arr()
        for j in range(r):
            for k in range(c):
                if copy_arr[j][k] != 0:
                    count += 1
        if min_count > count:
            min_count = count
        if min_count == 0:
            break
    print('#{0} {1}'.format(case, min_count))