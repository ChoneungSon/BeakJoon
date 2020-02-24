n = int(input())
pp = [0]*n
for i in range(n):
    pp[i] = list(map(int, input().split()))
for i in range(n):
    count = 0
    for j in range(n):
        if pp[i][0] < pp[j][0] and pp[i][1] < pp[j][1]:
            count += 1
    if i == n-1:
        print(count+1)
    else:
        print(count+1, end=' ')