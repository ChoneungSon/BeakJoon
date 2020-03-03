def find():
    global arr, r, c
    for i in range(c):
        x = 0
        y = i
        while x < r:
            for j in range(2):
                if arr[x][y+j] == 1:
                    if j == 0:
                        y -= 1
                    else:
                        y += 1
                    break
            x += 1
        if y != i:
            return 0
    return 1

def brute():
    global arr, r, c, min_cnt
    for i in range(r*(c+2)):
        xi, yi = i//(c+2), i%(c+2)
        if yi != 0 and yi != c+1 and arr[xi][yi] == 0 and arr[xi][yi-1] == 0 and arr[xi][yi+1] == 0:
            arr[xi][yi] = 1
            if find():
                min_cnt = 1
            elif min_cnt > 2:
                for j in range(i+1, r*(c+2)):
                    xj, yj = j//(c+2), j%(c+2)
                    if yj != 0 and yj != c + 1 and arr[xj][yj] == 0 and arr[xj][yj-1] == 0 and arr[xj][yj+1] == 0:
                        arr[xj][yj] = 1
                        if find():
                            if min_cnt > 2:
                                min_cnt = 2
                        elif min_cnt > 3:
                            for k in range(j+1, r*(c+2)):
                                xk, yk = k//(c+2), k%(c+2)
                                if yk != 0 and yk != c + 1 and arr[xk][yk] == 0 and arr[xk][yk-1] == 0 and arr[xk][yk+1] == 0:
                                    arr[xk][yk] = 1
                                    if find():
                                        if min_cnt > 3:
                                            min_cnt = 3
                                    arr[xk][yk] = 0
                        arr[xj][yj] = 0
            arr[xi][yi] = 0

c, m, r = map(int, input().split())
arr = [[0]*(c+2) for _ in range(r)]
min_cnt = 4
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b] = 1
if find():
    print(0)
else:
    brute()
    if min_cnt == 4:
        print(-1)
    else:
        print(min_cnt)