def dfs(m , k):
    if m == k:
        for i in range(k): # 모든 원소가 배열에 포함 되었을 때, 원소들을 출력
            if i == k-1:
                print(p[i])
            else:
                print(p[i], end=' ')
    else:
        for i in range(k): # 크기가 작은 순서대로 순열의 배열에 추가
            if visited[i] == 0: # 방문하지 않았을 때, 순열의 배열에 추가
                visited[i] = 1 # 방문을 표시
                p[m] = i+1 # 배열에 방문한 원소를 추가
                dfs(m+1, k) # 다음 배열원소를 추가하기 위해 재귀호출
                p[m] = 0 # 재귀호출이 끝나고 재귀호출 이전에 추가되었던 순열 부분을 초기화
                visited[i] = 0 # 방문 표시도 초기화

n = int(input())
visited = [0]*n
p = [0]*n
dfs(0, n)