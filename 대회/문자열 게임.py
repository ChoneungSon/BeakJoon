import sys
def command(d):
    global m, standard
    if d == 'L':
        for i in range(len(m)-len(standard)):
            if m[i] == standard[0]:
                for j in range(1, len(standard)-1):
                    if m[i+j] != standard[j]:
                        break
                else: return (i, j)
    else:
        for i in range(len(m)-len(standard)-1, -1, -1):
            if m[i] == standard[0]:
                for j in range(1, len(standard)-1):
                    if m[i + j] != standard[j]:
                        break
                else: return (i, j)
    return 0

standard = sys.stdin.readline()
m = sys.stdin.readline()
n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    d = str(input())
    flag = command(d)
    if flag:
        cnt += 1
        m = m[0:flag[0]] + m[sum(flag)+1:]
    else:
        print(f'{cnt}\n{m}Perfect!')
        break
else:
    if command(d):
        print(f'{cnt}\n{m}You Lose!')
    else:
        print(f'{cnt}\n{m}Perfect!')