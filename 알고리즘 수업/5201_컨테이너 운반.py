for case in range(1, int(input())+1):
    container, trucks = map(int, input().split())
    goods = sorted(list(map(int, input().split())), reverse=True)
    max_carry = sorted(list(map(int, input().split())), reverse=True)
    truck, result = 0, 0
    for i in range(container):
        if goods[i] <= max_carry[truck]:
            result += goods[i]
            truck += 1
            if truck == trucks: break
    print('#{} {}'.format(case, result))
