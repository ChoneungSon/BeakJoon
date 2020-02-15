def dfs(p):
    global arr, count, n
    arr[p[0]][p[1]] = '0' # main 부분에서 가구의 탐색시 중복탐색을 방지하기 위해 탐색된 부분의 원소를 '0'으로 초기화
    count += 1 # 가구의 수를 파악하기 위해 탐색성공시 count를 1씩 증가시킴
    for i in range(4):
        np = [p[0]+di[i], p[1]+dj[i]] # 각 방향마다 인접 가구가 있는지를 판별
        if 0 <= np[0] < n and 0 <= np[1] < n and arr[np[0]][np[1]] == '1':
            dfs(np) # 인접 가구 발견시 새로운 좌표로 이동하여 재귀호출

di = [0, 1, 0, -1] # 우, 하, 좌, 상
dj = [1, 0, -1, 0]
n = int(input())
arr = [list(input()) for _ in range(n)]
counts = []
for i in range(n):
    for j in range(n): # 배열의 각 부분을 순회하며
        if arr[i][j] == '1': # 원소가 '1'인 부분을 찾음
            count = 0 # 인접하는 가구의 수를 나타내기 위해 count 변수를 이용
            dfs([i, j])
            counts.append(count) # 인접하는 가구의 탐색이 끝나면 그 부분을 하나의 단지로 판단하고 counts 배열에 삽입
counts = sorted(counts)
print(len(counts))
for i in range(len(counts)):
    print(counts[i])