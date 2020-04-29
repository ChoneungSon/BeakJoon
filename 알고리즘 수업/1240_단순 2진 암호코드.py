for case in range(1, int(input())+1):
    r, c = map(int, input().split())
    arr = [input() for _ in range(r)]
    code_list = []
    for i in range(r):
        p, total, cnt, code, flag = c, 0, 0, [0]*8, 0
        while p >= 6:
            p -= 1
            if arr[i][p]:
                num, count = 0, 1
                for j in range(p-1, p-7, -1):
                    if arr[i][j] != arr[i][j+1]:
                        num += count; count = 1
                    else: count += 1
                cnt += 1; code[8-cnt] = num; p -= 6
                if cnt == 1 or cnt % 2 == 0: total += num
                else: total += num*3
            if cnt == 8 and total % 10 == 0:
                flag = 1
                break
        if flag: code_list.append(code[:])
        else: code_list.append([0]*8)
    print(code_list)