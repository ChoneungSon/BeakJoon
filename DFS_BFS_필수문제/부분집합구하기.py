def dfs(m, k): # m은 재귀함수의 깊이, k는 재귀깊이의 제한점을 입력
    global p_list, A
    if m == k:
        p = []
        for i in range(len(A)):
            if visited[i] == 1:
                p.append(A[i])
        p_list.append(p)
    else:
        dfs(m+1, k) # 방문을 표시하지 않고, 재귀호출
        visited[m] = 1
        dfs(m+1, k) # 방문을 표시하고, 재귀호출
        visited[m] = 0 # 이후 방문기록의 초기화를 진행

# n = int(input())
A = [1,2,3]
visited = [0]*len(A)
p_list = [] # 부분집합이 들어갈 빈 배열 지정
dfs(0, len(A))
print(p_list)