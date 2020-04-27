port_num = int(input()); air = int(input())
ports, count, flag = dict(), 0, 0
for _ in range(air):
    i = int(input())
    while 1:
        if i not in ports:
            if i <= 0:
                flag = 1
                break
            ports[i] = i - 1
            count += 1
            break
        temp = i
        i = ports[i]
        if ports.get(i):
            ports[temp] = ports[i] - 1
    if flag: break
print(count)