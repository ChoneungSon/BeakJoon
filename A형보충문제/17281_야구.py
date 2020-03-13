import sys
from itertools import permutations
def game(list_v):
    global n, arr, max_s
    num, score = -1, 0
    for inn in arr:
        b1 = b2 = b3 = out = 0
        while out < 3:
            num = (num+1)%9
            if inn[list_v[num]] == 0:
                out += 1
            elif inn[list_v[num]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif inn[list_v[num]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif inn[list_v[num]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                score += b1 + b2 + b3 + 1
                b1 = b2 = b3 = 0
    max_s = max(score, max_s)

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_s = 0
cut = 0
for i in permutations(range(1, 9)):
    v = list(map(int, i))
    game(v[:3] + [0] + v[3:])
print(max_s)