import sys, copy
def find(p):
    global r, c, limit, copy_arr
    for d in range(1, limit+1):
        for i in range(-(d-1), d):
            np = [r-(d-abs(i)), p+i]
            if 0 <= np[0] < r and 0 <= np[1] < c and copy_arr[np[0]][np[1]] >= 1:
                return np
    return 0

r, c, limit = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
max_count = 0

for k1 in range(c-2):
    for k2 in range(k1+1, c-1):
        for k3 in range(k2+1, c):
            count = 0
            copy_arr = copy.deepcopy(arr)
            for _ in range(r):    
                rmp = []
                for k in [k1, k2, k3]:
                    rm = find(k)
                    if rm:
                        copy_arr[rm[0]][rm[1]] += 1 # 맞은 적을 바로 없애지 않고 +1을 추가함
                for i in range(r):
                    for j in range(c):
                        if copy_arr[i][j] > 1:
                            copy_arr[i][j] = 0
                            count += 1
                copy_arr.pop()
                copy_arr.insert(0, [0]*c)
            if count > max_count:
                max_count = count
print(max_count)