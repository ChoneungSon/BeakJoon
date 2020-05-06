port_num = int(input()); air = int(input())
ports, count, flag = dict(), 0, 0
for _ in range(air):
    i = int(input())
    while 1:
        if i not in ports:
            if i <= 0:
                # i가 점점 줄어들기 때문에 0 이하가 되면 현재 상태에서 넣을 수 있는 곳이 없다는 것
                flag = 1
                break
            ports[i] = i - 1 # i에 i 대신 이동할 위치를 저장한다.
            count += 1 # 넣어진 비행기 수를 증가
            break
        temp = i # 일단 i가 저장되어 있기 때문에 i가 이동해야 할 위치를 수정해줘야 함
        i = ports[i] # i 대신에 가야할 위치를 꺼내준다.
        if ports.get(i): # 만약 i 대신에 가야할 위치도 존재한다면,
            ports[temp] = ports[i] - 1 # temp에서 이동해야 할 위치를 다음과 같이 수정한다.
    if flag: break
print(count)