import sys, copy
def find(p):
    global r, c, limit, copy_arr
    for d in range(1, limit+1):
        for i in range(1, d+1):
            for j in range(-(d-abs(i)), d-abs(i)+1):
                np = [r-i, p+j]
                if 0 <= np[0] < r and 0 <= np[1] < c and copy_arr[np[0]][np[1]] == 1:
                    return np
    return 0

r, c, limit = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
max_count = 0

for k1 in range(c-2):
    for k2 in range(k1+1, c-1):
        for k3 in range(k2+1, c):
            k1, k2, k3 = 0, 2, 4
            count = 0
            copy_arr = copy.deepcopy(arr)
            for _ in range(r):    
                rmp = []
                for k in [k1, k2, k3]:
                    rm = find(k)
                    if rm and rm not in rmp: # 화살을 맞은 적을 +1 해서 표시
                        rmp.append(rm[:])
                for k in rmp:
                    copy_arr[k[0]][k[1]] = 0
                    count += 1
                copy_arr.pop()
                copy_arr.insert(0,[0]*c)
            if count > max_count:
                max_count = count
                print(k1, k2, k3)
                print(max_count)
print(max_count)