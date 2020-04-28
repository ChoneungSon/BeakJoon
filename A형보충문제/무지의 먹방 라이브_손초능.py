def solution(food_times, k):
    i, length, pre, sort_time = 0, len(food_times), 0, sorted(food_times)
    if sum(food_times) <= k: return -1
    while i < len(food_times):
        if pre != sort_time[i]:
            if k >= (sort_time[i] - pre) * length:
                k -= (sort_time[i] - pre) * length
                pre = sort_time[i]
            else:
                k, cnt = k%length+1, 0
                for j in range(len(food_times)):
                    if food_times[j] > pre:
                        cnt += 1
                        if cnt == k: return j+1
        i += 1
        length -= 1

print(solution([5]*10, 15))