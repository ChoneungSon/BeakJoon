# 각 사람들은 오고 가기 위해 최단 시간으로 이동한다.

# x를 출발지로 하는 경우의 수를 구한다. 다익스트라 이용

# 다익스트라 공부하자!!! 오늘하자!!!
import heapq

def djikstra():
    global adj, enter_exit, n, home
    visit = [0]*n
    x = home - 1
    enter_exit[x][0] = 0
    for _ in range(n):
        visit[x] = 1
        idx, min_value = -1, float('inf')
        for i in range(n):
            if not visit[i]:
                if adj[x][i] and enter_exit[i][0] > enter_exit[x][0] + adj[x][i]:
                    enter_exit[i][0] = enter_exit[x][0] + adj[x][i]
                if min_value > enter_exit[i][0]:
                    idx, min_value = i, enter_exit[i][0]
        x = idx

    visit = [0] * n
    x = home - 1
    enter_exit[x][1] = 0
    for _ in range(n):
        visit[x] = 1
        idx, min_value = -1, float('inf')
        for i in range(n):
            if not visit[i]:
                if adj[i][x] and enter_exit[i][1] > enter_exit[x][1] + adj[i][x]:
                    enter_exit[i][1] = enter_exit[x][1] + adj[i][x]
                if min_value > enter_exit[i][1]:
                    idx, min_value = i, enter_exit[i][1]
        x = idx

for case in range(1, int(input())+1):
    n, m, home = map(int, input().split())
    adj = [[0]*n for _ in range(n)]
    for _ in range(m):
        x, y, t = map(int, input().split())
        adj[x-1][y-1] = t
    enter_exit = [[float('inf')]*2 for _ in range(n)]
    djikstra()
    print('#{} {}'.format(case, sum(max(enter_exit, key=lambda x: sum(x)))))