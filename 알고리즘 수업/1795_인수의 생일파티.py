# 각 사람들은 오고 가기 위해 최단 시간으로 이동한다.

# x를 출발지로 하는 경우의 수를 구한다. 다익스트라 이용

# 다익스트라 공부하자!!! 오늘하자!!!

for case in range(1, int(input())+1):
    n, m, home = map(int, input().split())
    adj = [[float('inf')]*n for _ in range(n)]
    for _ in range(m):
        x, y, t = map(int, input().split())
        adj[x-1][y-1] = t
    enter = [float('inf')]*n
    exit_ = [float('inf')]*n
