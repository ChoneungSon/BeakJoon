import sys
def find(p, ep):
    global arr, n, big
    np = p[:]
    queue = [np]
    visited = [[0]*n for _ in range(n)]
    count = 0
    lenq = 1
    while lenq != 0:
        count += 1
        for k in range(lenq):
            for i in range(4):
                new = [queue[k][0]+di[i], queue[k][1]+dj[i]]
                if new == ep:
                    return count
                elif 0 <= new[0] < n and 0 <= new[1] < n and arr[new[0]][new[1]] <= big and visited[new[0]][new[1]] == 0:
                    queue.append(new[:])
                    visited[new[0]][new[1]] = 1
        for i in range(lenq):
            queue.pop(0)
        lenq = len(queue)
    return 0
    
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
big, stack = 2, 0
count = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            sp = [i, j]
            break
while 1:
    m_len = n**2+1 
    ep = 0
    for i in range(n):
        for j in range(n):
            if 1 <= arr[i][j] < big:
                length = find(sp, [i, j])
                if length:
                    if m_len > length:
                        m_len = length
                        ep = [i, j]
    if ep:
        stack += 1
        arr[ep[0]][ep[1]] = n**2+1
        arr[sp[0]][sp[1]] = 0
        sp = ep[:]
        count += m_len
        if stack == big:
            big += 1
            stack = 0
    else:
        print(count)
        break