def calcul(num1, num2, op):
    if op == '+': return int(num1) + int(num2)
    else: return int(num1) - int(num2)

def solution(arr):
    def dfs(arr, op):
        if arr.__len__() == 1: return int(arr[0])
        elif arr.__len__() == 3: return calcul(arr[0], arr[2], arr[1])
        else:
            if op == '+': fun = max
            else: fun = min
            value = calcul(arr[0], dfs(arr[2:], arr[1]), arr[1])
            if arr.__len__() >= 5:
                value = fun(value, calcul(calcul(arr[0], arr[2], arr[1]), dfs(arr[4:], arr[3]), arr[3]))
            return value
    result = dfs(arr, '+')
    return result

def solution1(arr):
    max_value = -2**31
    def dfs(i, total):
        nonlocal arr, max_value
        if i == 0: max_value = max(max_value, total)
        else:
            dfs(i-2, calcul(arr[i-2], total, arr[i-1]))
            if i >= 5:
                dfs(i-4, calcul(calcul(arr[i-4], arr[i-2], arr[i-3]), arr[i], arr[i-1]))
    dfs(arr.__len__() - 1, int(arr[-1]))
    return max_value

def solution2(arr):
    max_list = [0]*(arr.__len__()//2+1)
    min_list = [0]*(arr.__len__()//2+1)
    max_list[-1] = min_list[-1] = int(arr[-1])
    for i in range(arr.__len__()//2-1, -1, -1):
        if arr[2*i+1] == '+':
            max_list[i], min_list[i] = int(arr[2*i]) + max_list[i+1], int(arr[2*i]) + min_list[i+1]
        else:
            max_list[i], min_list[i] = int(arr[2*i]) - min_list[i+1], int(arr[2*i]) - max_list[i+1]
    return max_list[0]

def solution3(arr):
    max_list = [0]*(arr.__len__()//2+1)
    min_list = [0]*(arr.__len__()//2+1)
    max_list[-1] = min_list[-1] = int(arr[-1])
    max_list[-2] = min_list[-2] = calcul(arr[-3], min_list[-1], arr[-2])
    for i in range(arr.__len__()//2-2, -1, -1):
        print(max_list)
        print(min_list)
        cal_list = [
            calcul(calcul(arr[2*i], arr[2*i+2], arr[2*i+1]), max_list[i+2], arr[2*i+3]),
            calcul(calcul(arr[2*i], arr[2*i+2], arr[2*i+1]), min_list[i+2], arr[2*i+3]),
            calcul(arr[2*i], max_list[i+1], arr[2*i+1]),
            calcul(arr[2*i], min_list[i+1], arr[2*i+1]),
        ]
        print(cal_list)
        max_list[i], min_list[i] = max(cal_list), min(cal_list)
    print(max_list)
    print(min_list)
    return max_list[0]

def solution4(arr):
    max_min = [[0]*4 for _ in range(arr.__len__()//2+1)]
    max_min[-1][0] = max_min[-1][1] = max_min[-1][2] = max_min[-1][3] = int(arr[-1])
    max_min[-2][0] = max_min[-2][1] = max_min[-2][2] = max_min[-2][3] = calcul(arr[-3], max_min[-1][0], arr[-2])
    for i in range(arr.__len__()//2-2, -1, -1):
        print(max_min)
        print(max_min)
        max_min[i][0] = max([calcul(calcul(arr[2*i], arr[2*i+2], arr[2*i+1]), max_min[i+2][j], arr[2*i+3]) for j in range(4)])
        max_min[i][1] = min([calcul(calcul(arr[2*i], arr[2*i+2], arr[2*i+1]), max_min[i+2][j], arr[2*i+3]) for j in range(4)])
        max_min[i][2] = max([calcul(arr[2*i], max_min[i+1][j], arr[2*i+1]) for j in range(4)])
        max_min[i][3] = min([calcul(arr[2*i], max_min[i+1][j], arr[2*i+1]) for j in range(4)])
    print(max_min)
    print(max_min)
    return max(max_min[0])

def solution5(arr):
    max_min = [[0]*4 for _ in range(arr.__len__()//2+1)]
    max_min[0][0] = max_min[0][1] = max_min[0][2] = max_min[0][3] = int(arr[0])
    max_min[1][0] = max_min[1][1] = max_min[1][2] = max_min[1][3] = calcul(max_min[0][0], arr[2], arr[1])
    for i in range(2, arr.__len__()//2+1):
        print(max_min)
        print(max_min)
        listA = [calcul(max_min[i-2][j], calcul(arr[2*i-2], arr[2*i], arr[2*i-1]), arr[2*i-3]) for j in range(4)]
        listB = [calcul(max_min[i-1][j], arr[2*i], arr[2*i-1]) for j in range(4)]
        max_min[i][0] = max(listA)
        max_min[i][1] = min(listA)
        max_min[i][2] = max(listB)
        max_min[i][3] = min(listB)
    print(max_min)
    print(max_min)
    return max(max_min[-1])

def solution6(arr):
    n = len(arr)//2 + 1
    visited = [[0]*n for _ in range(n)]
    dpmax, dpmin = [[0]*n for _ in range(n)], [[0]*n for _ in range(n)]
    for i in range(n): dpmax[i][i] = dpmin[i][i] = int(arr[2*i]); visited[i][i] = 1
    def dfs(x, y, op):
        nonlocal visited, dpmax, dpmin, arr
        if visited[x][y]:
            if op == '+': return dpmax[x][y]
            else: return dpmin[x][y]
        else:
            visited[x][y], min_value, max_value = 1, 2**31, -2**31
            for i in range(x, y):
                if arr[2*i+1] == '+':
                    min_value = min(min_value, calcul(dfs(x, i, '-'), dfs(i+1, y, '-'), arr[2*i+1]))
                    max_value = max(max_value, calcul(dfs(x, i, '+'), dfs(i+1, y, '+'), arr[2*i+1]))
                else:
                    min_value = min(min_value, calcul(dfs(x, i, '-'), dfs(i+1, y, '+'), arr[2*i+1]))
                    max_value = max(max_value, calcul(dfs(x, i, '+'), dfs(i+1, y, '-'), arr[2*i+1]))
            dpmin[x][y], dpmax[x][y] = min_value, max_value
            if op == '+': return max_value
            else: return min_value
    return dfs(0, n-1, '+')

print(solution6(['5','-','3','+','1','+','2','-','4']))