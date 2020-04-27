def solution(food_times, k):
    left, right = 0, 100000001
    while 1:
        mean, count = (left + right) // 2, 0
        cand_times = food_times[:]
        for i in range(len(food_times)):
            if cand_times[i]:
                if cand_times[i] >= mean:
                    count += mean - left
                    if cand_times[i] == mean: cand_times[i] = 0
                else:
                    right = mean
                    break
        else:
            if k >= count:
                k -= count
                food_times, left, right = cand_times[:], mean, 100000001
                if k == count:
                    for i in range(len(food_times)):
                        if food_times[i]: return i + 1
            else:
                right = mean
        if right - left == 1: break
    return -1


print(solution([3, 1, 2], 5))