def dfs(p): # 배추의 수가 최대 2500개 이므로 1000개가 넘어가서 재귀호춣이 오류가 날 수 있음.
    global arr, r, c # 따라서 반복문을 통한 dfs를 실시
    arr[p[0]][p[1]] = 0
    stack.append(p[:])
    while len(stack) != 0:
        np = stack.pop()
        for i in range(4):
            new_p = [np[0]+di[i], np[1]+dj[i]]
            if 0 <= new_p[0] < r and 0 <= new_p[1] < c and arr[new_p[0]][new_p[1]] == 1:
                stack.append(new_p[:])
                arr[new_p[0]][new_p[1]] = 0

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for _ in range(T):
    r, c, k = map(int, input().split())
    arr = [[0]*c for _ in range(r)]
    stack = []
    count = 0
    for _ in range(k):
        i, j = map(int, input().split())
        arr[i][j] = 1
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 1:
                count += 1
                dfs([i, j])
    print(count)