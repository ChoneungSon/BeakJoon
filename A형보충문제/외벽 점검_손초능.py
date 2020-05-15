def solution(n, weak, dist):
    if len(weak) == 1: return 1
    length, min_cnt = [0] * len(weak), 9
    dist = sorted(dist, key=lambda x: -x)
    for i in range(len(weak)):
        if i == len(weak) - 1: length[i] = n+weak[0] - weak[i]
        else: length[i] = weak[i+1] - weak[i]
    def dfs(x, y, sum, end):
        nonlocal length, dist, min_cnt
        if min_cnt <= y: return
        sum += length[x]
        x = (x+1) % len(length)
        if sum > dist[y]: sum, y = 0, y+1
        if x == end: min_cnt = min(min_cnt, y)
        else: dfs(x, y, sum, end)
    for i in range(len(weak)): dfs(i, 0, 0, (i+n-2)%len(weak))
    if min_cnt == 9: return -1
    else: return min_cnt+1

def solution1(n, weak, dist):
    if len(weak) == 1: return 1
    length, min_cnt = [0] * len(weak), 9
    dist = sorted(dist, key=lambda x: -x)
    for i in range(len(weak)):
        if i == len(weak) - 1: length[i] = n+weak[0] - weak[i]
        else: length[i] = weak[i+1] - weak[i]
    for i in range(len(length)):
        sum = y = 0
        for j in range(len(length)-1):
            x = (i+j) % len(length)
            sum += length[x]
            if sum > dist[y]:
                sum, y = 0, y+1
                if y >= len(dist): break
        else: min_cnt = min(min_cnt, y)
    if min_cnt == 9: return -1
    else: return min_cnt+1

def solution2(n, weak, dist):
    if len(weak) == 1: return 1
    length, min_cnt, visited = [0]*len(weak), 9, [0]*len(dist)
    dist = sorted(dist, key=lambda x:-x)
    for i in range(len(weak)):
        if i == len(weak) - 1: length[i] = n+weak[0] - weak[i]
        else: length[i] = weak[i+1] - weak[i]
    def dfs(x, y, sum, cnt, end):
        nonlocal length, dist, min_cnt, visited
        if x == end: min_cnt = min(min_cnt, cnt)
        elif min_cnt <= cnt: return
        else:
            while sum <= dist[y]:
                if x == end: min_cnt = min(min_cnt, cnt)
                sum += length[x]
                x = (x+1) % len(length)
            for i in range(len(dist)):
                if not visited[i]:
                    visited[i] = 1
                    dfs(x, i, 0, cnt+1, end)
                    visited[i] = 0
    for i in range(len(length)):
        for j in range(len(dist)):
            visited[j] = 1
            dfs(i, j, 0, 1, (i+len(length)-1)%len(length))
            visited[j] = 0
    if min_cnt == 9: return -1
    else: return min_cnt

print(solution2(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# 4, 1, 4, 3
print(solution2(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# 2, 1, 5, 1, 3
print(solution2(20, [1, 10], [2, 9]))
print(solution2(25, [1, 6, 10, 13, 16, 19], [1, 1, 8]))
# 5, 4, 3, 3, 3, 6
print(solution2(2, [0, 1], [1, 1, 1, 1, 1]))
print(solution2(50, [1, 5, 10, 16, 22, 25], [3, 4, 6]))
# 4 5 6 6 3 26