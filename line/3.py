def solution(road, n):
    arr, cnt, flag = [], 1, road[0]
    for i in range(1, len(road)):
        if flag != road[i]:
            arr.append((flag, cnt))
            flag, cnt = road[i], 1
        else: cnt += 1
    for i in range(len(arr)):
        if arr[i][0] == '0':
            if arr[i][0] < n:
                pass
            elif arr[i][0] == n:
                pass
            else:
                pass

solution("111011110011111011111100011111")