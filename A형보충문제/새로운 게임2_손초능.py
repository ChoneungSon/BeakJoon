import sys, pprint
def move(x):
    global n, di, dj, arr, nums, visit
    for i in range(n):
        for j in range(n):
            if visit[i][j]:
                flag, move_list = 0, []
                for k in range(len(visit[i][j])):
                    if visit[i][j][k] == x:
                        idx, flag = k, 1
                        move_list.append(visit[i][j][k])
                    elif flag: move_list.append(visit[i][j][k])
                if flag:
                    cnt = 0
                    temp = visit[i][j][0:idx]
                    visit[i][j], nx, ny = temp, i + di[nums[x]], j + dj[nums[x]]
                    while 1:
                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny] == 1:
                                visit[nx][ny] += move_list[::-1]
                                return len(visit[nx][ny])
                            elif arr[nx][ny] == 0:
                                visit[nx][ny] += move_list
                                return len(visit[nx][ny])
                            elif arr[nx][ny] == 2:
                                if cnt == 1: break
                                nx, ny = i-di[nums[x]], j-dj[nums[x]]
                                if cnt == 0:
                                    nums[x] = (nums[x] + 2) % 4
                                cnt += 1
                        else:
                            if cnt == 1: break
                            nx, ny = i - di[nums[x]], j - dj[nums[x]]
                            if cnt == 0:
                                nums[x] = (nums[x] + 2) % 4
                            cnt += 1
                    visit[i][j] += move_list
                    return 1

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
n, num = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[[] for _ in range(n)] for _ in range(n)]
nums, flag = [0] * num, 0
for i in range(num):
    x, y, d = map(int, sys.stdin.readline().split())
    visit[x-1][y-1].append(i)
    if d == 1: nums[i] = 0
    elif d == 2: nums[i] = 2
    elif d == 3: nums[i] = 1
    elif d == 4: nums[i] = 3
for case in range(1, 1001):
    for c in range(num):
        length = move(c)
        if length >= 4:
            print(case)
            flag = 1
            break
    if flag: break
else:
    print(-1)