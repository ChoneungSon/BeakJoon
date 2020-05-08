def find_con(lst):
    flag, cnt = 0, 0
    for i in range(10):
        if lst[i] and flag == 0:
            cnt += 1; flag = 1
        elif flag:
            if lst[i]:
                cnt += 1
                if cnt == 3: return 1
            else:
                flag = cnt = 0
    return 0

for case in range(1, int(input())+1):
    cards, result = list(map(int, input().split())), 0
    player1, player2 = [0] * 10, [0] * 10
    for i in range(12):
        print(player1, player2)
        if i%2:
            player2[cards[i]] += 1
            if player2[cards[i]] == 3:
                result = 2; break
            else:
                if find_con(player2): result = 2; break
        else:
            player1[cards[i]] += 1
            if player1[cards[i]] == 3:
                result = 1; break
            else:
                if find_con(player1): result = 1; break
    else: result = 0
    print('#{} {}'.format(case, result))

